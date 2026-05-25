import { useEffect, useState } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer
} from "recharts";

function MetricsChart() {
  const [metrics, setMetrics] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/metrics")
      .then((response) => {
        const formatted = Object.entries(response.data).map(([model, values]) => ({
          model,
          Precision: values.precision,
          Recall: values.recall,
          F1: values.f1_score,
          AUC: values.roc_auc
        }));

        setMetrics(formatted);
      })
      .catch((error) => console.error(error));
  }, []);

  return (
    <div style={{ marginTop: "40px", width: "100%", height: "350px" }}>
      <h2>Model Performance Comparison</h2>

      <ResponsiveContainer>
        <BarChart data={metrics}>
          <XAxis dataKey="model" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="Precision" />
          <Bar dataKey="Recall" />
          <Bar dataKey="F1" />
          <Bar dataKey="AUC" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default MetricsChart;