import datetime
import json
import logging
import pika
import random
import ssl
import time

from .mqs import Mqs
from .exceptions import Disconnected, ConnectionRefused, ClusterUnavailable


log = logging.getLogger(__name__)


class MqsSubscriber(Mqs):
    def __init__(self, config, exchange, exchange_type):
        """
        :param config: The configuration of the message queue service. The
            object should contain the following properties: `mqs_vhost`,
            `mqs_port`, `tls_ca`, `tls_cert`, and `tls_key`.

        :param exchange: The name of the exchange.

        :param exchange_type: The type of the exchange.
        """
        timeout = 1
        super().__init__(timeout, config, exchange, exchange_type)

    def listen(
            self, queue_name, routing_key, on_message,
            is_json=True, ack=True, volatile=True):
        """
        :param queue_name: the name of the queue to listen.

        :param routing_key: the routing key of the queue, or None if no routing
            needs to be performed. Routing can be performed later by calling
            `add_routing`. In order to apply multiple routings, use an array of
            strings.

        :param on_message: the callback which would be called when a message is
            received.

        :param bool is_json: a value indicating whether the message is expected
            to be in JSON format and should be presented to the caller as an
            object. If false, no deserialization would be performed.

        :param bool ack: a value indicating whether the reception will be
            acknowledged.

        :param bool volatile: if true, message loss could occur in a case of an
            issue with the node of RabbitMQ cluster to which the subscriber is
            connected. If false, there would be no loss of messages (unless the
            whole cluster is down), but the queue would be persisted.
        """
        def _on_message(channel, method_frame, header_frame, body):
            if ack:
                channel.basic_ack(delivery_tag=method_frame.delivery_tag)

            plain_body = body.decode("utf-8")
            message = json.loads(plain_body) if is_json else plain_body
            on_message(message)

        self._listen_on_queue(queue_name, volatile, routing_key, _on_message)

    def add_routing(self, queue, routing_key):
        instances = self._config.mqs_hosts
        random.shuffle(instances)
        for instance in instances:
            try:
                connection, channel = self._connect_to_instance(host)
                self._add_routing(channel, queue, routing_key)
                return
            except:
                log.info("Failed to set routing key on %s", instance)

        log.error("No more instances left.")
        raise ClusterUnavailable()

    def _add_routing(self, channel, queue, routing_key):
        channel.queue_bind(
            exchange=self._exchange, queue=queue, routing_key=routing_key)

    def _listen_on_queue(
            self, queue_name, volatile, routing_key, on_message):
        instances = self._config.mqs_hosts
        random.shuffle(instances)
        blacklisted_instances = []

        while True:
            for instance in instances:
                if instance not in blacklisted_instances:
                    try:
                        self._listen_on_queue_using_instance(
                            instance, queue_name, volatile, routing_key,
                            on_message)
                    except KeyboardInterrupt:
                        return
                    except ConnectionRefused:
                        log.info("Failed to connect to %s.", instance)
                        blacklisted_instances.append(instance)
                    except Disconnected:
                        log.info("Was disconnected from %s.", instance)
                        blacklisted_instances = []

            if len(blacklisted_instances) == len(instances):
                break

        log.error("No more instances left.")
        raise ClusterUnavailable()

    def _listen_on_queue_using_instance(
            self, host, queue, volatile, routing_key, on_message):
        connection, channel = self._connect_to_instance(host)
        channel.queue_declare(
            queue=queue,
            auto_delete=volatile,
            durable=not volatile,
            arguments={"x-dead-letter-exchange": self._exchange})

        if routing_key:
            if isinstance(routing_key, str):
                routing_key = [routing_key]

            for x in routing_key:
                self._add_routing(channel, queue, x)

        channel.basic_consume(queue, on_message)

        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            raise
        except Exception as e:
            raise Disconnected() from e

        connection.close()
