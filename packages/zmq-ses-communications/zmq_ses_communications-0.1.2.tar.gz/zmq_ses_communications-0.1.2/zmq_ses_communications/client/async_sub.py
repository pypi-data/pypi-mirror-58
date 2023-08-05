#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import time
import zmq
import zmq.asyncio
from zmq.asyncio import Context
import os
import psutil
from threading import Thread
import logging


class Subscriber(Thread):
    def __init__(self, host, port):
        self.subscriber_logger = logging.getLogger("Subscriber")
        Thread.__init__(self)
        self.subscriber_url = f"tcp://{host}:{port}"
        self.subscriber_logger.info(f"Subscriber connecting to {self.subscriber_url}")
        self.subscriber_ctx = Context.instance()
        self.process = psutil.Process(os.getpid())
        self.sub_loop = asyncio.new_event_loop()
        self.subscribed_messages = []

    def setup_subscriptions(self, subscriptions):
        self.subsciptions = subscriptions
        self.subscriber = self.subscriber_ctx.socket(zmq.SUB)
        self.subscriber.connect(self.subscriber_url)
        for prefix in subscriptions:
            self.add_subscription(prefix)

    def add_subscription(self, message_name):
        self.subscriber.setsockopt(zmq.SUBSCRIBE, message_name.encode())
        self.subscriber_logger.info(f"Setting subscription for msg : {message_name}")
        self.subscribed_messages.append(message_name)

    def remove_subscription(self, message_name):
        self.subscriber.setsockopt(zmq.UNSUBSCRIBE, message_name.encode())
        self.subscriber_logger.info(f"removing subscription for msg : {message_name}")

    async def subscriber_loop(self, subsciptions):

        self.setup_subscriptions(subsciptions)

        while True:
            # print("receiving msg")
            await asyncio.sleep(0.001)
            await self.receive_message()

    async def receive_message(self):
        topic, contents = await self.subscriber.recv_multipart()

        # future.add_done_callback(self.callback_msg_rcvd)
        #
        self.subscriber_logger.debug(
            f"Received topic : {topic} PUB,  contents : {contents}"
        )
        self.callback_msg_rcvd(topic, contents)

    def callback_msg_rcvd(self, topic, contents):
        pass

    # async def do_something(self):
    #     while True:
    #         await asyncio.sleep(0.0)
    #         #
    #         # print("Doing house keeping")

    def run_sub(self, prefix):
        asyncio.set_event_loop(self.sub_loop)
        self.sub_loop.create_task(self.subscriber_loop(prefix))
        self.sub_loop.run_forever()

    def stop_sub_loop(self):
        self.subscriber.disconnect(self.subscriber_url)
        self.sub_loop.stop()
        while self.sub_loop.is_running():
            self.subscriber_logger.info(f"Still running")
        self.subscriber_logger.info(f"Closed the sub")


if __name__ == "__main__":
    s = Subscriber("127.0.0.1", 6001)
    asyncio.run(s.subscriber_loop())
