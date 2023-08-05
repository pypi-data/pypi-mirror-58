#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from zmq_ses_communications import SES_Device


class Test_Device(SES_Device):
    def __init__(self, host, port, device_identity):
        SES_Device.__init__(self,host, port, device_identity)

if __name__ == "__main__":


    logging.basicConfig(
        level=logging.DEBUG,
        format="%(name)s %(threadName)s %(asctime)s [%(levelname)s] : %(message)s",
    )

    dev = Test_Device("134.103.112.185", 6000, "E")
    dev.create_publisher()
    dev2 = Test_Device("134.103.112.185", 6000, "F")
    dev2.create_publisher()
    dev.send_request("A", "REQUEST from E")
    dev2.send_request("B", "REQUEST from F")

