# Observability Model

## Metrics Monitored
| Metrics | Source | Alarm Threshold |
|---|---|---|
| CPUUtilization | ECS Service | > 70 % for 5 min |
| HealthyHostCount | ALB Target Group | < 1 |

## Alert Flow
CloudWatch Alarm -> SNS Topic -> Email Notification -> Runbook -> Incident Assistant

## Incident Assistant
The incident-assistant script reads alert payloads and produces structured summaries with metric-specific remediation steps. In production this would integrate directly with SNS via Lambda.
