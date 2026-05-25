import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE


DATA_PATH = "data/creditcard.csv"


def load_and_prepare_data():
    df = pd.read_csv(DATA_PATH)

    print("Dataset loaded successfully")
    print("Shape:", df.shape)
    print("Fraud count:")
    print(df["Class"].value_counts())

    df = df.dropna()

    X = df.drop("Class", axis=1)
    y = df["Class"]

    # Scale Amount column
    scaler = StandardScaler()
    X["Amount"] = scaler.fit_transform(X[["Amount"]])

    # Drop Time column
    X = X.drop("Time", axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # SMOTE only on training data
    smote = SMOTE(random_state=42)
    X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

    print("Before SMOTE:", y_train.value_counts().to_dict())
    print("After SMOTE:", y_train_balanced.value_counts().to_dict())

    return X_train_balanced, X_test, y_train_balanced, y_test, scaler


if __name__ == "__main__":
    load_and_prepare_data()