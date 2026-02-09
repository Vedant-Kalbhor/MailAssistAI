import React, { useState } from "react";
import { classifyEmail, generateReply } from "../services/api";

const EmailInput = ({ setResult }) => {
  const [email, setEmail] = useState("");

  const handleSubmit = async () => {
    try {
      const classification = await classifyEmail(email);
      const reply = await generateReply(email);

      setResult({
        category: classification.data.label,
        reply: reply.data.reply,
        text: email
      });

    } catch (err) {
      alert("Error connecting backend");
    }
  };

  return (
    <div>
      <textarea
        rows="8"
        cols="60"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Paste email text here..."
      />

      <br />

      <button onClick={handleSubmit}>Analyze Email</button>
    </div>
  );
};

export default EmailInput;
