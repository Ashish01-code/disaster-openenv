import os
from tasks import easy, medium, hard

API_BASE_URL = os.getenv("API_BASE_URL", "dummy")
MODEL_NAME = os.getenv("MODEL_NAME", "dummy")
HF_TOKEN = os.getenv("HF_TOKEN", "dummy")

def log_start():
    print("[START] Running inference")

def log_step(task_name, score):
    print(f"[STEP] Task={task_name} Score={score}")

def log_end():
    print("[END] Inference complete")

def main():
    log_start()

    try:
        e = easy()
        log_step("easy", e)

        m = medium()
        log_step("medium", m)

        h = hard()
        log_step("hard", h)

    except Exception as e:
        print("[STEP] ERROR:", str(e))

    log_end()

if __name__ == "__main__":
    main()