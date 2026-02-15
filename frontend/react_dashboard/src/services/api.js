const API_BASE_URL = "http://localhost:5000";

export const checkAuthStatus = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/status`);
    return await response.json();
  } catch (error) {
    return { connected: false };
  }
};

export const connectGmail = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/connect`);
    return await response.json();
  } catch (error) {
    return { status: "error", message: error.message };
  }
};

export const fetchEmails = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/emails`);
    if (!response.ok) {
      const errData = await response.json();
      throw new Error(errData.error || "Failed to fetch emails");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching emails:", error);
    throw error;
  }
};

export const classifyEmail = async (emailText) => {
  try {
    const response = await fetch(`${API_BASE_URL}/classify`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: emailText }),
    });
    if (!response.ok) throw new Error("Failed to classify email");
    return await response.json();
  } catch (error) {
    console.error("Error classifying email:", error);
    return { label: "error" };
  }
};
