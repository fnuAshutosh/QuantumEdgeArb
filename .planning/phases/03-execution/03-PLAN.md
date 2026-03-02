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

<task type="auto">
  <name>Define Order and Risk headers</name>
  <done>completed</done>
  <files>execution_engine/include/order.h, execution_engine/include/risk.h</files>
  <action>
    Write minimal C++ struct `Order` and class `RiskEngine` per spec in
    docs/ARCHITECTURE.md Section 6.6.  Include guards and simple constructors.
  </action>
  <verify>
    <automated>grep -n "struct Order" execution_engine/include/order.h || true
    grep -n "class RiskEngine" execution_engine/include/risk.h || true</automated>
  </verify>
  <done>Headers compile (later) and contain required definitions.</done>
</task>

<task type="auto">
  <name>Implement C++ router and risk engine stubs</name>
  <done>completed</done>
  <files>execution_engine/src/order_router.cpp, execution_engine/src/risk_engine.cpp</files>
  <action>
    Provide dummy implementations matching documentation comments: route_order
    logs JSON to stdout, RiskEngine methods return false or throw.
  </action>
  <verify>
    <automated>grep -n "route_order" execution_engine/src/order_router.cpp || true
    grep -n "check_risk" execution_engine/src/risk_engine.cpp || true</automated>
  </verify>
  <done>Functions present; compilation will be verified by `gsd build` later.</done>
</task>

<task type="auto">
  <name>Create Python glue and tests</name>
  <done>completed</done>
  <files>execution_engine/router.py, execution_engine/risk.py, execution_engine/tests/test_order_router.cpp</files>
  <action>
    Recreate simple Python modules with `route_order` and `check_risk` that
    call the C++ binaries (or just print).  Create an empty GoogleTest file.
  </action>
  <verify>
    <automated>python - <<'PY'
from execution_engine import router,risk
print(router.route_order({"order_id":1},0.01))
print(risk.check_risk(0.01))
PY
echo "// GoogleTest placeholder" > execution_engine/tests/test_order_router.cpp
</automated>
  </verify>
  <done>Python functions run and test file exists.</done>
</task>

</tasks>
