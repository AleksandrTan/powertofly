"""
Parsing the target resource
"""
from core.request_worker import RequestsWorker
from logsource.logmodule import LogModule


class Parser(LogModule):

    def __init__(self):
        super().__init__()
        self.requests = RequestsWorker()

    def start(self, send_data):
        pass
