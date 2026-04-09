# tasks.py
from disaster_env import DisasterEnv

# Helper to clamp score strictly between 0.01 and 0.99
def normalize_score(score):
    return max(0.01, min(0.99, score))

def run_task(difficulty):
    """
    Run the disaster environment with a simple policy
    and return a raw score between 0 and 1.
    """
    env = DisasterEnv()
    zones = env.reset(difficulty=difficulty)
    
    # Simple random/heuristic actions for demonstration
    total_steps = 10
    cumulative_reward = 0.0

    for _ in range(total_steps):
        # Example heuristic: dispatch based on remaining zones
        actions = ["dispatch_team_high" if z > 0 else "wait" for z in zones]
        zones, reward, done, _ = env.step(actions)
        cumulative_reward += reward
        if done:
            break

    # Normalize reward to 0-1 range
    raw_score = cumulative_reward / (total_steps * len(zones))
    return normalize_score(raw_score)

# === Tasks ===
def easy():
    return run_task("easy")

def medium():
    return run_task("medium")

def hard():
    return run_task("hard")
