from openenv_wrapper import OpenEnvWrapper
from agent import SmartAgent

def run_task(steps, difficulty):
    env = OpenEnvWrapper()
    agent = SmartAgent()

    obs = env.reset()
    env.env.reset(difficulty=difficulty)

    total_rescued_start = sum(
        z["people_trapped"] for row in env.env.zones for z in row
    )

    for _ in range(steps):
        actions = agent.choose_actions(env.env.zones)
        obs, reward, done, _ = env.step({"actions": actions})

        if done:
            break

    total_rescued_end = sum(
        z["people_trapped"] for row in env.env.zones for z in row
    )

    rescued = total_rescued_start - total_rescued_end

    score = rescued / total_rescued_start
    return round(min(1.0, score), 2)


def easy():
    return run_task(10, "easy")

def medium():
    return run_task(20, "medium")

def hard():
    return run_task(30, "hard")