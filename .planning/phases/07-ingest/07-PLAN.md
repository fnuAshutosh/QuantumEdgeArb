---
phase: 07-ingest
plan: 01
type: execute
wave: 1
depends_on:
  - 06-restructure
files_modified:
  - data_ingestion/kafka_producer.py
  - data_ingestion/fetch_data.py
  - data_ingestion/coinbase/ws_client.py
  - data_ingestion/binance/cpp_client/maine.cpp
requirements: [REQ-??]

must_haves:
  truths:
    - "KafkaProducer can send a tick dict to a bootstrap server"
    - "fetch_data can download real CSV or stream to Kafka"
  artifacts:
    - path: "data_ingestion/kafka_producer.py"
      provides: "Kafka producer class"
  key_links: []
---

<objective>
Create working data ingestion code: a Python KafkaProducer wrapper, a
Python fetcher that writes ticks, and stubs/placeholders for exchange
clients.
</objective>

<tasks>

<task type="auto">
  <name>Implement KafkaProducer wrapper in Python</name>
  <files>data_ingestion/kafka_producer.py</files>
  <action>
    Use `confluent-kafka` or `kafka-python` to implement a class with
    `send_tick(topic, tick_dict)` and `close()`; read bootstrap servers from
    env var `KAFKA_BOOTSTRAP_SERVERS`.
  </action>
  <verify>
    <automated>python - <<'PY'
from data_ingestion.kafka_producer import KafkaProducer
kp = KafkaProducer()
print(kp)
PY</automated>
  </verify>
  <done>Class exists and can be instantiated without error.</done>
</task>

<task type="auto">
  <name>Enhance fetch_data script</name>
  <files>data_ingestion/fetch_data.py</files>
  <action>
    Add flags `--to-kafka` and `--source` to either download CSV or produce
    ticks to Kafka topic using KafkaProducer.
  </action>
  <verify>
    <automated>python data_ingestion/fetch_data.py --help || true</automated>
  </verify>
  <done>Script accepts new options and imports KafkaProducer.</done>
</task>

<task type="auto">
  <name>Socket client placeholders</name>
  <files>data_ingestion/coinbase/ws_client.py, data_ingestion/binance/cpp_client/maine.cpp</files>
  <action>
    Fill in minimal class definitions for `CoinbaseWS` and `BinanceWS` that
    log received messages; real implementation will come later.
  </action>
  <verify>
    <automated>grep -n "class Coinbase" data_ingestion/coinbase/ws_client.py || true
    grep -n "main" data_ingestion/binance/cpp_client/maine.cpp || true</automated>
  </verify>
  <done>Files contain stub classes/functions.</done>
</task>

</tasks>

<verification>
Attempt to run `python data_ingestion/fetch_data.py --to-kafka` (Kafka may
not be running, but import should succeed).  Confirm KafkaProducer class can be
instantiated with no exceptions.
</verification>

<success_criteria>
Data ingestion module compiles/executes without errors; realistic functionality
is scaffolded and documented.
</success_criteria>

<output>
Create `.planning/phases/07-ingest/07-PLAN-SUMMARY.md` after tasks finish.
</output>
