# Cloud DevOps AI Project

## About
This project combines cloud deployment, CI/CD automation, observability, and AI-assisted incident analysis into one end-to-end system.

The goal is to demonstrate how a modern application can be deployed, monitored, and supported with automation beyond the initial release process.

This project does not stop at “the app is running.” It integrates deployment, monitoring, alerting, and incident analysis into a single operational workflow.


---
## System Overview

The application is deployed as a Dockerized Flask service on AWS ECS Fargate.

Deployment is automated through GitHub Actions, container images are stored in Amazon ECR, traffic is routed via an Application Load Balancer, and system health is monitored using CloudWatch alarms and dashboards.

A lightweight Incident Assistant reads CloudWatch-style alert data and generates a structured incident summary with severity, likely impact, and recommended response steps.

---
## Architecture

```text
User
  ↓
Application Load Balancer
  ↓
ECS Fargate Service
  ↓
Dockerized Flask App

GitHub Actions
  ↓
Build Docker Image
  ↓
Amazon ECR
  ↓
ECS Deployment

CloudWatch Alarm
  ↓
SNS Notification
  ↓
Incident Assistant
  ↓
Structured Incident Summary

![Architecture](docs/architecture.png)

---

## Key Capabilities

| Capability | Tool / Service |
|---|---|
| Container orchestration | AWS ECS Fargate |
| Image registry | Amazon ECR |
| Traffic routing | Application Load Balancer |
| Automated deployment | GitHub Actions |
| Monitoring | CLoudWatch Alarms + Dashboard |
| Alerting | SNS notification |
| Incident analysis | Python Incident Assistant|

---
## CI/CD Flow

Code push
→ GitHub Actions workflow
→ Docker image build
→ Commit SHA image tag
→ Push to Amazon ECR
→ ECS service update
→ Deployment verification

![CICD](docs/cicd-flow.png)
---

## Observability Flow

CloudWatch metric breach
→ CloudWatch alarm
→ SNS notification
→ Incident Assistant input
→ Structured incident summary

![Observability](docs/observability-model.png)
---

## Why This Is Different
Many portfolio projects stop once the application is deployed.

This project goes further by connecting:

- deployment automation
- container orchestration
- health checks
- monitoring
- alerting
- incident response support

The Incident Assistant connects my cloud and DevOps work with my AI/automation background by showing how operational signals can be converted into structured response guidance.

---

## Incident Assistant
The incident-assistant/ module reads a CloudWatch-style alert JSON file and produces:

- incident summary
- severity assessment
- likely impact
- recommended first checks
- suggested response steps

Run locally:

```bash
cd incident-assistant
python incident_summary.py
```
The current implementation is rule-based by design.

The severity assessment logic is isolated in a get_severity() function, so it can later be replaced with an LLM API call without changing the surrounding architecture.

See [incident-assistant/README.md](incident-assistant/README.md)

---

## Validation
The project was validated through:
- ECS Fargate service successfully serving traffic through ALB
- ALB target group reporting healthy targets
- GitHub Actions pipeline completing successfully on code push
- CloudWatch alarms configured and tested
- Incident Assistant generating structured output from alert JSON
- Deployment issues documented and resolved during implementation

---

## Troubleshooting Encountered
### Exit code 137
Issue:
Fargate killed the container due to insufficient memory allocation.

Resolution:
Increased the task definition to 0.5 vCPU / 1 GB memory.

Lesson:
Container memory sizing must account for runtime overhead, dependencies, and application behavior.

### Health check timeouts
Issue:
ECS tasks were initially placed in private subnets without NAT Gateway access, causing networking and health check failures.

Resolution:
Adjusted service networking to use public subnets for this development deployment.

Production Note:
In production, tasks should run in private subnets with NAT Gateway or VPC endpoints for outbound service access.

---

## Design Decisions
See [docs/decisions.md](docs/decisions.md)
Topics include:

- ECS Fargate vs EC2
- GitHub Actions for CI/CD
- ECR for image storage
- rule-based incident assistant vs LLM-based analysis
- public subnet development deployment vs private subnet production deployment
---  

## Production Gaps
See [docs/production-gaps.md](docs/production-gaps.md)
Current gaps include:

- HTTPS with ACM
- private subnet deployment with NAT Gateway or VPC endpoints
- Secrets Manager integration
- Terraform-based ECS provisioning
- CloudWatch log aggregation
- automated rollback strategy
- LLM-powered incident triage
- WAF protection
---

## What This Demonstrates

This project demonstrates the ability to:

- deploy containerized workloads on managed cloud infrastructure
- automate releases through CI/CD
- route traffic using health-based load balancing
- monitor system health with CloudWatch
- document and resolve deployment failures
- connect cloud operations with AI-assisted incident response

## Repository Structure
cloud-devops-ai-project/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── incident-assistant/
│   ├── incident_summary.py
│   ├── sample_alert.json
│   └── README.md
├── docs/
│   ├── architecture.png
│   ├── cicd.png
│   ├── observability.png
│   ├── decisions.md
│   └── production-gaps.md
├── screenshots/
│   ├── ecs-service.png
│   ├── alb-targets.png
│   ├── github-actions.png
│   ├── cloudwatch-alarm.png
│   └── incident-summary.png
└── README.md
