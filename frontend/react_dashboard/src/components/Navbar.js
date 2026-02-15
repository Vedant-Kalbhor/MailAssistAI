import React from "react";
import { Link, useLocation } from "react-router-dom";
import "./Navbar.css";

const Navbar = () => {
  const location = useLocation();

  return (
    <nav className="navbar glass-effect">
      <div className="nav-container">
        <Link to="/" className="nav-logo">
          <span className="logo-icon">🛡️</span>
          <span className="logo-text">MailAssist AI</span>
        </Link>
        <ul className="nav-links">
          <li>
            <Link to="/" className={location.pathname === "/" ? "active" : ""}>
              Dashboard
            </Link>
          </li>
          <li>
            <Link to="/history" className={location.pathname === "/history" ? "active" : ""}>
              History
            </Link>
          </li>
        </ul>
        <div className="nav-status">
          <span className="status-dot"></span>
          Connected
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
