# Design Decisions and Tradeoffs

## ECS Fargate over EC2
Removes sever management overhead. Tradeoff is less control over underlying compute.

## ECS over EKS
Simpler and faster to operationalize. EKS provides more portability via Kubernetes but adds significant complexity.

## ECR over Docker Hub
Private by default, native IAM integration, no rate limits.

## Public subnets for ECS tasks
Private subnets with NAT Gateway would be more secure but adds ~$32/month. Acceptable tradeoff for this project stage with security groups loacked down.

## Rule-based incident assistant over LLM
Avoids paid API dependency while demonstrating the workflow.
The `get_severity` function is designed to be replaceable with an LLM call without changing the surrounding architecture.

## GitHub Actions over CodePipeline
Lower barrier to entry, better developer experience, reusable across any cloud provider.
