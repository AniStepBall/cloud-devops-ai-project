import json
from datetime import datetime, UTC


def get_severity(metric, observed_value):
    """
    Rule-based severity assessment.
    """

    try:
        value = float(observed_value.replace("%", "").strip())

    except (ValueError, AttributeError):
        return "UNKNOWN"

    if metric == "CPUUtilization":
        if value >= 90:
            return "CRITICAL"
        elif value >= 70:
            return "WARNING"
        else:
            return "OK"
    elif metric == "HealthyHostCount":
        if value == 0:
            return "CRITICAL"
        elif value == 1:
            return "WARNING"
        else:
            return "OK"
    else:
        return "WARNING"


def summarize_incident(event):
    """
    Create a readable incident summary.
    """

    alarm_name = event.get("alarm_name", "Unknown Alarm")
    metric = event.get("metric", "Unknown Metric")
    threshold = event.get("threshold", "Unknown Threshold")
    observed = event.get("observed_value", "Unknown")
    resource = event.get("resource", "Unknown Resource")
    region = event.get("resource", "Unknown Region")

    severity = get_severity(metric, observed)

    summary = f"""
==================================================
                 INCIDENT SUMMARY
==================================================
Time:             {datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")} UTC
Alarm:            {alarm_name}
Resource:         {resource}
Region:           {region}
Metric:           {metric}
Observed Value:   {observed}
Threshold:        {threshold}
Severity:         {severity}

Likely Impact:
The service may be running slower than expected or may be unavailable to some users.

Recommended First Checks:
1. Confrim ECS service health in AWS Console.
2. Check CloudWatch metrics and recent deployment history.
3. Review applications logs in CloudWatch Logs.
4. Validate Application Load Balancers target group health.
5. Roll back recent changes if issues began after a deployment.

See docs/runbook.md for more in depth step-by-step respone procedures.
==================================================
"""

    return summary


if __name__ == "__main__":
    with open("sample_alert.json", "r") as file:
        event = json.load(file)

    print(summarize_incident(event))
