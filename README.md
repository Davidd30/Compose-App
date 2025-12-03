# Compose-App (Docker Test)

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

> A minimal, containerized application designed specifically for testing Docker and Docker Compose configurations.

![Browser Preview]('/Screenshots/Screenshot 2025-11-19 at 2.47.42 AM.png')

## 🧪 About This Project
This project serves as a sandbox to demonstrate and verify a containerized workflow. It runs a lightweight Flask server that outputs environment details to the web browser. 

It is designed to confirm:
1.  **Containerization:** The app runs successfully inside a Docker container.
2.  **Port Mapping:** The internal port 5000 is correctly exposed to the host.
3.  **Volume Mounting:** Local code changes are reflected instantly inside the container.

## 🐳 Docker Configuration
The core of this project is the configuration of the `Dockerfile` and `docker-compose.yml`.

### 1. The Dockerfile
The `Dockerfile` contains the instructions to build the image efficiently.

```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir Flask==2.3.3

COPY app/ /app/

EXPOSE 5000

CMD ["python","app.py"]
```

**Breakdown:**
* **`FROM python:3.11-slim`**: We use the "slim" version of the official Python image to keep the container size small and efficient for testing.
* **`WORKDIR /app`**: Sets the working directory inside the container.
* **`RUN pip install ...`**: Installs Flask. We use `--no-cache-dir` to prevent the image from storing unnecessary cache files, keeping it lightweight.
* **`COPY app/ /app/`**: Copies the source code from the local host into the container image.
* **`CMD ["python","app.py"]`**: The command that runs automatically when the container starts.

### 2. Docker Compose
The `docker-compose.yml` simplifies running the container by defining the services, networks, and volumes in a single file.

```yaml
services:
  flask_app:
    build: .
    container_name: flask_compose_app
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
    volumes:
      - ./app:/app
    restart: unless-stopped
```

**Key Features Enabled:**
* **Volume Mapping (`volumes`)**: The line `- ./app:/app` is crucial. It maps your local `./app` folder to the container's `/app` folder. This means if you edit `app.py` on your computer, the container sees the change immediately (hot-reloading).
* **Environment Variables (`environment`)**: We inject `FLASK_ENV=development` directly into the container configuration, which can be accessed by the Python script.
* **Port Forwarding (`ports`)**: Maps port `5000` on your local machine to port `5000` inside the container.

## 📸 Visual Verification
Screenshots confirming the build process and container status:

| Build Process | Container Status |
|:---:|:---:|
| <img src="'/Screenshots/Screenshot 2025-11-19 at 2.48.18 AM.png'" width="400"> | <img src="'/Screenshots/Screenshot 2025-11-19 at 2.46.53 AM.png'" width="400"> |
| *Docker building layers successfully* | *Container `flask_compose_app` up and running* | 

## 🚀 How to Test
1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Davidd30/Compose-App.git](https://github.com/Davidd30/Compose-App.git)
    cd Compose-App
    ```

2.  **Run with Docker Compose**
    Start the application in detached mode (background):
    ```bash
    docker compose up -d
    ```

3.  **Verify Application**
    Open your browser and navigate to [http://localhost:5000](http://localhost:5000). 
    
    You should see the message: *"Hello from the Containerized Flask App!"*

4.  **Stop the Application**
    To stop and remove the containers:
    ```bash
    docker compose down
    ```

## 📂 File Overview
* **`app/app.py`**: The Python entry point. It sets up a simple Flask route that returns HTML.
* **`Dockerfile`**: Instructions for building the Python environment.
* **`docker-compose.yml`**: Configuration for orchestrating the service.
# Compose-App
