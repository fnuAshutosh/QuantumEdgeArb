# Cost Summary

This project is designed to run on the **AWS free tier** or completely
locally.  Below are typical expenses if you choose to spin up cloud
resources for a short demo.

| Component            | Free‑tier / alternative                       | Estimated cost          |
|----------------------|-----------------------------------------------|-------------------------|
| Kafka broker (MSK)   | t3.micro EC2 or Confluent Cloud free tier     | $0 (free tier)          |
| SageMaker endpoint   | ml.t3.medium instance (stopped when idle)     | $0–$1/month             |
| Step Functions       | first 4 K transitions per month free          | $0                      |
| GPU compute (G5)     | spot instance or local GPU                   | ~$5 for a 1‑hour demo   |
| Storage / logs       | S3 free 5 GB                                  | $0                      |
| Networking           | local / free tier                             | $0                      |

> **Total**: essentially $0 unless you run a GPU for more than an hour.
> The highest single cost is the spot GPU session used for benchmarking,
> which can be covered with university or cloud credits.
