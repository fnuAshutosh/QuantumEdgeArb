import os
import json

try:
    from kafka import KafkaProducer as KP
except ImportError:
    KP = None


class KafkaProducer:
    def __init__(self, bootstrap_servers=None, **kwargs):
        self.bootstrap_servers = bootstrap_servers or os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        if not self.bootstrap_servers:
            raise ValueError("No bootstrap servers provided for KafkaProducer")
        if KP is None:
            raise ImportError("kafka-python library is required")
        # kafka-python producer serialises bytes; we encode JSON strings
        self._producer = KP(bootstrap_servers=self.bootstrap_servers.split(','),
                            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                            **kwargs)

    def send_tick(self, topic: str, tick: dict):
        if not topic:
            raise ValueError("Topic name required")
        future = self._producer.send(topic, tick)
        # optionally block for result
        try:
            future.get(timeout=5)
        except Exception as e:
            # log or rethrow
            raise

    def close(self):
        if self._producer:
            self._producer.flush()
            self._producer.close()


# basic sanity check when module run directly
if __name__ == "__main__":
    print("KafkaProducer module loaded")
    try:
        kp = KafkaProducer(bootstrap_servers="localhost:9092")
        print(kp)
    except Exception as e:
        print("could not instantiate producer", e)
