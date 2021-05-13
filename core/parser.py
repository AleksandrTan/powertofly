"""
Parsing the target resource
"""
from logsource.logmodule import LogModule
from core.request_worker import RequestsWorker
from supporting.analyzer import Analyzer


class Parser(LogModule):

    def __init__(self):
        super().__init__()
        # a flag that determines the state of the bot running shutdown
        self.execution_status = True
        self.requests = RequestsWorker()
        self.analyzer = Analyzer()

    def start(self, send_data):
        print("Parser Work")
        return True
