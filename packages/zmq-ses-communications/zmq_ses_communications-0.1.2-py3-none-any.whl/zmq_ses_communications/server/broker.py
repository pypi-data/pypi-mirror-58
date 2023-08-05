#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
from .pub_sub_router import PubSubRouter
from .req_res_router import ReqRepRouter


class Broker(PubSubRouter, ReqRepRouter):
    def __init__(self, host, port):
        PubSubRouter.__init__(self, host, port)
        ReqRepRouter.__init__(self, host, port + 2)
        self.pub_sub_thread = Thread(target=self.start_publish_subscribe_routing)
        self.req_res_thread = Thread(target=self.start_request_reply_routing)
        self.pub_sub_thread.start()
        self.req_res_thread.start()

    def dispose(self):

        self.dispose_pub_sub()
        self.req_res_stopped = True


if __name__ == "__main__":
    print("IIIIIIIIIII")
    broker = Broker("127.0.0.1", 6000)

