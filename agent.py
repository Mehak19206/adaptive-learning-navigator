import random

class LearningAgent:
    def __init__(self):
        self.actions = ["easy", "medium", "hard", "revise", "skip"]

    def choose_action(self, state):
        knowledge = state["knowledge"]

        if knowledge < 30:
            return random.choice(["easy", "medium"])
        elif knowledge < 70:
            return random.choice(["medium", "hard", "revise"])
        else:
            return random.choice(["hard", "revise"])