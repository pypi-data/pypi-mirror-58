class Disconnected(Exception):
    """
    An exception raised when the connection was dropped, for instance because
    the RabbitMQ instance was shut down or because there was an issue with the
    network.
    """
    pass


class ConnectionRefused(Exception):
    """
    An exception raised when the initial connection to RabbitMQ didn't succeed.
    """
    pass


class ClusterUnavailable(Exception):
    """
    An exception raised when every instance of the RabbitMQ cluster was tried,
    and none replied. This is likely to indicate that the whole cluster is
    down.
    """
    pass
