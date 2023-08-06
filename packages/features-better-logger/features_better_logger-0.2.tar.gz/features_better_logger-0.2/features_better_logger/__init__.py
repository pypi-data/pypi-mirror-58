import json
import logging
import queue
import time
from logging.handlers import HTTPHandler, QueueHandler, QueueListener
import requests


logger = logging.getLogger(__name__)

service_name = "Default (please change)"


def init(_service_name, logger_url):
    global service_name
    service_name = _service_name

    return BetterLogger(logger_url)


class BetterHTTPHandler(HTTPHandler):

    default_time_format = "%Y-%m-%dT%H:%M:%S"
    default_msec_format = "%s,%03d"

    def emit(self, record):
        message = self.mapLogRecord(record)

        log_message = {
            "service_name": service_name,
            "message": message["msg"],
            "timestamp": self.format_time(message["created"], message["msecs"]),
            "level": message["levelname"],
        }

        requests.post(self.host + self.url, json=json.dumps(log_message))

    def format_time(self, created, msecs):
        ct = time.localtime(created)
        t = time.strftime(self.default_time_format, ct)
        s = self.default_msec_format % (t, msecs)
        return s


class BetterLogger:
    def __init__(self, logger_url):
        """
        example: BetterLogger("http://localhost:8002")
        """
        que = queue.Queue(-1)  # no limit on size

        queue_handler = QueueHandler(que)

        handler = BetterHTTPHandler(logger_url, "/logs")
        listener = QueueListener(que, handler)

        root = logging.getLogger()
        root.addHandler(queue_handler)

        listener.start()
