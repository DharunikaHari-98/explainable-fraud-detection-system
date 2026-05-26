# Explainable Real-Time Fraud Detection System

An end-to-end machine learning fraud detection system that compares rule-based fraud detection with Logistic Regression, Random Forest, and XGBoost models for real-time transaction analysis.

---

## Tech Stack

- Python
- scikit-learn
- XGBoost
- SMOTE
- FastAPI
- React
- Recharts
- Axios

---

## Dataset

Kaggle Credit Card Fraud Detection Dataset.

- Total transactions: 284,807
- Fraud transactions: 492
- Legitimate transactions: 284,315
- Highly imbalanced fraud dataset

---

## Features

- Real-time fraud prediction
- Rule-based vs ML model comparison
- Fraud probability scoring
- React visualization dashboard
- REST API endpoints using FastAPI
- Model metrics analysis
- Confusion matrix and ROC curve generation
- Imbalanced dataset handling using SMOTE
- Research-oriented experiment tracking

---

## Models Evaluated

1. Logistic Regression
2. Random Forest
3. XGBoost

---

## Model Results

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9734 | 0.0563 | 0.9184 | 0.1061 | 0.9700 |
| Random Forest | 0.9995 | 0.8710 | 0.8265 | 0.8482 | 0.9731 |
| XGBoost | 0.9944 | 0.2208 | 0.8878 | 0.3537 | 0.9743 |

---

## Key Learning

Accuracy alone is misleading for fraud detection because the dataset is highly imbalanced.

Recall, Precision, F1-score, and ROC-AUC are more meaningful metrics for evaluating rare fraud detection systems.

Random Forest achieved the best overall balance between fraud detection capability and false positive reduction.

---

## Research Artifacts

This project includes research-oriented documentation and evaluation evidence:

```txt
research/
├── notes.md
├── results.md
└── images/
```

Research artifacts include:

- Experimental observations
- Model comparison results
- Confusion matrix visualizations
- ROC curve visualizations
- Research notes and findings

---

## How to Run Backend

```bash
python ml/train.py
python ml/evaluate.py
uvicorn api.main:app --reload
```

Backend API Docs:

```txt
http://127.0.0.1:8000/docs
```

---

## How to Run Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```txt
http://localhost:5173
```

---

## System Architecture

```txt
Transaction Input
        ↓
Data Preprocessing + SMOTE
        ↓
Machine Learning Models
(Logistic Regression / Random Forest / XGBoost)
        ↓
FastAPI Backend
        ↓
React Dashboard
        ↓
Prediction + Metrics Visualization
```

---

## Research Concepts Demonstrated

- Fraud detection using machine learning
- Imbalanced classification handling
- SMOTE oversampling
- Comparative model evaluation
- Precision vs Recall tradeoff
- ROC-AUC analysis
- Real-time ML inference APIs
- ML experiment visualization

---

## Future Improvements

- SHAP/LIME explainability integration
- Deep learning fraud detection models
- Streaming transaction analysis
- Docker deployment
- Cloud deployment
- Real-time Kafka pipeline
- User authentication and audit logging

---

## Learning Outcome

This project demonstrates practical machine learning engineering concepts including fraud detection, imbalanced data handling, model evaluation, API deployment, and research-oriented experimentation workflows.
