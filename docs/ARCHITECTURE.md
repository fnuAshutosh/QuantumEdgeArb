# Architecture

The system is composed of four primary layers:

1. **Data Ingestion** – Kafka/MSK topics receive 100ms ticks or replayed
   dataset.  Producers live in `data_ingestion/`.
2. **Signal Generation** – a Python service computes Kalman-filter
   residuals and a NeMo NIM classifies regime.  Models reside under
   `ml_model/`.
3. **Execution & Risk** – C++/Python engine routes orders and applies
   guardrails.  Code is in `execution_engine/`.
4. **Orchestration & Infrastructure** – Terraform defines MSK, SageMaker
   endpoints, and a Step Function that coordinates Trader and Risk
   agents.

## System Diagram

```mermaid
flowchart LR
    A[Market Ticks] -->|Kafka| B(Kafka Topic)
    B --> C[Kalman Service]
    B --> D[NIM Regime Classifier]
    C --> E[Step Function]
    D --> E
    E --> F[Trader Agent]
    E --> G[Risk Agent]
    F --> H((Order Router))
    G --> H
``` 

## Sequence Diagram

```mermaid
sequenceDiagram
    participant Tick as Tick Producer
    participant Kal as Kalman
    participant NIM as Regime NIM
    participant SF as StepFunction
    participant Router as OrderRouter
    participant Risk as RiskAgent

    Tick->>Kal: send tick
    Tick->>NIM: send tick
    Kal-->>SF: residual
    NIM-->>SF: regime
    SF->>Router: place order
    SF->>Risk: check p-value
    Risk-->>SF: kill if p>0.05
``` 

## UML Class Diagram

```mermaid
classDiagram
    class KalmanFilter {
        +train(data)
        +predict()
    }
    class NemoClassifier {
        +classify(residual,news)
    }
    class TraderAgent {
        +execute(order)
    }
    class RiskAgent {
        +evaluate(p_value)
    }
    class KafkaProducer {
        +send(tick)
    }
    class StepFunction {
        +invoke(payload)
    }
    class SageMakerEndpoint {
        +predict(input)
    }
    KalmanFilter <|-- NemoClassifier
    TraderAgent -- RiskAgent
    KafkaProducer --> KalmanFilter : feeds
    KafkaProducer --> NemoClassifier : feeds
    StepFunction --> TraderAgent : triggers
    StepFunction --> RiskAgent : triggers
    NemoClassifier --> SageMakerEndpoint : optional
```

## Extended Architecture & Tech Stack

To make the architecture diagrams more actionable, each component below
is annotated with the primary technologies or tools that implement it.  The
flowchart above was merely illustrative; the following component diagram is
closer to a "standard" architectural sketch with labeled subsystems and
persistence layers.

```mermaid
flowchart TB
    %% use rounded rectangles for components, cylinder for data stores
    subgraph Cloud [Cloud / Infrastructure]
      direction LR
      infra["Terraform IaC"]
      mske["MSK Kafka Cluster"]
      sf["AWS Step Functions"]
      sm["SageMaker Endpoints"]
    end
    subgraph Services [Application Services]
      direction TB
      ki["Kafka Ingestor\n(Python)"]
      kal["Kalman Filter Service\n(Python + numpy)\n"]
      nim["Regime Classifier\n(NeMo NIM on Torch)"]
      trader["Trader Agent\n(C++ order router)"]
      risk["Risk Agent\n(Python)\n"]
    end
    subgraph DataLayer [Data Layer]
      direction LR
      ticks(("Ticks Topic"))
      metrics(("Metrics Topic"))
    end

    %% relationships
    infra --> mske
    infra --> sf
    infra --> sm

    mske -->|publish/subscribe| ticks
    ticks --> ki
    ki --> kal
    ki --> nim
    kal --> sf
    nim --> sf
    sf --> trader
    sf --> risk
    trader -->|orders| metrics
    risk -->|risk events| metrics
``` 

### Why this version is better

* depicts actual deployment elements (cloud components vs. service boxes)
* uses directional arrows to show publish/subscribe and invocation paths
* separates infrastructure, services, and data layers clearly
* employs familiar shapes (cylinders for topics, rounded rectangles for
  services) akin to UML component or C4 diagrams

### Database / Persistence Schema

Although the current proof‑of‑concept uses Kafka topics instead of a
relational database, a sample schema is provided here to illustrate how one
might persist ticks, orders and risk events in a relational store for
back‑testing or auditing.

```mermaid
erDiagram
    TICK {
        int id PK
        datetime ts
        float price
        string symbol
    }
    "ORDER" {
        int id PK
        string side
        float quantity
        float price
        int tick_id FK
    }
    RISK_EVENT {
        int id PK
        int order_id FK
        string type
        float value
    }
    TICK ||--o{ "ORDER" : contains
    "ORDER" ||--o{ RISK_EVENT : generates
```
### Database / Persistence Schema

Although the current proof‑of‑concept uses Kafka topics instead of a
relational database, a sample schema is provided here to illustrate how one
might persist ticks, orders and risk events in a relational store for
back‑testing or auditing.

```mermaid
erDiagram
    TICK {
        int id PK
        datetime ts
        float price
        string symbol
    }
    "ORDER" {
        int id PK
        string side
        float quantity
        float price
        int tick_id FK
    }
    RISK_EVENT {
        int id PK
        int order_id FK
        string type
        float value
    }
    TICK ||--o{ "ORDER" : contains
    "ORDER" ||--o{ RISK_EVENT : generates
```

---

