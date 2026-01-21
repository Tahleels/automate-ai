import os
import random
import subprocess
from datetime import date

from agent.problem_generator import generate_problem
from agent.solver import solve_problem
from agent.explainer import explain_solution

def decide_commit_count():
    r = random.random()
    if r < 0.70:
        return 1
    elif r < 0.85:
        return 2
    elif r < 0.95:
        return 3
    else:
        return 4

today = date.today().isoformat()
commit_count = decide_commit_count()
base_dir = f"automate/{today}"
os.makedirs(base_dir, exist_ok=True)

for i in range(1, commit_count + 1):
    try:
        problem = generate_problem()
        solution = solve_problem(problem)
        explanation = explain_solution(problem, solution)

        with open(f"{base_dir}/problem_{i}.md", "w") as f:
            f.write(problem)

        with open(f"{base_dir}/solution_{i}.py", "w") as f:
            f.write(solution)

        with open(f"{base_dir}/explanation_{i}.md", "w") as f:
            f.write(explanation)

        with open("PROGRESS.md", "a") as f:
            f.write(f"\n### {today} – Problem {i}\n")

    except Exception as e:
        with open("PROGRESS.md", "a") as f:
            f.write(f"\n### {today} – ERROR\n{str(e)}\n")
        raise


    subprocess.run(["git", "add", "."])
    subprocess.run([
        "git", "commit",
        "-m",
        f"Daily DSA {today} #{i}"
    ])

# Final heartbeat (streak insurance)
with open("PROGRESS.md", "a") as f:
    f.write(f"\nHeartbeat update: {today}\n")
