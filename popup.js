document.getElementById("checkSpam").addEventListener("click", async function () {
    const message = document.getElementById("message").value;
    const resultDiv = document.getElementById("result");
    const button = document.getElementById("checkSpam");

    if (message.trim() === "") {
        resultDiv.innerHTML = '<span style="color: #94a3b8; font-size: 13px;">Please enter content</span>';
        return;
    }

    button.disabled = true;
    button.innerText = "Analyzing...";
    resultDiv.innerHTML = "";

    try {
        const response = await fetch("http://localhost:5000/classify", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email: message })
        });

        if (!response.ok) throw new Error("Server error");

        const data = await response.json();
        
        if (data.label === "spam") {
            resultDiv.innerHTML = '<span class="status-badge spam">🚨 High Risk: SPAM</span>';
        } else {
            resultDiv.innerHTML = '<span class="status-badge not_spam">✅ Low Risk: SAFE</span>';
        }

    } catch (error) {
        console.error("Error:", error);
        resultDiv.innerHTML = '<span style="color: #f59e0b; font-size: 13px;">Connection Error</span>';
    } finally {
        button.disabled = false;
        button.innerText = "Analyze Message";
    }
});
