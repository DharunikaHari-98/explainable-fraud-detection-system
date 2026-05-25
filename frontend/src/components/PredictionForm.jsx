import { useState } from "react";
import axios from "axios";

function PredictionForm() {
  const [amount, setAmount] = useState(100);
  const [result, setResult] = useState(null);

  const predict = async () => {
    const transaction = { Amount: Number(amount) };

    for (let i = 1; i <= 28; i++) {
      transaction[`V${i}`] = 0;
    }

    const response = await axios.post(
      "http://127.0.0.1:8000/predict",
      transaction
    );

    setResult(response.data);
  };

  return (
    <div style={{ marginBottom: "30px" }}>
      <h2>Manual Transaction Check</h2>

      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        placeholder="Enter Amount"
        style={{
          padding: "12px",
          marginRight: "10px",
          borderRadius: "8px",
          border: "none"
        }}
      />

      <button onClick={predict}>Predict</button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>
            Final Decision:
            <span style={{
              color: result.final_decision === "FRAUD" ? "#f87171" : "#4ade80",
              marginLeft: "10px"
            }}>
              {result.final_decision}
            </span>
          </h3>

          <p>ML Fraud Votes: {result.fraud_votes}/3</p>
          <p>Rule-Based Prediction: {result.rule_based_prediction}</p>
          <p>Rule-Based Score: {result.rule_based_score}/3</p>

          {Object.entries(result.model_results).map(([model, data]) => (
            <div
              key={model}
              style={{
                background: "#334155",
                padding: "12px",
                borderRadius: "10px",
                marginTop: "10px"
              }}
            >
              <strong>{model}</strong>
              <p>Prediction: {data.prediction}</p>
              <p>Fraud Probability: {(data.fraud_probability * 100).toFixed(2)}%</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default PredictionForm;