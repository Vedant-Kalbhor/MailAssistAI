import requests
import json

USE_LOCAL_LLAMA = True   # Change to False if you want Gemini

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_reply(email_text):
    """
    AI-powered reply generator using:
    - Local Llama2 (via Ollama)
    - OR Gemini API as fallback
    """

    if USE_LOCAL_LLAMA:
        return generate_reply_llama(email_text)
    else:
        return generate_reply_gemini(email_text)



def generate_reply_llama(email_text):

    prompt = f"""
You are an intelligent professional email assistant.

Generate a polite, professional, concise email reply to this message:

Email:
{email_text}

Rules:
- Keep it short
- Professional tone
- No emojis
- Only give the reply text
"""

    payload = {
        "model": "llama2:latest",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        result = response.json()

        return result.get("response", "Unable to generate reply at the moment.")

    except Exception as e:
        return f"Error generating reply: {str(e)}"



# OPTIONAL – Gemini Version (if you ever want)

import os
import google.generativeai as genai

def generate_reply_gemini(email_text):

    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        model = genai.GenerativeModel("gemini-pro")

        prompt = f"""
Generate a professional email reply to:

{email_text}

Keep it concise and formal.
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"
