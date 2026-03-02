---
phase: 06-restructure
plan: 01
type: execute
wave: 1
depends_on:
  - 05-cloud
files_modified: []
autonomous: true
requirements: [REQ-??]

must_haves:
  truths:
    - "Old source directories no longer exist"
    - "New skeleton directories match the layout described in docs/"
  artifacts:
    - path: "data_ingestion/"
      provides: "ingestion package skeleton"
    - path: "ml_model/"
      provides: "ml package skeleton"
  key_links: []
---

<objective>
Wipe existing folders and create a clean directory structure matching the
documentation.  This will serve as a neutral starting point for ongoing
implementation.
</objective>

<tasks>
<task type="auto">
  <name>Task 1: Delete old top-level directories</name>
  <action>
    Remove `data_ingestion`, `ml_model`, `execution_engine`, `infra`,
    `benchmarks` directories entirely (use `rm -rf` or platform equivalent).
    Preserve `docs` and `.planning`.
  </action>
  <verify>
    <automated>ls -1 | grep -E "^(data_ingestion|ml_model|execution_engine|infra|benchmarks)" || true</automated>
  </verify>
  <done>The listed directories are gone from the repo root.</done>
</task>

<task type="auto">
  <name>Task 2: Recreate skeleton directory structure</name>
  <action>
    Use `mkdir -p` to rebuild the following tree with placeholder `README.md`
    or empty `__init__.py` files where appropriate:

    data_ingestion/coinbase/python_client
    data_ingestion/binance/cpp_client
    ml_model/src
    ml_model/deploy
    ml_model/tests
    execution_engine/include
    execution_engine/src
    execution_engine/tests
    infra/kubernetes
    infra/terraform
    benchmarks/backtests
    benchmarks/chaos
  </action>
  <verify>
    <automated>find data_ingestion ml_model execution_engine infra benchmarks -maxdepth 3 -type d | head</automated>
  </verify>
  <done>All directories exist with at least one placeholder file each.</done>
</task>

<task type="auto">
  <name>Task 3: Add README/placeholder files in new dirs</name>
  <action>
    Create `README.md` in each top-level directory summarizing its purpose and
    place empty `__init__.py` where Python packages reside.
  </action>
  <verify>
    <automated>grep -R "#" data_ingestion/README.md || true</automated>
  </verify>
  <done>Each new folder contains a descriptive README or init file.</done>
</task>

</tasks>

<verification>
Run `git status` to ensure directories have been removed/added correctly, and
verify the new tree matches the example in `docs/`.
</verification>

<success_criteria>
A clean, empty skeleton tree exists, ready for files to be added according to
Sections 2 and 7 of `PROMPT.md`.  No residual source code remains in the old
locations.
</success_criteria>

<output>
After completion, create `.planning/phases/06-restructure/06-PLAN-SUMMARY.md`
</output>
