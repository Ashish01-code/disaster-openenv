import random

class DisasterEnv:
    def __init__(self, grid_size=4):
        self.grid_size = grid_size
        self.zones = []
        self.time_elapsed = 0
        self.initial_people_total = 0

    def reset(self, difficulty="medium"):
        self.zones = []
        self.time_elapsed = 0
        self.initial_people_total = 0

        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):

                if difficulty == "easy":
                    people = random.randint(10, 30)
                    teams = random.randint(1, 2)
                    uncertainty = 0.1

                elif difficulty == "hard":
                    people = random.randint(50, 100)
                    teams = random.randint(0, 1)
                    uncertainty = 0.4

                else:
                    people = random.randint(20, 60)
                    teams = random.randint(0, 2)
                    uncertainty = 0.25

                disaster_type = random.choice(["fire", "flood", "earthquake"])

                row.append({
                    "disaster_type": disaster_type,
                    "severity": random.randint(1, 10),
                    "people_trapped": people,
                    "high_risk": random.choice([True, False]),
                    "rescue_teams": teams,
                    "drones": random.randint(0, 1),
                    "uncertainty": uncertainty,
                    "rescued": 0
                })

                self.initial_people_total += people
            self.zones.append(row)

        return self.zones

    def step(self, action_list):
        reward = 0
        self.time_elapsed += 1

        for act in action_list:
            i, j, action = act
            zone = self.zones[i][j]

            if action == "dispatch_team_high" and zone["rescue_teams"] > 0:
                saved = min(zone["people_trapped"], random.randint(10, 30))
                zone["people_trapped"] -= saved
                zone["rescued"] += saved
                zone["rescue_teams"] -= 1
                reward += saved * 1.0

            elif action == "dispatch_team_medium" and zone["rescue_teams"] > 0:
                saved = min(zone["people_trapped"], random.randint(5, 15))
                zone["people_trapped"] -= saved
                zone["rescued"] += saved
                zone["rescue_teams"] -= 1
                reward += saved * 0.7

            elif action == "send_drone" and zone["drones"] > 0:
                zone["uncertainty"] *= 0.8
                zone["drones"] -= 1
                reward += 1

        # 🔥 Disaster evolution (enhanced realism)
        for row in self.zones:
            for zone in row:

                if zone["disaster_type"] == "fire":
                    spread = random.randint(1, 4)
                    zone["people_trapped"] += spread
                    reward -= spread * 0.7

                elif zone["disaster_type"] == "flood":
                    rise = random.randint(0, 3)
                    zone["people_trapped"] += rise
                    reward -= rise * 0.5

                elif zone["disaster_type"] == "earthquake":
                    aftershock = random.randint(0, 2)
                    zone["people_trapped"] += aftershock
                    reward -= aftershock * 0.6

                if zone["severity"] > 7:
                    zone["people_trapped"] += 2
                    reward -= 1

        # Resource recovery
        for row in self.zones:
            for z in row:
                if random.random() < 0.1:
                    z["rescue_teams"] += 1
                if random.random() < 0.1:
                    z["drones"] += 1

        done = all(z["people_trapped"] == 0 for row in self.zones for z in row)

        return self.zones, reward, done, {}

    def get_score(self):
        rescued_total = sum(z["rescued"] for row in self.zones for z in row)
        return round(rescued_total / self.initial_people_total, 2)