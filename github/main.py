from fastapi import FastAPI
from env import LearningEnv

app = FastAPI()
env = LearningEnv()

@app.post("/reset")
def reset():
    return env.reset().dict()

@app.post("/step")
def step(action: dict):
    state, reward, done, _ = env.step(action)
    return {
        "observation": state.dict(),
        "reward": reward.value,
        "done": done,
        "info": {}
    }

@app.get("/state")
def state():
    return env.state().dict()