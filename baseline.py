from env import LearningEnv
from agent import LearningAgent

def run_baseline(task="medium", goal="UPSC", episodes=5):
    agent = LearningAgent()

    for ep in range(episodes):
        env = LearningEnv(task=task, goal=goal)
        state = env.reset()

        total_reward = 0

        print(f"\n===== Episode {ep+1} =====")

        for step in range(20):
            action = agent.choose_action(state)

            new_state, reward, done, gain, resource_name = env.step(action)

            total_reward += reward

            print(
                f"Step {step+1}: {resource_name} | +{gain} knowledge | "
                f"Time: {new_state['time_spent']} | Reward: {round(reward,2)}"
            )

            state = new_state

            if done:
                break

        # Final Metrics
        knowledge = state["knowledge"]
        time_spent = state["time_spent"]

        score = knowledge / (time_spent + 1)
        efficiency = (knowledge * 100) / (time_spent + 1)

        print("\n--- Final Results ---")
        print(f"Knowledge: {knowledge}")
        print(f"Time Spent: {time_spent}")
        print(f"Score: {round(score,2)}")
        print(f"Efficiency: {round(efficiency,2)}%")
        print(f"Total Reward: {round(total_reward,2)}")


if __name__ == "__main__":
    run_baseline(task="medium", goal="UPSC", episodes=3)