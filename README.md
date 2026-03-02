# QuantumEdgeArb: Bayesian Pairs Trading Proof‑of‑Concept

A **production‑grade pairs trading engine** demonstrating modern AWS
and NVIDIA skills.  It combines Bayesian cointegration, NeMo NIMs,
TensorRT‑LLM optimisation, and a cloud‑native, agent‑driven architecture
—all built on a student‑friendly, low‑cost stack.


## Overview
This repository is a proof‑of‑concept for a high‑frequency arbitrage
strategy using Kalman‑filter cointegration.  The system includes data
ingestion (Kafka/MSK), signal generation (Kalman + NIM regime
classifier), execution with risk guardrails, and cloud orchestration via
Step Functions.  It is designed to showcase:

* **AWS proficiency**: SageMaker endpoints, Terraform infrastructure,
  Step Functions, and cost management.
* **NVIDIA expertise**: NeMo agent toolkit, NIMs, TensorRT‑LLM tuning
  on G5 instances.
* **Software engineering**: hybrid C++/Python stack, automated tooling,
  and clear documentation.


## Install
```bash
git clone https://your.repo.url/QuantumEdgeArb.git
cd QuantumEdgeArb
# install either Python or npm helper
pip install gsd           # or `npx get-shit-done-cc@latest`

gsd deps                  # build dependencies and Python packages
```


## Usage
Run the built-in tasks to exercise various components:

```bash
gsd data:fetch            # download or stream sample market data
gsd ml:train              # train the Kalman/co-integr model (stub)
gsd ml:test               # run unit tests for ml_model
gsd exec:test             # run execution engine unit tests
gsd nvidia:benchmark      # convert NIM to TensorRT and measure latency
gsd infra:apply           # terraform apply (MSK, SageMaker, StepFunctions)
``` 

Open the folder in VS Code to auto-trigger the `gsd context` task and
use keybindings (Ctrl+Alt+B/T/C) for build/test/context.


## Project Structure
```bash
quantum-edge-arb/
├── data_ingestion/     # Kafka producers, tick fetchers
│   ├── binance/        # exchange adapters (empty stubs)
│   └── coinbase/
├── ml_model/           # cointegration, NIM classifier, training
│   ├── train.py
│   ├── cointegration.py
│   └── nemo_classifier.py
├── execution_engine/   # order router, risk logic (C++/Python)
│   ├── src/            # Boost.Asio networking (stubs)
│   └── tests/          # GoogleTest benchmarks
├── infra/              # Terraform/IaC for AWS services
├── benchmarks/         # VectorBT notebooks and backtests
└── docs/               # Architecture diagrams, whitepaper, cost
```


## Demonstrates
* AWS SageMaker model endpoints
* Terraform infrastructure (MSK, Step Functions)
* NVIDIA NIM/NeMo agent and TensorRT‑LLM optimization
* Agentic risk guardrails with Kill Switch
* Cost‑aware, free‑tier deployment suitable for students


## Development Environment & Vibe‑Coding
This repo is editor‑agnostic and works with Gemini CLI, VS Code, Vim, or
any terminal.  See the **Development Environment** section below for
setup instructions and workflow.


## Cost
See [`docs/COST.md`](docs/COST.md) for a breakdown of expected
expenses when using AWS free‑tier and spot GPU credits.


## Contributing
See [`docs/SETUP.md`](docs/SETUP.md) for detailed setup steps and
contribution guidelines.


## License
MIT
