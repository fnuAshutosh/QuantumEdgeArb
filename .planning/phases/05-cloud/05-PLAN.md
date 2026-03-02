---
phase: 05-cloud
plan: 01
type: execute
wave: 1
depends_on:
  - 04-backtest
files_modified:
  - infra/terraform/main.tf
  - infra/terraform/variables.tf
  - infra/kubernetes/deployment.yaml
  - ml_model/deploy/Dockerfile
requirements: [REQ-??]

must_haves:
  truths:
    - "Terraform apply succeeds and outputs SageMaker endpoint URL"
    - "Cloud resources can be destroyed with gsd infra:destroy"
  artifacts:
    - path: "infra/terraform/main.tf"
      provides: "AWS resources definition"
  key_links: []
---

<objective>
Achieve fully automated AWS deployment and teardown on free tier.
</objective>

<tasks>
  <!-- tasks for cloud deployment -->
</tasks>
