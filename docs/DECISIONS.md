# Architecture Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Order routing language | C++ | Sub-millisecond latency requirement for HFT path |
| Risk engine language | Python (+ C++ mirror) | Rapid iteration; kill switch must be readable |
| ML framework | statsmodels (OLS) + numpy | OLS cointegration is simpler and more interpretable for POC than full state-space Kalman |
| Regime classifier | NVIDIA NIM | Showcases NVIDIA GPU / NeMo ecosystem; NIM is a drop-in hosted endpoint |
| Message bus | Kafka (MSK) | Decoupling, replay capability, fan-out to multiple consumers |
| Orchestrator | AWS Step Functions | Native AWS, serverless, visual state machine, no infra to manage |
| Infra-as-code | Terraform | Industry standard; reproducible teardown avoids runaway costs |
| Test framework (Python) | unittest | No extra dependency; built-in; sufficient for POC |
| Test framework (C++) | GoogleTest | Industry standard; integrates with CMake + CTest |
| Pairs choice (NVDA/TSM) | NVDA + TSM | High correlation semiconductor pair; liquid; publicly available data |
