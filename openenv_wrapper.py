from pydantic import BaseModel
from disaster_env import DisasterEnv

class Observation(BaseModel):
    zones: list
    time: int

class Reward(BaseModel):
    value: float


class OpenEnvWrapper:
    def __init__(self):
        self.env = DisasterEnv()

    def reset(self):
        zones = self.env.reset(difficulty="medium")
        return Observation(zones=zones, time=0).dict()

    def step(self, actions: list):  # ✅ FIXED
        zones, reward, done, _ = self.env.step(actions)  # ✅ FIXED

        return (
            Observation(zones=zones, time=self.env.time_elapsed).dict(),
            float(reward),  # ✅ return float (IMPORTANT)
            done,
            {}
        )

    def state(self):
        return Observation(
            zones=self.env.zones,
            time=self.env.time_elapsed
        ).dict()
