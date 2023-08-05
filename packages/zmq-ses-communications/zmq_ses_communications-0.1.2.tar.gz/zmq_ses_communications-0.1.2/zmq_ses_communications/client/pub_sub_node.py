#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import logging
from threading import Thread

from .async_pub import Publisher
from .async_sub import Subscriber


class PubSubNode(Publisher, Subscriber):
    def __init__(self, host, port):
        self.pubsub_logger = logging.getLogger("PubSubNode")
        Publisher.__init__(self, host, port)
        Subscriber.__init__(self, host, port + 1)
        pub = Thread(target=self.run_pub)
        subs = ["test", "HEARTBEAT"]
        sub = Thread(target=self.run_sub, args=(subs,))
        pub.start()
        sub.start()
        self.pubsub_logger.info("Started Publisher and subscriber threads")
        # pub.join()
        # self.pubsub_logger.info("Joined Pub")
        # sub.join()
        # self.pubsub_logger.info("Joined Sub")

    def stop_pub_sub(self):
        self.stop_pub_loop()
        self.stop_sub_loop()


if __name__ == "__main__":
    N1 = PubSubNode("127.0.0.1", 6000)
    print("this will not print")
    N1.create_publisher()
