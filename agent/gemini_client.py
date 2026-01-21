import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def call_gemini(prompt: str) -> str:
    response = requests.post(
        f"{URL}?key={API_KEY}",
        json={
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        },
        timeout=30
    )
    response.raise_for_status()
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
