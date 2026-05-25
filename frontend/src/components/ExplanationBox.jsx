function ExplanationBox() {
  return (
    <div style={{
      background: "#334155",
      padding: "18px",
      borderRadius: "12px",
      marginTop: "20px"
    }}>
      <h3>How this system works</h3>

      <p>
        This system first compares a simple rule-based fraud detector with
        machine learning models.
      </p>

      <ul>
        <li><strong>Logistic Regression:</strong> simple baseline model</li>
        <li><strong>Random Forest:</strong> best balanced model in current results</li>
        <li><strong>XGBoost:</strong> strong boosting model with high recall</li>
      </ul>

      <p>
        For fraud detection, recall is very important because missing a fraud
        transaction is more costly than wrongly flagging one transaction.
      </p>
    </div>
  );
}

export default ExplanationBox;