from fastapi import FastAPI
from env import LearningEnv

app = FastAPI()
env = LearningEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "knowledge": obs.knowledge,
        "time_spent": obs.time_spent
    }

@app.post("/step")
def step(action: dict):
    action_value = action.get("action")  # extract actual action

    state, reward, done, _ = env.step(action_value)

    return {
        "observation": {
            "knowledge": state.knowledge,
            "time_spent": state.time_spent
        },
        "reward": reward.value,
        "done": done,
        "info": {}
    }

@app.get("/state")
def state():
    s = env.state()
    return {
        "knowledge": s.knowledge,
        "time_spent": s.time_spent
    }
