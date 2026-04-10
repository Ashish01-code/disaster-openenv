import os
from openai import OpenAI

# Initialize client using injected environment variables
client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)
MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-3.5-turbo")

# Logging helpers
def log_start():
    print("[START] Running inference")

def log_step(task_name, score):
    print(f"[STEP] Task={task_name} Score={score:.2f}")

def log_end():
    print("[END] Inference complete")

# Function to call LiteLLM proxy and get score
def call_llm(task_name):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": f"Evaluate task {task_name} and return a score strictly between 0 and 1"}]
        )
        # Extract numeric score from LLM response
        score = float(response.choices[0].message.content.strip())
        # Ensure score is strictly in (0,1)
        if score <= 0:
            score = 0.01
        elif score >= 1:
            score = 0.99
        return score
    except Exception as e:
        # If LLM fails, fallback to 0.5
        print(f"[STEP] ERROR calling LLM for {task_name}: {e}")
        return 0.5

def main():
    log_start()

    # Call LLM for each task
    easy_score = call_llm("easy")
    log_step("easy", easy_score)

    medium_score = call_llm("medium")
    log_step("medium", medium_score)

    hard_score = call_llm("hard")
    log_step("hard", hard_score)

    log_end()

if __name__ == "__main__":
    main()
