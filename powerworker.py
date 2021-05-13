"""
Software designed for parsing, mailing of letters for resource https://powertofly.com/
"""
import time
from logsource.logmodule import LogModule
from core.redissub import RedisSub
from core.redispub import RedisPub


class PowertoflyWorker(LogModule):
    def __init__(self):
        super().__init__()
        self.execution_status = True
        self.task_data = dict()
        self.send_data = dict()
        self.redis_subscriber = RedisSub()
        self.redis_publisher = RedisPub()

    def start(self):
        print("Start work")
        while self.execution_status:
            time.sleep(2)
            e = self.redis_subscriber.subscribes.get_message()
            if e:
                if type(e["data"]) != int:
                    print(e["data"].decode())

            time.sleep(2)


if __name__ == "__main__":
    power = PowertoflyWorker()
    power.start()