import React, { useState } from "react";
import { classifyEmail } from "../services/api";
import ResultCard from "./ResultCard";

const EmailForm = () => {
  const [email, setEmail] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);

    try {
      const response = await classifyEmail(email);

      console.log("API Response:", response.data);

      setResult(response.data);
    } catch (error) {
      console.error("API Error:", error);
    }

    setLoading(false);
  };

  return (
    <div>
      <h2>AI Email Assistant</h2>

      <textarea
        rows="6"
        cols="70"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Paste your email here..."
      />

      <br />

      <button onClick={handleSubmit}>
        Analyze Email
      </button>

      {loading && <p>Analyzing...</p>}

      <ResultCard result={result} />
    </div>
  );
};

export default EmailForm;
