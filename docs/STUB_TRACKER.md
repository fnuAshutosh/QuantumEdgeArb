# Stub Tracker

Use this file to track which source files are incomplete (stubs or empty).
Maintainers should update the legend as progress is made.

| File | Status | Notes |
|------|--------|-------|
| data_ingestion/kafka_producer.py | 🟡 STUB | needs real KafkaProducer class |
| data_ingestion/coinbase/ws_client.py | 🔴 EMPTY | WebSocket client skeleton |
| data_ingestion/binance/cpp_client/maine.cpp | 🔴 EMPTY | C++ WS client stub |
| ml_model/nemo_classifier.py | 🟡 STUB | currently hardcoded threshold |
| ml_model/deploy/api_server.py | 🟡 STUB | FastAPI endpoints stub |
| ml_model/src/model.py | 🔴 EMPTY | placeholder for later ML model |
| ml_model/src/preprocess.py | 🔴 EMPTY | compute rolling zscore |
| ml_model/src/train.py | 🟡 STUB | dummy training script |
| execution_engine/include/order.h | 🔴 EMPTY | to be defined |
| execution_engine/include/risk.h | 🔴 EMPTY |
| execution_engine/src/order_router.cpp | 🔴 EMPTY |
| execution_engine/src/risk_engine.cpp | 🔴 EMPTY |
| execution_engine/tests/test_order_router.cpp | 🔴 EMPTY | GoogleTest placeholder |
| benchmarks/backtests/pairs.ipynb | 🔴 EMPTY |
| benchmarks/backtests/vectorbt_notebook.ipynb | 🔴 EMPTY |
| docs/WHITEPAPER.md | 🟡 UPDATED | now contains math |

(Update this table as you implement each stub.)