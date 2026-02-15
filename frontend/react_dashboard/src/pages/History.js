import React from "react";

const History = () => {
  return (
    <div className="dashboard-container animate-fade-in" style={{ textAlign: 'center', paddingTop: '100px' }}>
      <div className="glass-effect" style={{ padding: '3rem', maxWidth: '600px', margin: '0 auto' }}>
        <h2 style={{ marginBottom: '1rem', fontSize: '2rem' }}>History Feature</h2>
        <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>🏗️</div>
        <p style={{ color: 'var(--text-muted)' }}>
          We're working on a feature to store and track your classification history across devices. Stay tuned!
        </p>
      </div>
    </div>
  );
};

export default History;
