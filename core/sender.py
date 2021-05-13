"""
Sending letters to the target resource
"""
from logsource.logmodule import LogModule


class Sender(LogModule):

    def __init__(self):
        super().__init__()

    def start(self, send_data):
        pass
