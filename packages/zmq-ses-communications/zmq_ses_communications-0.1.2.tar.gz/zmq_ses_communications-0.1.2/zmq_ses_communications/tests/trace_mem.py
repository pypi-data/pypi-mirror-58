import tracemalloc
import logging
import time

tracemalloc.start()

from zmq_ses_communications import SES_Device

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s %(threadName)s %(asctime)s [%(levelname)s] : %(message)s",
)

dev = SES_Device("127.0.0.1", 6000, "A")
dev.create_publisher()
dev2 = SES_Device("127.0.0.1", 6000, "B")
dev2.create_publisher()
dev.send_request("B", "REQUEST from A")
dev2.send_request("A", "REQUEST from B")

while True:

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics("lineno")

    print("[ Top 10 ]")

    for stat in top_stats[:10]:
        print(stat)

    time.sleep(2)
