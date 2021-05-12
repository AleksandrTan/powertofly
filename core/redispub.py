import redis
import time
import json

import config


class RedisPub:

    def __init__(self):
        self.redis_connector = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)

    @property
    def connector(self):
        return self.redis_connector

    def set_data(self, i):
        self.connector.publish("data-for-server", json.dumps({"status": True, "cmd": f"start_parser - {i}"}))

    def get_data(self):
        return self.connector.get("Alex")


if __name__ == "__main__":
    i = 0
    pub = RedisPub()
    while i < 10:
        pub.set_data(i)
        i += 1
        time.sleep(2)