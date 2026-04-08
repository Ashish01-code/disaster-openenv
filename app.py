from fastapi import FastAPI
from pydantic import BaseModel
from openenv_wrapper import OpenEnvWrapper

app = FastAPI()

env = OpenEnvWrapper()

# -------- REQUEST MODELS --------
class ActionRequest(BaseModel):
    actions: list

# -------- ENDPOINTS --------

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    state = env.reset()
    return state

@app.post("/step")
def step(action: ActionRequest):
    state, reward, done, info = env.step(action.actions)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def get_state():
    return env.state()
