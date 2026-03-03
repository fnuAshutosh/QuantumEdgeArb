# TODOs

This file collects actionable items to avoid forgetting details.  It mirrors
the Phase 07 plan in `.planning` and other outstanding work.

- [ ] Implement `data_ingestion/kafka_producer.py` with KafkaProducer class
- [ ] Enhance `data_ingestion/fetch_data.py` to support `--to-kafka` and real
      data sources
- [ ] Add environment variable docs for Kafka in `.env.example`
- [ ] Implement stub `CoinbaseWS` client in `data_ingestion/coinbase/ws_client.py`
- [ ] Implement C++ WebSocket skeleton in
      `data_ingestion/binance/cpp_client/maine.cpp`
- [ ] Write unit tests for KafkaProducer (can mock library)
- [ ] Ensure `gsd data:fetch` works locally (log or save to file if Kafka
      unavailable)
- [ ] Update `SETUP.md` and `STRATEGY.md` with ingestion notes once ready

(Tasks will be checked off as they complete.)