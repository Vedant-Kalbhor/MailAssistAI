import React, { useState, useEffect } from "react";
import { fetchEmails, classifyEmail, checkAuthStatus, connectGmail } from "../services/api";
import "./Home.css";

const Home = () => {
  const [emails, setEmails] = useState([]);
  const [loading, setLoading] = useState(false);
  const [isConnected, setIsConnected] = useState(false);
  const [stats, setStats] = useState({ total: 0, spam: 0, safe: 0 });

  const checkConnection = async () => {
    const status = await checkAuthStatus();
    setIsConnected(status.connected);
    if (status.connected) {
      loadEmails();
    }
  };

  const handleConnect = async () => {
    setLoading(true);
    const result = await connectGmail();
    if (result.status === "success") {
      setIsConnected(true);
      loadEmails();
    } else {
      alert("Failed to connect: " + (result.message || "Unknown error"));
    }
    setLoading(false);
  };

  const loadEmails = async () => {
    setLoading(true);
    try {
      const data = await fetchEmails();
      
      if (data.error) {
         alert("Gmail Error: " + data.error);
         setLoading(false);
         return;
      }

      // Backend now handles classification, so we just set the data
      setEmails(data);
      
      const spamCount = data.filter(e => e.label === "spam").length;
      setStats({
          total: data.length,
          spam: spamCount,
          safe: data.length - spamCount
      });
    } catch (err) {
      console.error("Fetch Error:", err);
      alert("Failed to reach server. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    checkConnection();
  }, []);

  return (
    <div className="dashboard-container animate-fade-in">
      {!isConnected ? (
        <div className="connect-prompt glass-effect">
          <div className="prompt-icon">🔐</div>
          <h2>Connect Your Gmail</h2>
          <p>Grant MailAssist AI permission to analyze your inbox for potential threats.</p>
          <button className="connect-btn" onClick={handleConnect} disabled={loading}>
            {loading ? "Opening Login..." : "Connect Gmail Account"}
          </button>
        </div>
      ) : (
        <>
          <header className="dashboard-header">
            <h1>Email Security Overview</h1>
            <button className="refresh-btn" onClick={loadEmails} disabled={loading}>
              {loading ? "Refreshing..." : "🔄 Sync Now"}
            </button>
          </header>

          <div className="stats-grid">
            {/* ... stats cards ... */}
        <div className="stat-card glass-effect">
          <div className="stat-icon total">📧</div>
          <div className="stat-info">
            <span className="stat-label">Total Analyzed</span>
            <span className="stat-value">{stats.total}</span>
          </div>
        </div>
        <div className="stat-card glass-effect">
          <div className="stat-icon spam">🚨</div>
          <div className="stat-info">
            <span className="stat-label">Spam Detected</span>
            <span className="stat-value">{stats.spam}</span>
          </div>
        </div>
        <div className="stat-card glass-effect">
          <div className="stat-icon safe">✅</div>
          <div className="stat-info">
            <span className="stat-label">Safe Emails</span>
            <span className="stat-value">{stats.safe}</span>
          </div>
        </div>
      </div>

      <section className="emails-section glass-effect">
        <div className="section-header">
          <h2>Recent Messages</h2>
          <span className="count-badge">{emails.length} Found</span>
        </div>
        
        <div className="emails-list">
          {loading ? (
            <div className="loader">Analyzing Inbox...</div>
          ) : emails.length > 0 ? (
            emails.map((email) => (
              <div key={email.id} className="email-item">
                <div className={`status-indicator ${email.label}`}></div>
                <div className="email-content">
                  <div className="email-top">
                    <span className="email-sender">{email.sender}</span>
                    <span className="email-date">{new Date(email.date).toLocaleDateString()}</span>
                  </div>
                  <h3 className="email-subject">{email.subject}</h3>
                  <p className="email-snippet">{email.snippet}</p>
                </div>
                <div className={`email-label-badge ${email.label}`}>
                  {email.label.toUpperCase()}
                </div>
              </div>
            ))
          ) : (
            <div className="no-data">No emails found. Click Sync to fetch.</div>
          )}
        </div>
      </section>
        </>
      )}
    </div>
  );
};

export default Home;
