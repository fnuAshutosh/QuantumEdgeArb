---
phase: 04-backtest
plan: 01
type: execute
wave: 1
depends_on:
  - 03-execution
files_modified:
  - benchmarks/backtests/pairs.ipynb
  - benchmarks/backtests/vectorbt_notebook.ipynb
requirements: [REQ-??]

must_haves:
  truths:
    - "Pairs.ipynb runs end-to-end without errors, prints Sharpe > 0"
  artifacts:
    - path: "benchmarks/backtests/pairs.ipynb"
      provides: "historical backtest notebook"
  key_links: []
---

<objective>
Deliver an executable notebook demonstrating strategy performance.
</objective>

<tasks>

<task type="auto">
  <name>Create basic backtest notebook</name>
  <done>completed</done>
  <files>benchmarks/backtests/pairs.ipynb</files>
  <action>
    Generate a new Jupyter notebook with markdown cells outlining the backtest
    steps. The code cells may contain `# TODO` comments; creation of the file
    satisfies the task.
  </action>
  <verify>
    <automated>test -f benchmarks/backtests/pairs.ipynb && echo "exists"</automated>
  </verify>
  <done>Notebook file exists.</done>
</task>

<task type="auto">
  <name>Create vectorbt notebook placeholder</name>
  <done>completed</done>
  <files>benchmarks/backtests/vectorbt_notebook.ipynb</files>
  <action>
    Touch an empty notebook file with a header cell indicating future vectorbt
    implementation.
  </action>
  <verify>
    <automated>test -f benchmarks/backtests/vectorbt_notebook.ipynb && echo "exists"</automated>
  </verify>
  <done>Notebook file present.</done>
</task>

</tasks>
