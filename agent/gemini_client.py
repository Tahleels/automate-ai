import os
from google import genai

# Initialize client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def call_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-1.5-flash",   # STABLE + AVAILABLE
        contents=prompt
    )
    return response.text
