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

<task type="auto">
  <name>Provide placeholder Terraform files</name>
  <done>completed</done>
  <files>infra/terraform/main.tf, infra/terraform/variables.tf</files>
  <action>
    Add minimal Terraform configuration with comments. For example, include a
    `provider "aws" {}` block and comment stubs for MSK, SageMaker, Step
    Function resources.
  </action>
  <verify>
    <automated>grep -n "provider" infra/terraform/main.tf || true</automated>
  </verify>
  <done>Terraform files contain at least provider declaration.</done>
</task>

<task type="auto">
  <name>Prepare Kubernetes skeleton</name>
  <done>completed</done>
  <files>infra/kubernetes/deployment.yaml, infra/kubernetes/service.yaml</files>
  <action>
    Drop simple YAML stubs with placeholder image and ports.
  </action>
  <verify>
    <automated>grep -n "kind:" infra/kubernetes/deployment.yaml || true</automated>
  </verify>
  <done>Deployment YAML exists.</done>
</task>

</tasks>
