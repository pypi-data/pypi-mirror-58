import asyncio
import zmq
import os
import sys
import time
from threading import Thread
import logging
from .request import Requester
from .reply import Responder


class ReqResNode(Requester, Responder):
    def __init__(self, host, port, identitiy):
        self.reqres_logger = logging.getLogger("ReqResNode")
        Requester.__init__(self, host, port, identitiy)  # "127.0.0.1", 5559
        Responder.__init__(self, host, port + 1, identitiy)  #  "127.0.0.1", 5560
        reponder_thread = Thread(target=self.run_reply_loop)
        reponder_thread.start()
        self.reqres_logger.info("Request Responder initiated")
        time.sleep(0.5)

    def stop_req_res(self):
        self.stop_reply_loop()
        self.stop_requester()


if __name__ == "__main__":
    name = "node"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    for i in range(60):
        N = Node(f"{name}{i}")
        N.send_request(f"{name}{i}", "hello")
