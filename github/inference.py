import requests

BASE_URL = "http://localhost:8000"

def run():
    requests.post(f"{BASE_URL}/reset")

    total_reward = 0

    for _ in range(20):
        action = {"action": "medium"}
        res = requests.post(f"{BASE_URL}/step", json=action)
        data = res.json()

        total_reward += data["reward"]

        if data["done"]:
            break

    print("Total Reward:", total_reward)

if __name__ == "__main__":
    run()