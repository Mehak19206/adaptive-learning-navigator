import os
import requests
from openai import OpenAI

BASE_URL = os.environ.get("ENV_BASE_URL", "http://localhost:7860")
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

ACTIONS = ["easy", "medium", "hard", "revise", "skip"]

TASKS = [
    {"id": "task_easy",   "difficulty": "easy",   "target": 50},
    {"id": "task_medium", "difficulty": "medium",  "target": 75},
    {"id": "task_hard",   "difficulty": "hard",    "target": 100},
]

def run_task(task: dict):
    obs = requests.post(f"{BASE_URL}/reset").json()
    done = False
    steps = 0
    total_reward = 0.0

    while not done and steps < 20:
        prompt = (
            f"You are an RL agent optimizing a study plan. "
            f"Current knowledge: {obs['knowledge']:.1f}, "
            f"time spent: {obs['time_spent']:.1f}. "
            f"Target knowledge: {task['target']}. "
            f"Choose one action from: {ACTIONS}. "
            f"Reply with exactly one action word only."
        )
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10,
        )
        action = response.choices[0].message.content.strip().lower()
        if action not in ACTIONS:
            action = "medium"

        result = requests.post(f"{BASE_URL}/step", json={"action": action}).json()
        obs = result["observation"]
        total_reward += result["reward"]
        done = result["done"]
        steps += 1

    score = min(obs["knowledge"] / task["target"], 1.0)
    return round(score, 3), round(total_reward, 3)

if __name__ == "__main__":
    print("Running baseline inference on all 3 tasks...\n")
    total_score = 0.0
    for task in TASKS:
        score, reward = run_task(task)
        total_score += score
        print(f"Task: {task['id']:15s} | Difficulty: {task['difficulty']:6s} | Score: {score:.3f} | Total Reward: {reward:.3f}")
    print(f"\nAverage score: {total_score / len(TASKS):.3f}")
