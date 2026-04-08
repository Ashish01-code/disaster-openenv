import random

class SmartAgent:
    def __init__(self):
        pass

    def choose_actions(self, zones):

        all_zones = []

        # Flatten grid with scoring
        for i, row in enumerate(zones):
            for j, z in enumerate(row):
                if z["people_trapped"] > 0:

                    score = (
                        z["people_trapped"] * 1.5 +
                        z["severity"] * 2 +
                        (10 if z["high_risk"] else 0) -
                        z["uncertainty"] * 5
                    )

                    all_zones.append((score, i, j, z))

        # Sort by priority
        all_zones.sort(reverse=True, key=lambda x: x[0])

        actions = []
        used_zones = set()

        for score, i, j, z in all_zones:

            if (i, j) in used_zones:
                continue

            if z["rescue_teams"] > 0 and z["people_trapped"] > 20:
                actions.append((i, j, "dispatch_team_high"))
                used_zones.add((i, j))

            elif z["rescue_teams"] > 0 and z["people_trapped"] > 5:
                actions.append((i, j, "dispatch_team_medium"))
                used_zones.add((i, j))

            elif z["drones"] > 0 and z["uncertainty"] > 0.2:
                actions.append((i, j, "send_drone"))
                used_zones.add((i, j))

        return actions