"""
Software designed for parsing, mailing of letters for resource https://powertofly.com/
"""
import time
from logsource.logmodule import LogModule
from core.redissub import RedisSub
from core.redispub import RedisPub
from core.parser import Parser
from core.sender import Sender


class PowertoflyWorker(LogModule):
    def __init__(self):
        super().__init__()
        # a flag that determines the state of the bot running shutdown
        self.execution_status = True
        # Incoming message store
        self.task_data = dict()
        # Outgoing message store
        self.send_data = dict()
        self.redis_subscriber = RedisSub()
        self.redis_publisher = RedisPub()
        self.parser = Parser()
        self.sender = Sender()

    def start(self):
        print("Start work")
        self.set_task_data(self.redis_subscriber)
        while self.execution_status:
            # check tasks
            if self.task_data:
                print(self.task_data)
            time.sleep(2)

    def set_task_data(self, sub: RedisSub):
        """
        Initializes a task by receiving a message from the main system
        :param sub: RedisSub object
        :return: None
        """
        e = sub.subscribes.get_message()
        if e:
            if type(e["data"]) != int:
                self.task_data["task"] = e["data"].decode()


if __name__ == "__main__":
    power = PowertoflyWorker()
    power.start()
