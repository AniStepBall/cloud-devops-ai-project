# Cloud DevOps AI Project

## About
This project combines modern cloud deployment, CI/CD automation, observability, and AI-assisted incident analysis into one system.

---

## Architecture

![Architecture](docs/architecture.png)

### CI/CD

![CICD](docs/cicd-flow.png)

### Observability

![Observability](docs/observability-model.png)

---

## Key Capabilities

| Capability | Tool |
|---|---|
| Container orchestration | ECS Fargate |
| Image registry | Amazon ECR |
| Traffic routing | Application Load Balancer |
| Automated deployment | GitHub Actions |
| Monitoring | CLoudWatch Alarms + Dashboard |
| Alerting | SNS notification |
| Incident analysis | Incident Assistant script |

---

## Why This Is Different
This system does not stop at deployment. It includes operational visibility and a first step toward intelligent incident response connecting cloud infrastructure with automation and AI tools.

---

## Incident Assistant

### How to Run the Incident Assistant
```bash
cd incident-assistant
python incident_summary.py
```

The `incident-assistant/` module reads a CloudWatch-style alert JSON and produces a structured incident summary with severity assessment and recommended response steps.

It is currently using a rule-based structure and it is designed in a way that the severity assessment function (i.e., `get_severity` function) can be replaced with an LLM API call without changing the surrounding architecture.

See [incident-assistant/README.md](incident-assistant/README.md)

---

## Validation
- App deployed to ECS Fargate and is serving traffic via Application Load Balancer (ALB)
- ALB target group shows healthy status
- Github Actions pipeline deploys on every push and shows no errors
- CloudWatch alarms configured and tested
- Incident assistant generates summary from alert JSON

---

## Troubleshooting Encountered
### Exit code 137
Fargate killed the container due to insufficient memory.
Fixed by increasing task definition to 0.5 vCPU / 1 GB.

### Health check timeouts
ECS tasks placed in private subnets with no NAT Gateway.
Fixed by restricting service networking to public subnets only.

---

## Design Decisions
See [docs/decisions.md](docs/decisions.md)

## Production Gaps
See [docs/production-gaps.md](docs/production-gaps.md)
