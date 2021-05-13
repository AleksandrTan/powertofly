"""
Subscriber to the distribution of tasks from the main system
Used Redis
Messages are received in a separate thread
"""
import redis
import config
import json


class RedisSub:

    def __init__(self, task_data):
        """
        :param task_data: dict
        """
        self.task_data = task_data
        self.redis_connector = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)
        self.subscribes = self.redis_connector.pubsub()
        self.subscribes.subscribe(**{"data-for-parser": self.handler})
        self.thread = self.subscribes.run_in_thread(sleep_time=0.001)

    def handler(self, message):
        if type(message["data"]) != int:
            self.task_data["task"] = json.loads(message["data"].decode())
