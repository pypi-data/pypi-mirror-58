#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import zmq
import zmq.asyncio
from zmq.asyncio import Context
import os
import time
import sys
import random
from threading import Thread, get_ident
import logging


class Responder(Thread):
    def __init__(self, host, port, identitiy):
        Thread.__init__(self)
        self.responder_url = f"tcp://{host}:{port}"
        self.responder_ctx = Context.instance()
        self.responder_identitiy = identitiy
        self.responder_logger = logging.getLogger("Responder")
        self.responder_loop = asyncio.new_event_loop()

    async def announce_service(self):
        self.responder_socket = self.responder_ctx.socket(zmq.DEALER)
        self.responder_socket.setsockopt(
            zmq.IDENTITY, self.responder_identitiy.encode("utf-8")
        )
        self.responder_logger.info(f"Responder connecting to {self.responder_url}")
        self.responder_socket.connect(self.responder_url)  # "tcp://127.0.0.1:5560"
        self.responder_logger.info(f"Announcing presence to {self.responder_url}")
        await self.responder_socket.send(b"READY")

    async def response_loop(self):
        await self.announce_service()
        while True:
            # source, service, request = self.responder_socket.recv_multipart()
            await asyncio.sleep(0.001)
            request, source = await self.responder_socket.recv_multipart()

            self.responder_logger.debug(
                f"got request : {request} from : {source} for service : {self.responder_identitiy} threadid : {get_ident()}"
            )
            self.on_request_received(source, request)

            await self.responder_socket.send_multipart([source, b"OK"])

    def run_reply_loop(self):
        asyncio.set_event_loop(self.responder_loop)
        self.responder_loop.create_task(self.response_loop())
        self.responder_loop.run_forever()
        # asyncio.run(self.response_loop())

    def stop_reply_loop(self):
        self.responder_socket.disconnect(self.responder_url)
        self.responder_loop.stop()
        while self.responder_loop.is_running():
            self.responder_logger.debug(f"Still running")
        self.responder_logger.info(f"Closed the sub")


if __name__ == "__main__":
    name = "s1"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    R = Responder("127.0.0.1", 5560, name)
    asyncio.run(R.response_loop())
