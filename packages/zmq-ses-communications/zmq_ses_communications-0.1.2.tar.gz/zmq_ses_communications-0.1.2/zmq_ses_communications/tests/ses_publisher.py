#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import zmq
import json


class Publisher:
    def __init__(self, host, port):
        self.context = zmq.Context()
        self.publisher = self.context.socket(zmq.PUB)
        self.publisher.connect(f"tcp://{host}:{port}")

    def send_dict_message(self, topic_name, dict_message):
        self.publisher.send_multipart(
            [str.encode(topic_name), str.encode(json.dumps(dict_message))])

    def stop_publishing(self):
        self.publisher.close()
        self.context.term()


if __name__ == "__main__":
    puber = Publisher("127.0.0.1", 6000)
    i = 1

    while True:
        # Write two messages, each with an envelope and content
        print("publishubg ", i)
        error = {"error_type": "warning",
                 "error_msg": f"crashed arm to side: {i}"}
        i += 1

        puber.send_dict_message("ERROR", error)
        time.sleep(0.1)
