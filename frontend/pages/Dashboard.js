import React, { useState, useEffect } from "react";
import { fetchEmails } from "../services/api";

export default function Dashboard() {

  const [emails, setEmails] = useState([]);

  useEffect(() => {
    fetchEmails().then(res => setEmails(res.data));
  }, []);

  return (
    <div>
      <h2>Email Inbox</h2>
      {emails.map((e,i) => <p key={i}>{e}</p>)}
    </div>
  );
}
