import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h2>AI Email Assistant</h2>
      <div>
        <Link to="/">Home</Link>
        <Link to="/history">History</Link>
      </div>
    </nav>
  );
};

export default Navbar;
