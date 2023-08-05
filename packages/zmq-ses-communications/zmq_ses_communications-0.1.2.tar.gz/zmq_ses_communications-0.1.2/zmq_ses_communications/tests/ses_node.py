#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
from uuid import uuid1, getnode

from ses_publisher import Publisher
from ses_subscriber import Subscriber


# Publisher publishes topics
# Subscriber connects to publiser and receives messages


class Node:
    def __init__(self, nodename):

        self.pub = Publisher("127.0.0.1", 6000)
        self.sub = Subscriber("127.0.0.1", 6001)
        self.heartbeat = {"device_name": nodename, "device_id": uuid1(getnode())}
        self.sub.subscribe_topic("HEARTBEAT")
        self.sub.start_reception_loop()

    def start_publishing(self):
        self.pub.send_dict_message("HEARTBEAT", self.heartbeat)

    def start_loop(self):
        while True:
            self.start_publishing()
            time.sleep(1.1)


if __name__ == "__main__":

    _node1 = Node("A")
    _node1.start_loop()
