from fastapi import FastAPI
from env import LearningEnv

app = FastAPI()
env = LearningEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: dict):
    action_value = action.get("action")
    state, reward, done, _ = env.step(action_value)
    return {
        "observation": state.dict(),
        "reward": reward.value,
        "done": done,
        "info": {}
    }

@app.get("/state")
def state():
    s = env.state()
    return s.dict()
