from resources import GOAL_RESOURCES

class LearningEnv:
    def __init__(self, task="medium", goal="UPSC"):
        self.max_knowledge = 100
        self.max_steps = 20

        self.tasks = {
            "easy": 50,
            "medium": 75,
            "hard": 100
        }

        self.target = self.tasks[task]
        self.goal = goal
        self.resources = GOAL_RESOURCES[goal]

        self.reset()

    def reset(self):
        self.knowledge = 0
        self.time_spent = 0
        self.steps = 0
        return self._get_state()

    def _get_state(self):
        return {
            "knowledge": self.knowledge,
            "time_spent": self.time_spent
        }

    def step(self, action):
        resource = self.resources[action]

        gain = resource["gain"]
        time = resource["time"]

        self.knowledge += gain
        self.time_spent += time
        self.steps += 1

        if self.knowledge > self.max_knowledge:
            self.knowledge = self.max_knowledge

        reward = gain - time

        done = (
            self.knowledge >= self.target or
            self.steps >= self.max_steps
        )

        return self._get_state(), reward, done, gain, resource["name"]