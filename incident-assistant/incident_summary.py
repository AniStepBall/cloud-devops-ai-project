import json
from datetime import datetime, UTC


def get_severity(observed, threshold):
    """
    Compare the observed value against the threshold
    and return a severity level.
    """

    try:
        observed_value = float(observed.replace("%", ""))
        threshold_value = float(threshold.replace("%", ""))

        difference = observed_value - threshold_value

        if difference > 30:
            return "HIGH"
        elif difference > 15:
            return "MEDIUM"
        else:
            return "LOW"

    except:
        return "UNKNOWN"


def get_recommendations(metric):
    """
    Return troubleshooting steps based on the metric.
    """

    if metric == "CPUUtilization":
        return """
1. Check that all ECS tasks are healthy
2. Look for recent deployments
3. Review application logs
4. Consider scaling the service
5. Check if traffic has increased
"""

    elif metric == "HealthyHostCount":
        return """
1. Check the health status of target group
2. Verify that all ECS tasks are running
3. Confirm security group rules
4. Check subnet configuration (especially to show only public subnets)
5. Review all stopped task errors
"""

    else:
        return """
1. Check the status health for each service
2. Review the corresponding CloudWatch metrics
3. Check the application logs
4. Verify target health
5. Roll back any recent changes if necessary
"""


def summarize_incident(event):
    """
    Create a readable incident summary.
    """

    alarm_name = event.get("alarm_name", "Unknown Alarm")
    metric = event.get("metric", "Unknown Metric")
    threshold = event.get("threshold", "Unknown")
    observed = event.get("observed_value", "Unknown")
    resource = event.get("resource", "Unknown Resource")

    severity = get_severity(observed, threshold)

    recommendations = get_recommendations(metric)

    current_time = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")

    summary = f"""
==================================================
                 INCIDENT SUMMARY
==================================================
Time:             {current_time} UTC
Alarm:            {alarm_name}
Resource:         {resource}
Metric:           {metric}
Observed Value:   {observed}
Threshold:        {threshold}
Severity:         {severity}

LIKELY IMPACT:
The service may be running slower than expected
or may be unavailable to some users.

RECOMMENDED FIRST CHECKS:
{recommendations}

ESCALATE IF:
- The issue lasts more than 15 minutes
- Multiple alarms trigger at the same time
- Service health checks continue to fail
==================================================
"""

    return summary


if __name__ == "__main__":

    with open("sample_alert.json", "r") as file:
        event = json.load(file)

    print(summarize_incident(event))
