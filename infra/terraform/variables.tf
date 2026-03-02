variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "sagemaker_instance_type" {
  description = "Instance type for SageMaker endpoint"
  default     = "ml.t3.medium"
}

variable "mks_broker_count" {
  description = "Number of MSK brokers"
  default     = 1
}
