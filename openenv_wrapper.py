from pydantic import BaseModel
from disaster_env import DisasterEnv

class Observation(BaseModel):
    zones: list
    time: int

class Action(BaseModel):
    actions: list

class Reward(BaseModel):
    value: float


class OpenEnvWrapper:
    def __init__(self):
        self.env = DisasterEnv()

    def reset(self):
        zones = self.env.reset(difficulty="medium")
        return Observation(zones=zones, time=0)

    def step(self, action: Action):
        zones, reward, done, _ = self.env.step(action["actions"])

        return (
            Observation(zones=zones, time=self.env.time_elapsed),
            Reward(value=reward),
            done,
            {}
        )

    def state(self):
        return Observation(zones=self.env.zones, time=self.env.time_elapsed)