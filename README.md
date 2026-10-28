# Laptop Price Prediction — MLOps Project

An end-to-end Machine Learning Operations (MLOps) project that predicts laptop prices using a machine learning model, FastAPI, Docker, and GitHub Actions.

## 🚀 Features

- Laptop price prediction using a Random Forest Regressor
- REST API built with FastAPI
- Interactive API documentation using Swagger UI
- Docker containerization
- Automated API testing with Pytest
- Continuous Integration using GitHub Actions

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Machine Learning:** Scikit-learn
- **Model Serialization:** Joblib
- **API:** FastAPI and Uvicorn
- **Testing:** Pytest and HTTPX
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

## 📁 Project Structure

```text
laptop-price-mlops/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_main.py
├── main.py
├── model.joblib
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## ⚙️ Installation and Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/vidhigoyal28/laptop-price-mlops.git
cd laptop-price-mlops
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn main:app --reload
```

Open the interactive documentation:

http://localhost:8000/docs

## 🐳 Run with Docker

### Build the image

```bash
docker build -t laptop-price-api .
```

### Start the container

```bash
docker run --name laptop-price-container -p 8000:8000 laptop-price-api
```

Access the endpoints:

- API documentation: http://localhost:8000/docs
- Health check: http://localhost:8000/health

## 🔮 Example Prediction

Send a `POST` request to `/predict` with the following JSON:

```json
{
  "Brand": "Asus",
  "Processor_Speed": 3.8,
  "RAM_Size": 16,
  "Storage_Capacity": 512,
  "Screen_Size": 15.6,
  "Weight": 2.5
}
```

The API returns the laptop price predicted by the trained model.

## 🧪 Run Automated Tests

```bash
python -m pytest tests/test_main.py -v
```

## 🔄 Continuous Integration

GitHub Actions automatically:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Runs automated API tests.
5. Builds the Docker image.

The workflow runs on pushes to the `main` branch and pull requests targeting `main`.

## 📌 Project Highlights

This project demonstrates a complete model-serving workflow, including model serialization, API development, containerization, automated testing, and continuous integration.

## 🔗 Repository

[GitHub — Laptop Price Prediction MLOps](https://github.com/vidhigoyal28/laptop-price-mlops)
