---
phase: 03-execution
plan: 01
type: execute
wave: 1
depends_on:
  - 02-signal
files_modified:
  - execution_engine/include/order.h
  - execution_engine/include/risk.h
  - execution_engine/src/order_router.cpp
  - execution_engine/src/risk_engine.cpp
  - execution_engine/tests/test_order_router.cpp
requirements: [REQ-??]

must_haves:
  truths:
    - "RiskEngine.check_risk throws when p_value > kill threshold"
    - "OrderRouter.route_order logs JSON and returns true on approval"
  artifacts:
    - path: "execution_engine/include/order.h"
      provides: "Order struct definition"
  key_links: []
---

<objective>
Build the C++ execution engine and integrate with the Python risk glue.
</objective>

<tasks>
  <!-- tasks to be added -->
</tasks>
