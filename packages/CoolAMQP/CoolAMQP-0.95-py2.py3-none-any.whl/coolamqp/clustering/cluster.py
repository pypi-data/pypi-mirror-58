# coding=UTF-8
"""
THE object you interface with
"""
from __future__ import print_function, absolute_import, division
import six
import logging
import warnings
import time
import monotonic
from coolamqp.uplink import ListenerThread
from coolamqp.clustering.single import SingleNodeReconnector
from coolamqp.attaches import Publisher, AttacheGroup, Consumer, Declarer
from coolamqp.objects import Exchange
from coolamqp.exceptions import ConnectionDead
from concurrent.futures import Future

from coolamqp.clustering.events import ConnectionLost, MessageReceived, \
    NothingMuch

logger = logging.getLogger(__name__)

THE_POPE_OF_NOPE = NothingMuch()


class Cluster(object):
    """
    Frontend for your AMQP needs.

    This has ListenerThread.

    Call .start() to connect to AMQP.

    It is not safe to fork() after .start() is called, but it's OK before.
    """

    # Events you can be informed about
    ST_LINK_LOST = 0  # Link has been lost
    ST_LINK_REGAINED = 1  # Link has been regained

    def __init__(self, nodes, on_fail=None):
        """
        :param nodes: list of nodes, or a single node. For now, only one is supported.
        :type nodes: NodeDefinition instance or a list of NodeDefinition instances
        :param on_fail: callable/0 to call when connection fails in an
            unclean way. This is a one-shot
        :type on_fail: callable/0
        """
        from coolamqp.objects import NodeDefinition
        if isinstance(nodes, NodeDefinition):
            nodes = [nodes]

        if len(nodes) > 1:
            raise NotImplementedError(u'Multiple nodes not supported yet')

        self.node, = nodes

        if on_fail is not None:
            def decorated():
                if not self.listener.terminating:
                    on_fail()

            self.on_fail = decorated
        else:
            self.on_fail = None

    def declare(self, obj, persistent=False):
        """
        Declare a Queue/Exchange
        :param obj: Queue/Exchange object
        :param persistent: should it be redefined upon reconnect?
        :return: Future
        """
        return self.decl.declare(obj, persistent=persistent)

    def drain(self, timeout):
        """
        Return an Event.
        :param timeout: time to wait for an event. 0 means return immediately. None means block forever
        :return: an Event instance. NothingMuch is returned when there's nothing within a given timoeout
        """
        try:
            if timeout == 0:
                return self.events.get_nowait()
            else:
                return self.events.get(True, timeout)
        except six.moves.queue.Empty:
            return THE_POPE_OF_NOPE

    def consume(self, queue, on_message=None, *args, **kwargs):
        """
        Start consuming from a queue.

        args and kwargs will be passed to Consumer constructor (coolamqp.attaches.consumer.Consumer).
        Don't use future_to_notify - it's done here!

        Take care not to lose the Consumer object - it's the only way to cancel a consumer!

        :param queue: Queue object, being consumed from right now.
            Note that name of anonymous queue might change at any time!
        :param on_message: callable that will process incoming messages
                           if you leave it at None, messages will be .put into self.events
        :type on_message: callable(ReceivedMessage instance) or None
        :return: a tuple (Consumer instance, and a Future), that tells, when consumer is ready
        """
        fut = Future()
        fut.set_running_or_notify_cancel()  # it's running right now
        on_message = on_message or (
            lambda rmsg: self.events.put_nowait(MessageReceived(rmsg)))
        con = Consumer(queue, on_message, future_to_notify=fut, *args,
                       **kwargs)
        self.attache_group.add(con)
        return con, fut

    def delete_queue(self, queue):
        """
        Delete a queue.

        :param queue: Queue instance that represents what to delete
        :return: a Future (will succeed with None or fail with AMQPError)
        """
        return self.decl.delete_queue(queue)

    def publish(self, message, exchange=None, routing_key=u'', tx=None,
                confirm=None):
        """
        Publish a message.

        :param message: Message to publish
        :param exchange: exchange to use. Default is the "direct" empty-name exchange.
        :type exchange: unicode/bytes (exchange name) or Exchange object.
        :param routing_key: routing key to use
        :param confirm: Whether to publish it using confirms/transactions.
                        If you choose so, you will receive a Future that can be used
                        to check it broker took responsibility for this message.
                        Note that if tx if False, and message cannot be delivered to broker at once,
                        it will be discarded.
        :param tx: deprecated, alias for confirm
        :return: Future or None
        """
        if isinstance(exchange, Exchange):
            exchange = exchange.name.encode('utf8')
        elif exchange is None:
            exchange = b''
        else:
            exchange = exchange.encode('utf8')

        if isinstance(routing_key, six.text_type):
            routing_key = routing_key.encode('utf8')

        if tx is not None:  # confirm is a drop-in replacement. tx is unfortunately named
            warnings.warn(u'Use confirm kwarg instead', DeprecationWarning)

            if confirm is not None:
                raise RuntimeError(
                    u'Using both tx= and confirm= at once does not make sense')
        elif confirm is not None:
            tx = confirm
        else:
            tx = False

        try:
            return (self.pub_tr if tx else self.pub_na).publish(message,
                                                                exchange,
                                                                routing_key)
        except Publisher.UnusablePublisher:
            raise NotImplementedError(
                u'Sorry, this functionality is not yet implemented!')

    def start(self, wait=True, timeout=10.0):
        """
        Connect to broker. Initialize Cluster.

        Only after this call is Cluster usable.
        It is not safe to fork after this.

        :param wait: block until connection is ready
        :param timeout: timeout to wait until the connection is ready. If it is not, a ConnectionDead error will be raised
        :raise RuntimeError: called more than once
        :raise ConnectionDead: failed to connect within timeout
        """

        try:
            self.listener
        except AttributeError:
            pass
        else:
            raise RuntimeError(u'This was already called!')

        self.listener = ListenerThread()

        self.attache_group = AttacheGroup()

        self.events = six.moves.queue.Queue()  # for coolamqp.clustering.events.*

        self.snr = SingleNodeReconnector(self.node, self.attache_group,
                                         self.listener)
        self.snr.on_fail.add(lambda: self.events.put_nowait(ConnectionLost()))
        if self.on_fail is not None:
            self.snr.on_fail.add(self.on_fail)

        # Spawn a transactional publisher and a noack publisher
        self.pub_tr = Publisher(Publisher.MODE_CNPUB)
        self.pub_na = Publisher(Publisher.MODE_NOACK)
        self.decl = Declarer()

        self.attache_group.add(self.pub_tr)
        self.attache_group.add(self.pub_na)
        self.attache_group.add(self.decl)

        self.listener.init()
        self.listener.start()
        self.snr.connect(timeout=timeout)

        # todo not really elegant
        if wait:
            start_at = monotonic.monotonic()
            while not self.snr.is_connected() and monotonic.monotonic() - start_at < timeout:
                time.sleep(0.1)
            if not self.snr.is_connected():
                raise ConnectionDead('Could not connect within %s seconds' % (timeout, ))

    def shutdown(self, wait=True):
        """
        Terminate all connections, release resources - finish the job.
        :param wait: block until this is done
        :raise RuntimeError: if called without start() being called first
        """

        try:
            self.listener
        except AttributeError:
            raise RuntimeError(u'shutdown without start')

        logger.info('Commencing shutdown')

        self.listener.terminate()
        if wait:
            self.listener.join()
