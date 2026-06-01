# Operations Runbook

## High CPU Alarm (week8-high-cpu-alarm)

### Trigger
CPUUtilization > 70% for 5 minutes on ECS service.

### Immediate Steps
1. Check the running task count uynder ECS services
2. Check the CPU trends under CloudWatch. Checks whether the trends are rising or stabilizing
3. Check recent deployments. Confirm wether the CPU spiked after
4. Check the Application Load Balancers (ALB) whether the traffic is higher than normal

### Resolution Options
- Traffic spike: increase ECS desired task count
- Bad deployment: force new deployment with previous image
- Persistent: increase task CPU allocation in task definition

### Escalate If
CPU stays above 90% for more than 15 minutes.

---

## No Healthy Hosts (week8-no-healthy-hosts)

### Trigger
ALB HealthyHostCount < 1

### Immediate Steps
1. Check EC2 → Target Groups → check target health status
2. Check ECS tasks are RUNNING not STOPPED
3. Verify ECS task SG allows port 5000 from ALB SG
4. Verify ECS service is using public subnets only
5. Check stopped task details for error messages: Exit code 137 (increase task memory in task definition)

### Resolution Options
- Wrong subnets: update service networking to public subnets only
- Memory issue: increase task definition memory and redeploy
- SG issue: fix inbound rules on ECS task security group

