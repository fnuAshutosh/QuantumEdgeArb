# Stub Tracker

Legend:
- ✅ REAL – working code in place
- 🟡 STUB – partial implementation present
- 🔴 EMPTY – file exists but contains no logic

Most core components now have real implementations or functioning stubs.
Backtesting notebooks and cloud infrastructure remain skeletal.

| Component | Status | Notes |
|-----------|--------|-------|
| ml_model/cointegration.py | ✅ REAL | full OLS + ADF logic implemented |
| ml_model/nemo_classifier.py | ✅ REAL | calls NVIDIA NIM via requests |
| ml_model/deploy/api_server.py | ✅ REAL | computes signal + regime |
| ml_model/src/preprocess.py | ✅ REAL | rolling z-score computed |
| ml_model/src/train.py | ✅ REAL | returns coefficients, reads sample data later |
| ml_model/tests | ✅ REAL | comprehensive pytest suite |
| execution_engine/include/*.h | ✅ REAL | structs and class defined |
| execution_engine/src/*.cpp | ✅ REAL | stub behaviors implemented |
| execution_engine/router.py | ✅ REAL | Python wrapper logs orders |
| execution_engine/risk.py | ✅ REAL | basic kill-switch logic |
| execution_engine/tests | ✅ REAL | python tests pass, C++ placeholder exists |
| infra/terraform | 🟡 STUB | provider skeleton present |
| infra/kubernetes | 🟡 STUB | basic YAML placeholders |
| benchmarks/backtests | 🔴 EMPTY | notebooks created but no code |

Remaining TODOs:
* Implement actual Kafka producer in `data_ingestion/`
* Fill backtest notebooks with logic
* Flesh out Terraform files with real resources

