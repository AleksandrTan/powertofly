import redis
import time

import config


class RedisSub:

    def __init__(self):
        self.redis_connector = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)
        self.subscribes = self.redis_connector.pubsub()
        self.subscribes.subscribe(**{"data-for-power-my": self.handler})
        self.subscribes.run_in_thread(sleep_time=0.001)

    def handler(self, message):
        print(message)
        return message


if __name__ == "__main__":
    pub = RedisSub()
    while True:
        e = pub.subscribes.get_message()
        if e:
            if type(e["data"]) != int:
                print(e["data"].decode())
        time.sleep(2)
