#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from zmq_ses_communications import Broker
import logging

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(name)s %(threadName)s %(asctime)s [%(levelname)s] : %(message)s",
    )
    broker = Broker("127.0.0.1", 6000)

