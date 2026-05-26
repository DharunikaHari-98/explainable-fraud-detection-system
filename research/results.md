# Experimental Results

## Dataset
- Credit Card Fraud Detection Dataset
- Total Transactions: 284,807
- Fraud Cases: 492
- Highly imbalanced dataset

---

## Models Evaluated
1. Logistic Regression
2. Random Forest
3. XGBoost

---

## Evaluation Metrics
- Precision
- Recall
- F1-score
- ROC-AUC

---

## Model Performance

| Model | Precision | Recall | F1-score | ROC-AUC |
|------|------:|------:|------:|------:|
| Logistic Regression | 0.0563 | 0.9184 | 0.1061 | 0.9700 |
| Random Forest | 0.8710 | 0.8265 | 0.8482 | 0.9731 |
| XGBoost | 0.2208 | 0.8878 | 0.3537 | 0.9743 |

---

## Observations

- Random Forest achieved the best overall F1-score.
- Logistic Regression had high recall but very low precision, meaning it caught many frauds but created many false positives.
- XGBoost achieved high recall and ROC-AUC but lower precision than Random Forest.
- SMOTE helped improve minority class detection.
- Accuracy alone was misleading because the dataset was highly imbalanced.
