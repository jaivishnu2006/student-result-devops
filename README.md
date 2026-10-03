# DevOps-Based Student Result Management System

## Project Title
DevOps-Based Student Result Management System with Automated CI/CD using Jenkins and Docker

## Run locally

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open: http://127.0.0.1:5000

## Run tests

```powershell
pytest
```

## Run with Docker

```powershell
docker build -t student-result-devops .
docker run -d --name student-result-devops-container -p 5000:5000 student-result-devops
```

Open: http://localhost:5000

## Run with Docker Compose

```powershell
docker compose up --build
```

## DevOps flow

GitHub -> Jenkins -> Install Dependencies -> Test -> Docker Build -> Docker Container
