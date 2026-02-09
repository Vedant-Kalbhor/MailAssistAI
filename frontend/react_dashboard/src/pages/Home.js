import React, { useState } from "react";
import EmailInput from "../components/EmailInput";
import ResultCard from "../components/ResultCard";

const Home = () => {
  const [result, setResult] = useState(null);

  return (
    <div>
      <h2>Email Analyzer</h2>

      <EmailInput setResult={setResult} />

      <ResultCard result={result} />
    </div>
  );
};

export default Home;
