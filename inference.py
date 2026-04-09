import os
from openai import OpenAI
from tasks import easy, medium, hard

# ✅ MUST use EXACT env variables
client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("API_KEY")
)

def call_llm():
    try:
        response = client.chat.completions.create(
            model=os.environ.get("MODEL_NAME"),
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        return response.choices[0].message.content
    except Exception as e:
        print("[STEP] API_ERROR:", str(e))
        return "error"


def log_start():
    print("[START] Running inference")

def log_step(task_name, score):
    print(f"[STEP] Task={task_name} Score={score}")

def log_end():
    print("[END] Inference complete")


def main():
    log_start()

    call_llm()

    try:
        e = easy()
        log_step("easy", e)

        call_llm()

        m = medium()
        log_step("medium", m)

        call_llm()

        h = hard()
        log_step("hard", h)

    except Exception as e:
        print("[STEP] ERROR:", str(e))

    log_end()


if __name__ == "__main__":
    main()
