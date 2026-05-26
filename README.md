# Explainable Real-Time Fraud Detection System

An end-to-end machine learning fraud detection system that compares rule-based fraud detection with Logistic Regression, Random Forest, and XGBoost models.

## Tech Stack

- Python
- scikit-learn
- XGBoost
- SMOTE
- FastAPI
- React
- Recharts
- Axios

## Dataset

Kaggle Credit Card Fraud Detection Dataset.

- Total transactions: 284,807
- Fraud transactions: 492
- Legitimate transactions: 284,315

## Model Results

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9734 | 0.0563 | 0.9184 | 0.1061 | 0.9700 |
| Random Forest | 0.9995 | 0.8710 | 0.8265 | 0.8482 | 0.9731 |
| XGBoost | 0.9944 | 0.2208 | 0.8878 | 0.3537 | 0.9743 |

## Key Learning

Accuracy alone is misleading for fraud detection because the dataset is highly imbalanced. Recall and F1-score are more meaningful for detecting rare fraud cases.

## Features

- Real-time fraud prediction
- Rule-based vs ML comparison
- React visualization dashboard
- REST API endpoints
- Model metrics analysis
- Fraud probability scoring
- Imbalanced dataset handling using SMOTE

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
