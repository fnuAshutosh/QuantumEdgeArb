---
phase: 02-signal
plan: 01
type: execute
wave: 1
depends_on:
  - 01-bootstrap
files_modified:
  - ml_model/nemo_classifier.py
  - ml_model/deploy/api_server.py
  - ml_model/src/preprocess.py
  - ml_model/src/train.py
  - .env.example
requirements: [REQ-??]

must_haves:
  truths:
    - "NemoClassifier.classify calls NIM API and returns dict"
    - "/predict endpoint returns JSON conforming to schema"
  artifacts:
    - path: "ml_model/nemo_classifier.py"
      provides: "regime classification via HTTP"
  key_links: []
---

<objective>
Implement the signal pipeline components: real NIM call and prediction API.
</objective>

<tasks>
  <!-- tasks will be filled during planning -->
</tasks>
