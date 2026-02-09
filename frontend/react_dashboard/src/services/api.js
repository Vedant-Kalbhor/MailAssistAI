import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000"
});

export const classifyEmail = async (email) => {
  return API.post("/multi_classify", { email });
};

export const generateReply = async (email) => {
  return API.post("/generate_reply", { email });
};
