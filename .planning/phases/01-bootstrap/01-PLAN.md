---
phase: 01-bootstrap
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - data_ingestion/coinbase/ws_client.py
  - ml_model/cointegration.py
  - execution_engine/tests/test_order_router.cpp
autonomous: true
requirements: [REQ-01]

must_haves:
  truths:
    - "A stub Kafka producer exists in the data_ingestion package"
    - "The cointegration module contains a train() function"
    - "There is at least one unit test for the order router"
  artifacts:
    - path: "data_ingestion/coinbase/ws_client.py"
      provides: "Kafka producer stub"
    - path: "ml_model/cointegration.py"
      provides: "cointegration training placeholder"
    - path: "execution_engine/tests/test_order_router.cpp"
      provides: "GoogleTest file for OrderRouter"
  key_links: []
---

<objective>
Bootstrap repository with skeletal components to make development tangible.
Purpose: establish the basic directories, stub code and tests so future work
can build on them.
Output: three new or modified files representing the initial pieces of each
major subsystem.
</objective>

<execution_context>
@./.claude/get-shit-done/workflows/execute-plan.md
@./.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@docs/ARCHITECTURE.md
@README.md
</context>

<tasks>

<task type="auto">
  <name>Task 1: Add Kafka producer stub</name>
  <files>data_ingestion/coinbase/ws_client.py</files>
  <action>
    Create a new Python file at `data_ingestion/coinbase/ws_client.py`.
    Define a class or function named `send_tick(topic, tick)` that merely
    prints the tick or writes it to a local file; the implementation can be a
    placeholder since the real Kafka client will come later.
  </action>
  <verify>
    <automated>python -m pyflakes data_ingestion/coinbase/ws_client.py || true</automated>
  </verify>
  <done>A Python module exists with a `send_tick` symbol and pyflakes reports
no syntax errors.</done>
</task>

<task type="auto" tdd="true">
  <name>Task 2: Implement cointegration train stub</name>
  <files>ml_model/cointegration.py, ml_model/tests/test_cointegration.py</files>
  <behavior>
    - when train([]) is called it returns None without error
  </behavior>
  <action>
    Write tests first in `ml_model/tests/test_cointegration.py` asserting that
    `ml_model.cointegration.train([])` exists and returns None.  Then implement
    the minimal `train` function in `ml_model/cointegration.py` to satisfy the
    test.
  </action>
  <verify>
    <automated>python -m unittest discover -s ml_model/tests</automated>
  </verify>
  <done>A passing unit test confirms the train stub is available.</done>
</task>

<task type="auto">
  <name>Task 3: Add order router unit test</name>
  <files>execution_engine/tests/test_order_router.cpp</files>
  <action>
    Create a new GoogleTest source file that includes `order_router.cpp` or the
    appropriate header and contains one trivial test case (e.g. constructing an
    OrderRouter object).  The file can be a stub; the goal is simply to ensure
    the C++ test suite compiles.
  </action>
  <verify>
    <automated>cd build && ctest -R order_router --output-on-failure || true</automated>
  </verify>
  <done>CTest reports at least one test called `order_router` (may be pending).</done>
</task>

</tasks>

<verification>
Run `gsd deps` to ensure dependencies install, then execute `/gsd ml:test` and
`/gsd exec:test` from the Copilot chat window to confirm the new tests
compile/run.
</verification>

<success_criteria>
Roadmap contains Phase 01 entry; plan file exists with three tasks; stub code
and tests are committed; running the existing gsd tasks produces no errors.
</success_criteria>

<output>
After completion, create `.planning/phases/01-bootstrap/01-PLAN-SUMMARY.md`
</output>
