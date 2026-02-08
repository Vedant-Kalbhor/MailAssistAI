import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000"
});

export const classifyEmail = (email) =>
  API.post("/multi_classify", { email });

export const generateReply = (email) =>
  API.post("/reply", { email });

export const fetchEmails = () =>
  API.get("/emails");
