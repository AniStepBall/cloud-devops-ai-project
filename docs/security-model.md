# Security Model

| Layer | Control |
|---|---|
| ALB | Accepts HTTP port 80 from internet only |
| ECS Tasks | Accepts port 5000 from ALB SG only |
| ECR | Private registry, IAM auth only |
| GitHub Secrets | AWS credentials encrypted, never in code |
| IAM | Least-privilege user for GitHub Actions |

## Production Gaps
- No HTTPS (would add ACM certificate)
- No WAF on ALB
- ECS tasks in public subnets (would move to private + NAT)
- No Secrets Manager for environment variables
