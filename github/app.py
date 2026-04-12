
import streamlit as st
from env import LearningEnv
from agent import LearningAgent

st.title("🎓 Adaptive Learning Navigator")

# Select options
goal = st.selectbox("🎯 Select Goal", ["UPSC", "JEE", "NEET", "Hackathon"])
difficulty = st.selectbox("📊 Select Difficulty", ["easy", "medium", "hard"])

if st.button("Start Simulation"):
    env = LearningEnv(task=difficulty, goal=goal)
    agent = LearningAgent()

    state = env.reset()

    logs = []

    for step in range(20):
        action = agent.choose_action(state)
        state, reward, done, _ = env.step(action)

        logs.append(
            f"Step {step+1}: Action={action}, Knowledge={state.knowledge}, Time={state.time_spent}, Reward={reward.value}"
        )

        if done:
            break

    st.subheader("📊 Final Results")
    st.write(f"Knowledge Gained: {state.knowledge}")
    st.write(f"Time Spent: {state.time_spent}")

    score = state.knowledge / (state.time_spent + 1)
    st.write(f"Score (Efficiency): {round(score, 2)}")

    st.subheader("📜 Step Log")
    for log in logs:
        st.write(log)