from agent.gemini_client import call_gemini

def explain_solution(problem: str, solution: str):
    prompt = f"""
Explain the solution clearly.

Problem:
{problem}

Solution:
{solution}

Explain approach and complexity briefly.
"""
    return call_gemini(prompt)
