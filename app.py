import streamlit as st
from env import LearningEnv
from agent import LearningAgent

st.title("🎓 Adaptive Learning Navigator")

# USER INPUTS
goal = st.selectbox(
    "🎯 Select Your Goal",
    ["UPSC", "JEE", "NEET", "Hackathon"]
)

difficulty = st.selectbox(
    "📊 Select Difficulty",
    ["easy", "medium", "hard"]
)

if st.button("🚀 Start Learning Simulation"):

    env = LearningEnv(task=difficulty, goal=goal)
    agent = LearningAgent()

    state = env.reset()

    steps_log = []
    total_reward = 0

    for step in range(20):
        action = agent.choose_action(state)

        new_state, reward, done, gain, resource_name = env.step(action)

        total_reward += reward

        steps_log.append(
            f"Step {step+1}: {resource_name} → +{gain} knowledge | Time: {new_state['time_spent']} | Reward: {round(reward,2)}"
        )

        state = new_state

        if done:
            break

    # FINAL SCORE
    knowledge = state["knowledge"]
    time_spent = state["time_spent"]

    score = knowledge / (time_spent + 1)
    efficiency = (knowledge * 100) / (time_spent + 1)

    st.subheader("📈 Final Results")

    st.write(f"📚 Knowledge Gained: {knowledge}")
    st.write(f"⏱ Time Spent: {time_spent}")
    st.write(f"🏆 Score: {round(score,2)}")
    st.write(f"⚡ Efficiency: {round(efficiency,2)}%")

    st.subheader("🧠 Learning Journey")
    for log in steps_log:
        st.write(log)