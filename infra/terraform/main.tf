provider "aws" {
  region = var.region
}

# MSK cluster with a single topic for tick data
resource "aws_msk_cluster" "kafka" {
  cluster_name           = "quantum-msk"
  kafka_version          = "2.8.1"
  number_of_broker_nodes = var.mks_broker_count

  broker_node_group_info {
    instance_type = "kafka.t3.small"
  }
}

# SageMaker model and endpoint (placeholder)
resource "aws_sagemaker_model" "cointegration" {
  name          = "cointegration-model"
  execution_role_arn = "arn:aws:iam::123456789012:role/SageMakerRole" # replace

  primary_container {
    image = "123456789012.dkr.ecr.${var.region}.amazonaws.com/cointegration:latest"
  }
}

resource "aws_sagemaker_endpoint_configuration" "cointegration_config" {
  name = "cointegration-config"
  production_variants {
    variant_name           = "AllTraffic"
    model_name             = aws_sagemaker_model.cointegration.name
    initial_instance_count = 1
    instance_type          = var.sagemaker_instance_type
  }
}

resource "aws_sagemaker_endpoint" "cointegration" {
  name                 = "cointegration-endpoint"
  endpoint_config_name = aws_sagemaker_endpoint_configuration.cointegration_config.name
}

# Step Function for trading and risk agents
resource "aws_sfn_state_machine" "trading" {
  name     = "trading-state-machine"
  role_arn = "arn:aws:iam::123456789012:role/StepFunctionsRole" # replace

  definition = <<EOF
{
  "Comment": "Trader + Risk orchestration",
  "StartAt": "IngestTick",
  "States": {
    "IngestTick": {
      "Type": "Pass",
      "Next": "ParallelAgents"
    },
    "ParallelAgents": {
      "Type": "Parallel",
      "Branches": [
        {
          "StartAt": "TraderAgent",
          "States": {
            "TraderAgent": {"Type": "Pass","End": true}
          }
        },
        {
          "StartAt": "RiskAgent",
          "States": {
            "CheckP": {
              "Type": "Pass",
              "Next": "KillSwitch"
            },
            "KillSwitch": {
              "Type": "Choice",
              "Choices": [
                {
                  "Variable": "$.p_value",
                  "NumericGreaterThan": 0.05,
                  "Next": "Terminate"
                }
              ],
              "Default": "Continue"
            },
            "Terminate": {"Type": "Fail","Cause": "p>0.05"},
            "Continue": {"Type": "Pass","End": true}
          }
        }
      ],
      "Next": "Done"
    },
    "Done": {"Type": "Succeed"}
  }
}
EOF
}
