from urllib.parse import urlsplit
from redis import Redis
from . import version as _version


def version() -> str:
    return f"{_version.major}.{_version.minor}.{_version.patch}"


def get_redis_client(url: str) -> Redis:
    """
    Parse given URL, and instantiate a Redis client.

    :param url: Redis URL in the form redis://[user]:[token]@<host>[:port]/<database>
    :return: An instance of the Redis class.
    """
    if url == "test":
        from fakeredis import FakeRedis
        redis_client = FakeRedis()
    else:
        url_parts = urlsplit(url)
        port_number = 6379 if url_parts.port is None else url_parts.port
        db_number = int(url_parts.path.split("/")[1])
        ssl_enabled = True if url_parts.scheme == "rediss" else False
        redis_client = Redis(host=url_parts.hostname, port=port_number,
                             db=db_number, max_connections=3, retry_on_timeout=True,
                             socket_connect_timeout=60, socket_keepalive=True,
                             ssl=ssl_enabled, password=url_parts.password)
    return redis_client


def out(*args, out_file=None):
    if out_file:
        for arg in args:
            out_file.write(arg)
        out_file.write("\n")
    else:
        print(*args)
