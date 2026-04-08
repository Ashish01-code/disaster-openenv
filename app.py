from fastapi import FastAPI
from tasks import easy, medium, hard

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/run")
def run_tasks():
    return {
        "easy": easy(),
        "medium": medium(),
        "hard": hard()
    }