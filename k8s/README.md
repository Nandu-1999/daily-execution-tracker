# Daily Execution Tracker - Kubernetes Deployment

## Overview

This folder contains the Kubernetes manifests required to deploy the Daily Execution Tracker application.

### Application Architecture

```text
Browser
   ↓
Ingress
   ↓
+-------------------+
|   Frontend (NGINX)|
+-------------------+
   ↓
+-------------------+
| FastAPI Backend   |
+-------------------+
   ↓
+-------------------+
| PostgreSQL        |
| (PVC-backed)      |
+-------------------+
```

---

## Components

### Frontend

* Angular application
* Served using Nginx
* Exposed through a Kubernetes Service
* Accessible through Ingress

Files:

* `frontend-deployment.yaml`
* `frontend-service.yaml`

---

### Backend

* FastAPI application
* JWT Authentication
* Task and Activity APIs
* Connected to PostgreSQL

Files:

* `backend-deployment.yaml`
* `backend-service.yaml`

---

### Database

* PostgreSQL 17
* Persistent storage using PVC

Files:

* `postgres-deployment.yaml`
* `postgres-service.yaml`
* `postgres-pvc.yaml`

---

### Ingress

Ingress routes traffic based on path:

| Path          | Service  |
| ------------- | -------- |
| `/auth`       | Backend  |
| `/tasks`      | Backend  |
| `/activities` | Backend  |
| `/health`     | Backend  |
| `/`           | Frontend |

File:

* `det-ingress.yaml`

---

## Prerequisites

Install:

* Docker Desktop
* Minikube
* kubectl

Verify installation:

```bash
minikube version
kubectl version --client
docker --version
```

---

## Start Minikube

```bash
minikube start --driver=docker
```

Verify:

```bash
kubectl get nodes
```

Expected:

```text
NAME       STATUS   ROLES
minikube   Ready    control-plane
```

---

## Load Docker Images

Backend:

```bash
docker build -t daily-execution-tracker-backend:latest .
minikube image load daily-execution-tracker-backend:latest
```

Frontend:

```bash
docker build -t daily-execution-tracker-frontend:latest .
minikube image load daily-execution-tracker-frontend:latest
```

---

## Deploy Application

### PostgreSQL

```bash
kubectl apply -f postgres-pvc.yaml
kubectl apply -f postgres-deployment.yaml
kubectl apply -f postgres-service.yaml
```

### Backend

```bash
kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml
```

### Frontend

```bash
kubectl apply -f frontend-deployment.yaml
kubectl apply -f frontend-service.yaml
```

### Ingress

Enable ingress:

```bash
minikube addons enable ingress
```

Apply ingress:

```bash
kubectl apply -f det-ingress.yaml
```

Run tunnel:

```bash
minikube tunnel
```

Add hosts entry:

```text
127.0.0.1 det.local
```

---

## Database Migration

Run migrations inside backend pod:

```bash
kubectl exec -it deployment/det-backend -- sh
```

```bash
alembic upgrade head
```

Verify:

```bash
alembic current
```

---

## Useful Commands

### View Pods

```bash
kubectl get pods
```

### View Services

```bash
kubectl get services
```

### View Deployments

```bash
kubectl get deployments
```

### View PVC

```bash
kubectl get pvc
```

### Backend Logs

```bash
kubectl logs deployment/det-backend -f
```

### Frontend Logs

```bash
kubectl logs deployment/det-frontend -f
```

### PostgreSQL Access

```bash
kubectl exec -it deployment/postgres -- psql -U postgres -d daily_tracker
```

---

## Features Verified

* Angular frontend deployment
* FastAPI backend deployment
* PostgreSQL deployment
* Persistent Volume Claims
* JWT Authentication
* Task CRUD
* Activity Summary APIs
* Ingress Routing
* Frontend ↔ Backend communication
* Backend ↔ Database communication

---

## Learning Outcomes

This project demonstrates:

* Docker containerization
* Kubernetes Deployments
* ReplicaSets
* Services
* Persistent Storage
* Ingress Controllers
* Authentication with JWT
* Multi-tier application deployment
* Kubernetes troubleshooting and debugging

---

## Future Improvements

* ConfigMaps
* Secrets
* Readiness Probes
* Liveness Probes
* Resource Requests & Limits
* Horizontal Pod Autoscaler
* CI/CD Deployment Pipeline
* Cloud Deployment (AWS/GCP/Azure)

```
```
