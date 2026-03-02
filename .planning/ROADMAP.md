# Roadmap

### Phase 01: Bootstrap core pipeline
Goal: Get data ingestion and Kalman model working locally; establish basic
project structure and tooling.

Requirements: REQ-01

Plans:
- [ ] 01-bootstrap-01-PLAN.md — initial setup and skeleton tasks

### Phase 02: Signal Pipeline
Goal: Wire Kalman signal and regime classification into a cohesive pipeline.
Plans:
- [x] 02-signal-01-PLAN.md — implement NemoClassifier and API server

### Phase 03: Execution Engine
Goal: Complete C++ router and risk engine; consume signals to create orders.
Plans:
- [x] 03-execution-01-PLAN.md — order/router implementations and tests

### Phase 04: Backtesting
Goal: Backtest NVDA/TSM strategy using historical data and vectorbt.
Plans:
- [x] 04-backtest-01-PLAN.md — create notebooks and compute metrics

### Phase 05: Cloud Deployment
Goal: Deploy full system on AWS free-tier using Terraform.
Plans:
- [x] 05-cloud-01-PLAN.md — finalize infra config, ECR, SageMaker, StepFn

### Phase 06: Repository Restructure
Goal: Tear down existing directory tree and rebuild skeleton according to updated documentation in docs/. Plans:
- [ ] 06-restructure-01-PLAN.md � remove old directories and recreate new layout
