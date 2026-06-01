# Incident Assistant

A rule-based incident summarization tool that reads a CloudWatch-style alert JSON and produces a structured incident summary with severity assessment and recommended first-respone steps.

## How to Run
```bash
python incident_summary.py
```

## Sample Input Format
```json
{
  "alarm_name": "week8-high-cpu",
  "metric": "CPUUtilization",
  "threshold": "70%",
  "observed_value": "91%",
  "resource": "ecs-service/week8-fargate-service",
  "region": "ca-central-1"
}
```

## Severity Logic
| Metric | Observed Value | Severity |
|---|---|---|
| CPUUtilization | >= 90% | CRITICAL |
| CPUUtilization | >= 70% | WARNING |
| HealthyHostCount | 0 | CRITICAL |
| HealthyHostCount | 1 | WARNING |

## How it Works
1. Reads the JSON alert file (simulating a CloudWatch/SNS payload)
2. Calculates severity based on how far the observed value exceeds the threshold
3. Selects metric-specific recommendations from a playbook
4. Outputs a structured incident summary

## Extension Path
- This rule-based version demonstrates the workflow.
- In production, this JSON rule-based would be replaced LLM call (e.g. Cluade API or OpenAI) to generate dynamic, context-aware reommendations based on the full alert payload.
