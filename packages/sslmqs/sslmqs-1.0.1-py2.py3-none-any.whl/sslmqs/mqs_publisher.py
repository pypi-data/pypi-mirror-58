import datetime
import exceptions
import json
import logging
import pika
import random
import ssl
import time

from .mqs import Mqs


log = logging.getLogger(__name__)


class MqsPublisher(Mqs):
    def __init__(self, config, exchange, exchange_type, timeout=60):
        """
        :param config: The configuration of the message queue service. The
            object should contain the following properties: `mqs_vhost`,
            `mqs_port`, `tls_ca`, `tls_cert`, and `tls_key`.

        :param exchange: The name of the exchange.

        :param exchange_type: The type of the exchange.

        :param timeout: The socket-level timeout. The value should be high
            enough, otherwise the connection would time out not because of a
            specific issue, but just because there was no heartbeat during the
            interval. A value of ten seconds seems like a good starting point.
        """
        super().__init__(timeout, config, exchange, exchange_type)
        self._connection = None

    def send(self, routing_key, body):
        connection, channel = self._connect()
        try:
            result = channel.basic_publish(
                exchange=self._exchange, routing_key=routing_key, body=body)
        except:
            log.info("Existing connection is closed. Reconnecting.")
            connection, channel = self._reconnect()
            result = channel.basic_publish(
                exchange=self._exchange, routing_key=routing_key, body=body)

        log.info("Result: %s for message %s.", result, body)

    def _reconnect(self):
        self._connection = None
        self._channel = None
        return self._connect()

    def _connect(self):
        if self._connection:
            log.info("Reusing existing connection to %s.", self._instance)
            return self._connection, self._channel

        instances = self._config.mqs_hosts
        random.shuffle(instances)

        for instance in instances:
            try:
                log.debug("Connecting to %s.", instance)
                connection, channel = self._connect_to_instance(instance)
                channel.confirm_delivery()
                self._instance = instance
                self._connection = connection
                self._channel = channel
                return connection, channel
            except:
                log.info("Failed to connect to %s.", instance)

        log.warn("No more instances left.")
        raise exceptions.ClusterUnavailable()
