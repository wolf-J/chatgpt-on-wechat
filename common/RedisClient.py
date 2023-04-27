import redis

from common.singleton import singleton
from config import conf


@singleton
class RedisClient(object):

    def __init__(self):
        self.pool = redis.ConnectionPool(host=conf().get("redis_host"), port=conf().get("redis_port"),
                                         password=conf().get("redis_password"))

    @property
    def conn(self):
        if not hasattr(self, '_conn'):
            self.getConnection()
        return self._conn

    def getConnection(self):
        self._conn = redis.Redis(connection_pool=self.pool)


redisClient = RedisClient()

pre_fix_key = "hades:logistics:"
