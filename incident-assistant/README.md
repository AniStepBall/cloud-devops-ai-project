# Incident Assistant

A rule-based incident summarization tool that reads CloudWatch-style alert JSON and produces a structured incident summary with metric-specific remediation steps.

## How to Run
```bash
python incident_summary.py
```

## How it Works
1. Reads the JSON alert file (simulating a CloudWatch/SNS payload)
2. Calculates severity based on how far the observed value exceeds the threshold
3. Selects metric-specific recommendations from a playbook
4. Outputs a structured incident summary

## Extension Path
This rule-based version demonstrates the workflow. The natural next step is replacing the playbook lookup with an LLM call (e.g. Cluade API or OpenAI) to generate dynamic, context-aware reommendations based on the full alert payload.
