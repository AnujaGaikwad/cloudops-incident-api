# CloudOps Rescue Center

A containerized cloud incident management platform built with Python and Flask, demonstrating the container lifecycle from local Docker Compose development to AWS ECS Fargate and Kubernetes.

## Objective

CloudOps Rescue Center simulates a production-style operations platform with separate services for incident management, notifications, and a web dashboard.

The project demonstrates containerization, service networking, health checks, scaling, self-healing, rolling updates, and rollback.

## Architecture

```text
User
  |
  v
Frontend :3000
  |
  v
Incident API :5000
  |
  v
Notification Service :5001

Local: Docker -> Docker Compose
AWS:   Amazon ECR -> Amazon ECS/Fargate
K8s:   Kubernetes Deployment -> Service -> Replicas
```

## Services

### Frontend
- Flask dashboard
- Port `3000`
- User-facing incident management interface

### Incident API
- Flask REST API
- Port `5000`
- Handles incident operations
- Includes a health endpoint
- Containerized and deployed to Amazon ECR/ECS

### Notification Service
- Flask service
- Port `5001`
- Handles notification-related service communication

## Technology Stack

| Category | Technologies |
|---|---|
| Language | Python |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| Containers | Docker |
| Local orchestration | Docker Compose |
| Container registry | Amazon ECR |
| AWS compute | Amazon ECS with Fargate |
| AWS networking | VPC, Security Groups |
| Monitoring | Amazon CloudWatch |
| Orchestration | Kubernetes |
| Development | VS Code, PowerShell |
| Version control | Git, GitHub |

## Project Structure

```text
cloudops-rescue-center/
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── script.js
│       └── style.css
├── incident-api/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── notification-service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── .gitignore
```

Local Python virtual-environment files are intentionally excluded from Git.

## Run Locally

### Prerequisites

- Python 3
- Docker Desktop
- Docker Compose
- Git

### Start

From the project root:

```bash
docker compose up --build
```

Services:

```text
Frontend:       http://localhost:3000
Incident API:   http://localhost:5000
Notification:   http://localhost:5001
```

### Stop

```bash
docker compose down
```

## Health Check

Example:

```bash
curl http://localhost:5000/health
```

## AWS Deployment

### Amazon ECR

AWS Region:

```text
ap-south-1
```

ECR repository:

```text
cloudops-incident-api
```

The Incident API container image was built locally and pushed to Amazon ECR.

### Amazon ECS Fargate

Recorded deployment configuration:

```text
Cluster: cloudops-rescue-cluster
Service: cloudops-incident-api-service-spez2sjs
Launch type: Fargate
CPU: 0.5 vCPU
Memory: 1 GiB
Container port: 5000
```

ECS Fargate demonstrates running the container without directly managing EC2 servers.

## Kubernetes

The project was also used to demonstrate Kubernetes operations:

- Deployment of the Incident API
- Scaling from 2 to 3 replicas
- Pod self-healing/replacement
- NodePort exposure
- Rolling update
- Version update from `latest` to `v2`
- Rollback

Recorded state:

```text
Deployment: incident-api
Replicas: 3/3
NodePort: 5000:31002
```

The currently verified local repository structure does not contain a `k8s/` directory, so Kubernetes manifests are not falsely listed as repository files.

## Container Lifecycle

```text
Flask Services
     |
     v
 Dockerfiles
     |
     v
Docker Compose
     |
     v
 Local Testing
     |
     v
 Amazon ECR
     |
     v
ECS Fargate
     |
     v
 Kubernetes
     |
     +-- Scaling
     +-- Self-healing
     +-- Rolling Update
     +-- Rollback
```

## Security

The repository excludes sensitive and environment-specific files through `.gitignore`, including:

- `.env` files
- PEM/private-key files
- Python virtual environments
- Python cache files
- IDE configuration
- Local logs

AWS credentials should never be hardcoded into source code. Use IAM roles, environment-based configuration, or another secure credential mechanism appropriate to the deployment.

## Key DevOps Concepts Demonstrated

- Dockerizing Python Flask services
- Multi-container application networking
- Docker Compose orchestration
- Amazon ECR image management
- ECS Fargate deployment
- Kubernetes replicas and scaling
- Kubernetes self-healing
- Rolling updates
- Deployment rollback
- Cloud networking and security groups
- CloudWatch operational visibility

## Key Learnings

- How to Dockerize Python Flask applications
- How multiple services communicate in a containerized environment
- How Docker Compose supports local multi-service development
- How to build and push images to Amazon ECR
- How to deploy containers with ECS Fargate
- How Kubernetes maintains desired replica counts
- How scaling, rolling updates, and rollback work
- How cloud networking and security groups affect containerized applications

## Resume Description

**CloudOps Rescue Center | Python, Docker, Docker Compose, AWS ECR, ECS Fargate, Kubernetes**

Built a containerized 3-service incident management system and deployed it from local Docker Compose to AWS Fargate and Kubernetes, demonstrating service networking, health checks, scaling, self-healing, rolling updates, and rollback.

## Interview Explanation

> I built CloudOps Rescue Center to understand the complete container lifecycle, from Dockerizing a Python microservice application to deploying it on AWS Fargate and using Kubernetes for scaling, self-healing, rolling updates, and rollback.

## Project Note

This is a learning and portfolio project intended to demonstrate cloud, containerization, and DevOps concepts. It is not intended to represent a production incident-management platform with enterprise-grade security, authentication, observability, or disaster recovery.

## Author

**Anuja Gaikwad**

GitHub: https://github.com/AnujaGaikwad
