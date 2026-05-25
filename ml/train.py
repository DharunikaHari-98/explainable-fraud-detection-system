import os
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from preprocess import load_and_prepare_data


MODEL_DIR = "ml/models"


def train_models():
    os.makedirs(MODEL_DIR, exist_ok=True)

    X_train, X_test, y_train, y_test, scaler = load_and_prepare_data()

    models = {
        "logistic": LogisticRegression(max_iter=1000),
        "random_forest": RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        ),
        "xgboost": XGBClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5,
            eval_metric="logloss",
            random_state=42
        )
    }

    for name, model in models.items():
        print(f"\nTraining {name} model...")
        model.fit(X_train, y_train)

        save_path = f"{MODEL_DIR}/{name}_model.pkl"
        joblib.dump(model, save_path)

        print(f"Saved: {save_path}")

    joblib.dump(scaler, f"{MODEL_DIR}/scaler.pkl")
    print("\nScaler saved successfully")


if __name__ == "__main__":
    train_models()