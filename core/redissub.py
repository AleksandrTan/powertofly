import redis
import time

import config


class RedisSub:

    def __init__(self):
        self.redis_connector = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)
        self.subscribes = self.redis_connector.pubsub()
        self.subscribes.subscribe("data-for-power-my")

    def get_data(self):
        return self.subscribes.get_message()


if __name__ == "__main__":
    pub = RedisSub()
    while True:
        e = pub.get_data()
        if e:
            if type(e["data"]) != int:
                print(e["data"].decode())
        time.sleep(2)
