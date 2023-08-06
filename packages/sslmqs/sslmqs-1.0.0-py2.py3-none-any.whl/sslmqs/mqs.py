import datetime
import exceptions
import json
import logging
import pika
import random
import ssl
import time


log = logging.getLogger(__name__)


class Mqs():
    def __init__(self, timeout, config, exchange, exchange_type):
        """
        :param timeout: The socket-level timeout. The value should be high
            enough, otherwise the connection would time out not because of a
            specific issue, but just because there was no heartbeat during the
            interval. A value of ten seconds seems like a good starting point.

        :param config: The configuration of the message queue service. The
            object should contain the following properties: `mqs_vhost`,
            `mqs_port`, `tls_ca`, `tls_cert`, and `tls_key`.

        :param exchange: The name of the exchange.

        :param exchange_type: The type of the exchange.
        """
        self._timeout = timeout
        self._exchange = exchange
        self._exchange_type = exchange_type
        self._config = config

    def _connect_to_instance(self, instance):
        parameters = self._generate_instance_params(instance)

        try:
            connection = pika.BlockingConnection(parameters)
        except Exception as e:
            raise exceptions.ConnectionRefused() from e

        channel = connection.channel()
        channel.exchange_declare(
            exchange=self._exchange, exchange_type=self._exchange_type)
        log.info("Connected to %s.", instance)

        # A hack to reduce downtime when RabbitMQ instance goes down.
        # See https://groups.google.com/forum/#!topic/pika-python/2Ht06Kjrp9s
        # See https://blog.pelicandd.com/article/151/
        connection._impl._heartbeat_checker._check_interval = 1
        return (connection, channel)

    def _generate_instance_params(self, instance):
        context = ssl.create_default_context(cafile=self._config.tls_ca)
        context.load_cert_chain(self._config.tls_cert, self._config.tls_key)
        ssl_options = pika.SSLOptions(context, instance)

        return pika.ConnectionParameters(
            host=instance,
            port=self._config.mqs_port,
            virtual_host=self._config.mqs_vhost,
            ssl_options=ssl_options,
            credentials=pika.credentials.ExternalCredentials(),
            heartbeat=1,
            socket_timeout=self._timeout,
            stack_timeout=self._timeout,
            blocked_connection_timeout=1,
            connection_attempts=1,
            retry_delay=0)
