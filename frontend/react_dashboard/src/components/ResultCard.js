import React from "react";

const ResultCard = ({ result }) => {
  if (!result) return null;

  return (
    <div className="card">
      <h3>Classification Result</h3>

      <p>
        <b>Category:</b> {result.category || "Not Classified"}
      </p>

      <h4>Suggested Reply</h4>

      <textarea
        rows="5"
        cols="60"
        value={result.reply || ""}
        readOnly
      />
    </div>
  );
};

export default ResultCard;
