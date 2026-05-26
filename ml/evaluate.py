import json
import os
import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
    RocCurveDisplay
)

from preprocess import load_and_prepare_data


MODEL_DIR = "ml/models"
IMAGE_DIR = "research/images"


def safe_file_name(name):
    return name.lower().replace(" ", "_")


def evaluate_models():
    os.makedirs(IMAGE_DIR, exist_ok=True)

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

        cm = confusion_matrix(y_test, y_pred)

        results[model_name] = {
            "accuracy": round(accuracy_score(y_test, y_pred), 4),
            "precision": round(precision_score(y_test, y_pred), 4),
            "recall": round(recall_score(y_test, y_pred), 4),
            "f1_score": round(f1_score(y_test, y_pred), 4),
            "roc_auc": round(roc_auc_score(y_test, y_prob), 4),
            "confusion_matrix": cm.tolist()
        }

        print(classification_report(y_test, y_pred))

        file_key = safe_file_name(model_name)

        # Save confusion matrix image
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.title(f"{model_name} - Confusion Matrix")
        plt.savefig(f"{IMAGE_DIR}/{file_key}_confusion_matrix.png")
        plt.close()

        # Save ROC curve image
        RocCurveDisplay.from_predictions(y_test, y_prob)
        plt.title(f"{model_name} - ROC Curve")
        plt.savefig(f"{IMAGE_DIR}/{file_key}_roc_curve.png")
        plt.close()

    with open(f"{MODEL_DIR}/metrics.json", "w") as file:
        json.dump(results, file, indent=4)

    print("\nMetrics saved to ml/models/metrics.json")
    print("Research images saved to research/images")


if __name__ == "__main__":
    evaluate_models()