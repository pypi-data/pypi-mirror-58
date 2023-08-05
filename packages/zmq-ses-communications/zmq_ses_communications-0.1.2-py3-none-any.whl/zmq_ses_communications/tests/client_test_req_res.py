#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from zmq_ses_communications import SES_Device
import time
import datetime as dt
from zmq_ses_communications.client.msgs.heartbeat_pb2 import HeartBeat
import asyncio
import random


class Test_Device(SES_Device):
    def __init__(self, host, port, device_identity):
        SES_Device.__init__(self, host, port, device_identity)
        self.start_time = dt.datetime.today().timestamp()
        self.i = 0
        self.j = 0
        self.k = 0

    def on_request_received(self, source, request):
        self.device_logger.info(f"request reveived from {request}")
        time_diff = dt.datetime.today().timestamp() - self.start_time
        self.i += 1
        print("ITPS", self.i / time_diff)

    def on_HeartBeat_received(self, message):
        self.device_logger.debug(f"{self.device_identity} received {message}")
        time_diff = dt.datetime.today().timestamp() - self.start_time
        self.j += 1
        print("ITPS HB", self.j / time_diff)

    def on_message_received(self, message):
        self.device_logger.debug(f"{self.device_identity} received {message}")

    def get_hb_msg(self):
        msg = HeartBeat()
        msg.device_name = "test_device"
        msg.device_id = 1
        msg.device_lifetime = 1
        return msg.SerializeToString()

    async def publish_heartbeat(self):
        while True:
            await asyncio.sleep(1)
            await self.send_proto_message("HEARTBEAT", self.get_hb_msg())
            self.pubsub_logger.debug("publishing heartbeat")

    async def publish_test(self):
        while True:
            await asyncio.sleep(1)
            await self.send_message("test", "this is test")
            self.pubsub_logger.debug("publishing test msg")

    def setup_publishing(self):
        future = asyncio.run_coroutine_threadsafe(
            self.publish_heartbeat(), self.pub_loop
        )
        future = asyncio.run_coroutine_threadsafe(self.publish_test(), self.pub_loop)
        # self.add_publisher()
        # self.add_publisher(self.publish_test)


if __name__ == "__main__":

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(name)s %(threadName)s %(asctime)s [%(levelname)s] : %(message)s",
    )


    dev = Test_Device("134.103.112.185", 6000, "E")
    dev.setup_publishing()
    dev2 = Test_Device("134.103.112.185", 6000, "F")
    dev2.setup_publishing()


    while True:
        dev.send_request("F", f"REQUEST {random.randint(0,10000)} from E")
        dev2.send_request("E", "REQUEST from F")
        time.sleep(1)

