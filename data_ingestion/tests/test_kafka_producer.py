import pytest
import os

from data_ingestion.kafka_producer import KafkaProducer

class DummyProducer:
    def __init__(self, **kwargs):
        pass
    def send(self, topic, value):
        class F:
            def get(self, timeout=None):
                return True
        return F()
    def flush(self):
        pass
    def close(self):
        pass


def test_missing_bootstrap():
    with pytest.raises(ValueError):
        KafkaProducer(bootstrap_servers="")


def test_import_error(monkeypatch):
    monkeypatch.setattr('data_ingestion.kafka_producer.KP', None)
    with pytest.raises(ImportError):
        KafkaProducer(bootstrap_servers="localhost:9092")


def test_send_tick(monkeypatch):
    monkeypatch.setattr('data_ingestion.kafka_producer.KP', DummyProducer)
    kp = KafkaProducer(bootstrap_servers="srv1:9092")
    kp.send_tick("ticks", {"symbol":"NVDA"})
    kp.close()
