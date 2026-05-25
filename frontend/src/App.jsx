import { useState } from "react";
import axios from "axios";
import MetricsChart from "./components/MetricsChart";
import PredictionForm from "./components/PredictionForm";
import ExplanationBox from "./components/ExplanationBox";

function App() {
  const [result, setResult] = useState(null);

  const sampleData = {
    V1: -1.359807, V2: -0.072781, V3: 2.536347, V4: 1.378155,
    V5: -0.338321, V6: 0.462388, V7: 0.239599, V8: 0.098698,
    V9: 0.363787, V10: 0.090794, V11: -0.5516, V12: -0.617801,
    V13: -0.99139, V14: -0.311169, V15: 1.468177, V16: -0.470401,
    V17: 0.207971, V18: 0.025791, V19: 0.403993, V20: 0.251412,
    V21: -0.018307, V22: 0.277838, V23: -0.110474, V24: 0.066928,
    V25: 0.128539, V26: -0.189115, V27: 0.133558, V28: -0.021053,
    Amount: 149.62
  };

  const testPrediction = async () => {
    const response = await axios.post("http://127.0.0.1:8000/predict", sampleData);
    setResult(response.data);
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: "#0f172a",
      color: "white",
      padding: "40px",
      fontFamily: "Arial"
    }}>
      <h1 style={{ fontSize: "42px", textAlign: "center" }}>
        Explainable Fraud Detection System
      </h1>

      <p style={{ textAlign: "center", color: "#cbd5e1" }}>
        ML-powered real-time transaction fraud detection using Logistic Regression,
        Random Forest, and XGBoost.
      </p>
<div style={{
  display: "grid",
  gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
  gap: "20px",
  maxWidth: "1000px",
  margin: "30px auto"
}}>
  <div style={{ background: "#1e293b", padding: "20px", borderRadius: "14px" }}>
    <h3>Dataset</h3>
    <p>284,807 transactions</p>
  </div>

  <div style={{ background: "#1e293b", padding: "20px", borderRadius: "14px" }}>
    <h3>Fraud Cases</h3>
    <p>492 fraud transactions</p>
  </div>

  <div style={{ background: "#1e293b", padding: "20px", borderRadius: "14px" }}>
    <h3>Best Model</h3>
    <p>Random Forest</p>
  </div>

  <div style={{ background: "#1e293b", padding: "20px", borderRadius: "14px" }}>
    <h3>Best F1-Score</h3>
    <p>0.8482</p>
  </div>
</div>
      <div style={{
        maxWidth: "900px",
        margin: "30px auto",
        background: "#1e293b",
        padding: "25px",
        borderRadius: "16px"
      }}>
        <h2>Real-Time Transaction Prediction</h2>

        <button
          onClick={testPrediction}
          style={{
            padding: "12px 20px",
            borderRadius: "8px",
            border: "none",
            cursor: "pointer",
            fontWeight: "bold"
          }}
        >
          Test Sample Transaction
        </button>

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

            <p>Fraud Votes: {result.fraud_votes}/3 models</p>

            {Object.entries(result.model_results).map(([model, data]) => (
              <div key={model} style={{
                background: "#334155",
                padding: "15px",
                marginTop: "12px",
                borderRadius: "10px"
              }}>
                <strong>{model}</strong>
                <p>Prediction: {data.prediction}</p>
                <p>Fraud Probability: {(data.fraud_probability * 100).toFixed(2)}%</p>
              </div>
            ))}
          </div>
        )}
      </div>

      <div style={{
        maxWidth: "1000px",
        margin: "30px auto",
        background: "#1e293b",
        padding: "25px",
        borderRadius: "16px"
      }}>
        <MetricsChart />
        <PredictionForm />
        <ExplanationBox />
      </div>
    </div>
  );
}

export default App;