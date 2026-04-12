from env import LearningEnv
from agent import LearningAgent
from tasks import grade_easy, grade_medium, grade_hard

def run_baseline():
    agent = LearningAgent()
    results = {}

    for task, grader in [
        ("easy", grade_easy),
        ("medium", grade_medium),
        ("hard", grade_hard),
    ]:
        env = LearningEnv(task=task)
        state = env.reset()

        for _ in range(20):
            action = agent.choose_action(state)
            state, reward, done, _ = env.step(action)
            if done:
                break

        results[task] = grader(state.knowledge)

    return results

if __name__ == "__main__":
    print(run_baseline())