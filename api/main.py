import json
import joblib
import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


MODEL_DIR = "ml/models"

app = FastAPI(title="Fraud Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Fraud Detection API is running",
        "docs": "/docs"
    }

logistic_model = joblib.load(f"{MODEL_DIR}/logistic_model.pkl")
random_forest_model = joblib.load(f"{MODEL_DIR}/random_forest_model.pkl")
xgboost_model = joblib.load(f"{MODEL_DIR}/xgboost_model.pkl")
scaler = joblib.load(f"{MODEL_DIR}/scaler.pkl")


class TransactionInput(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "models_loaded": True
    }


@app.get("/metrics")
def get_metrics():
    with open(f"{MODEL_DIR}/metrics.json", "r") as file:
        metrics = json.load(file)
    return metrics


@app.post("/predict")
def predict_transaction(transaction: TransactionInput):
    data = transaction.dict()

    amount_scaled = scaler.transform([[data["Amount"]]])[0][0]
    data["Amount"] = amount_scaled

    feature_order = [f"V{i}" for i in range(1, 29)] + ["Amount"]
    input_df = pd.DataFrame([[data[col] for col in feature_order]], columns=feature_order)

    models = {
        "Logistic Regression": logistic_model,
        "Random Forest": random_forest_model,
        "XGBoost": xgboost_model
    }

    result = {}

    for name, model in models.items():
        prediction = int(model.predict(input_df)[0])
        probability = float(model.predict_proba(input_df)[0][1])

        result[name] = {
            "prediction": "FRAUD" if prediction == 1 else "LEGITIMATE",
            "fraud_probability": round(probability, 4)
        }

    fraud_votes = sum(1 for model_result in result.values() if model_result["prediction"] == "FRAUD")

    final_decision = "FRAUD" if fraud_votes >= 2 else "LEGITIMATE"

    return {
        "final_decision": final_decision,
        "fraud_votes": fraud_votes,
        "model_results": result
    }
