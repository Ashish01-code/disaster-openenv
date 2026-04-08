from fastapi import FastAPI
from openenv_wrapper import OpenEnvWrapper

app = FastAPI()
env = OpenEnvWrapper()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)

@app.get("/state")
def state():
    return env.state()


# ✅ IMPORTANT MAIN FUNCTION
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
if __name__ == "__main__":
    main()
