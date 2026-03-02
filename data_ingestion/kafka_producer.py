"""Simple Kafka producer for tick data (stub)."""

from kafka import KafkaProducer
import json

class TickProducer:
    def __init__(self, bootstrap_servers='localhost:9092', topic='ticks'):
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                       value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        self.topic = topic

    def send_tick(self, tick):
        """Send a single tick (dict) to Kafka."""
        self.producer.send(self.topic, tick)
        self.producer.flush()


if __name__ == '__main__':
    # example usage, emits dummy ticks
    import time
    tp = TickProducer()
    for i in range(10):
        tp.send_tick({'price': 100 + i, 'volume': 1, 'timestamp': time.time()})
        time.sleep(0.1
)