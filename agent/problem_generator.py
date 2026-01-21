from agent.gemini_client import call_gemini

def generate_problem():
    prompt = """
Generate ONE unique DSA problem.

Rules:
- Difficulty: Easy to Medium
- Topic: Arrays / Strings / Stack / Hashing / Two pointers
- Provide:
  1. Title
  2. Problem statement
  3. Constraints
  4. Example

Avoid very famous problems.
"""
    return call_gemini(prompt)
