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
        self.redis_subscriber = RedisSub(self.task_data)
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
                # determine what type of task is set to work
                if self.task_data["task"]["cmd"] == "start_parser":
                    parser_result = self.parser.start(self.send_data)
                else:
                    sender_result = self.sender.start(self.send_data)
                    print("Start sender")
                #
            else:
                print("No data")
            time.sleep(2)

    def set_task_data(self, sub: RedisSub):
        """
        Initializes a task by receiving a message from the main system
        Provides a persistent connection to the system server
        :param sub: RedisSub object
        :return: None
        """
        sub.subscribes.get_message()


if __name__ == "__main__":
    power = PowertoflyWorker()
    power.start()
