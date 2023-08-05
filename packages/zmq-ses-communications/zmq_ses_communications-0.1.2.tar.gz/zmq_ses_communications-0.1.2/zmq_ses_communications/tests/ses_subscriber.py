#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq
import time

from ses_helpers import Message


class Subscriber:
    def __init__(self, host, port):
        self.context = zmq.Context()
        self.subscriber = self.context.socket(zmq.SUB)
        self.connect_node(host, port)

    def connect_node(self, host, port):

        self.subscriber.connect(f"tcp://{host}:{port}")  # localhost:5563

    def subscribe_topic(self, topic_name):

        self.subscriber.setsockopt(zmq.SUBSCRIBE, topic_name.encode())

    def receive_message(self):
        try:
            [address, contents] = self.subscriber.recv_multipart(zmq.NOBLOCK)
            return Message(address.decode(), contents.decode())
        except Exception as e:
            return False

    def start_reception_loop(self):
        while True:
            message = self.receive_message()
            if message:
                print(message)

    def stop_subscription(self):
        self.subscriber.close()
        self.context.term()


if __name__ == "__main__":
    suber = Subscriber("127.0.0.1", 600)
    suber.subscribe_topic("ERROR")
    suber.start_reception_loop()
