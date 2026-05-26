# Research Notes

## Title
Explainable Real-Time Fraud Detection Using Machine Learning

## Problem Statement
Credit card fraud detection is challenging because fraudulent transactions are rare compared to legitimate transactions. This creates a highly imbalanced classification problem where accuracy alone can be misleading.

## Objective
The objective of this project is to build and evaluate a real-time fraud detection system using machine learning models and compare their performance against a simple rule-based baseline.

## Dataset
Kaggle Credit Card Fraud Detection Dataset

- Total transactions: 284,807
- Fraud transactions: 492
- Legitimate transactions: 284,315

## Models Used
- Logistic Regression
- Random Forest
- XGBoost

## Techniques Used
- StandardScaler for amount normalization
- SMOTE for handling class imbalance
- Precision, Recall, F1-score, and ROC-AUC for evaluation
- FastAPI for real-time model serving
- React dashboard for visualization

## Research Question
Which machine learning model provides the best balance between fraud detection recall and false positive control on highly imbalanced transaction data?

## Expected Contribution
This project compares multiple machine learning approaches for fraud detection and demonstrates how model evaluation metrics can be used to select a practical fraud detection model.
