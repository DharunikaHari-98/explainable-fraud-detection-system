import json
import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

from preprocess import load_and_prepare_data


MODEL_DIR = "ml/models"


def evaluate_models():
    _, X_test, _, y_test, _ = load_and_prepare_data()

    model_files = {
        "Logistic Regression": "logistic_model.pkl",
        "Random Forest": "random_forest_model.pkl",
        "XGBoost": "xgboost_model.pkl"
    }

    results = {}

    for model_name, file_name in model_files.items():
        print(f"\nEvaluating {model_name}...")

        model = joblib.load(f"{MODEL_DIR}/{file_name}")

        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        results[model_name] = {
            "accuracy": round(accuracy_score(y_test, y_pred), 4),
            "precision": round(precision_score(y_test, y_pred), 4),
            "recall": round(recall_score(y_test, y_pred), 4),
            "f1_score": round(f1_score(y_test, y_pred), 4),
            "roc_auc": round(roc_auc_score(y_test, y_prob), 4),
            "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
        }

        print(classification_report(y_test, y_pred))

    with open(f"{MODEL_DIR}/metrics.json", "w") as file:
        json.dump(results, file, indent=4)

    print("\nMetrics saved to ml/models/metrics.json")


if __name__ == "__main__":
    evaluate_models()