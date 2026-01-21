from agent.gemini_client import call_gemini

def solve_problem(problem_text: str):
    prompt = f"""
Solve the following DSA problem in Python.

{problem_text}

Rules:
- Clean, readable code
- Handle edge cases
- Add comments
- Mention time & space complexity
"""
    return call_gemini(prompt)
