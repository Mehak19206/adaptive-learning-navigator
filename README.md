# 🎓 Adaptive Learning Navigator

## 🚀 Overview

Adaptive Learning Navigator is an intelligent simulation system that models how a student learns over time using a decision-making agent. The system dynamically selects learning strategies (easy, medium, hard, revise, skip) to maximize knowledge while minimizing time.

This project demonstrates a simplified **Reinforcement Learning (RL)-inspired approach** using a heuristic-based agent.

---

## 🎯 Key Features

* 📌 Goal-based learning (UPSC, JEE, NEET, Hackathon)
* 📊 Difficulty levels (Easy, Medium, Hard)
* 🤖 Intelligent agent for decision-making
* 📚 Resource-based learning system
* 📈 Score & efficiency calculation
* 🧠 Step-by-step learning logs
* 🌐 Interactive UI using Streamlit

---

## 🧠 How It Works

1. User selects a **Goal** and **Difficulty**
2. The **Agent** chooses actions based on current knowledge
3. The **Environment** applies learning outcomes (gain + time)
4. The system calculates:

   * Reward = Learning Gain − Time Cost
   * Score = Knowledge / (Time + 1)
   * Efficiency = (Knowledge × 100) / (Time + 1)
5. The process continues until the target is achieved

---

## 🏗️ Project Structure

```
learning_navigator/
│── app.py          # Streamlit UI
│── env.py          # Learning environment
│── agent.py        # Decision-making agent
│── resources.py    # Goal-based resources
│── baseline.py     # Simulation testing (optional)
│── config.yaml     # Project configuration
│── requirements.txt
```

---

## ⚙️ Installation & Setup

1. Clone or download the project
2. Open in VS Code
3. Install dependencies:

```
pip install streamlit
```

4. Run the app:

```
streamlit run app.py
```

---

## 🧪 Example Output

```
Step 1: NCERT Reading → +5 knowledge  
Step 2: Laxmikant Polity → +10 knowledge  
Step 3: Advanced Analysis → +15 knowledge  

Final Results:
Knowledge: 75  
Time Spent: 10  
Score: 6.8  
Efficiency: 680%
```

---

## 🧩 Core Components

### 🔹 Environment (`env.py`)

* Simulates learning progress
* Tracks knowledge, time, and steps
* Computes rewards

### 🔹 Agent (`agent.py`)

* Chooses actions based on knowledge level
* Uses heuristic strategy (not Q-learning)

### 🔹 Resources (`resources.py`)

* Maps goals to real-world study resources
* Defines gain and time cost

### 🔹 UI (`app.py`)

* Built using Streamlit
* Displays results and learning journey

---

## 🧠 Future Improvements

* Implement Q-learning for adaptive policy learning
* Add user progress tracking
* Personalize learning paths further
* Improve UI/UX design
* Add data visualization (graphs)

---

## 🏆 Why This Project Stands Out

* Combines **AI concepts with real-world learning**
* Simple, explainable, and scalable design
* Demonstrates **decision-making under constraints**
* Practical application of reinforcement learning ideas

---

## 👨‍💻 Author

** Team:
 Ayush Pandey
 Yash Kumar
 Mehak Rai **

---

## 📌 Note

This project uses a simplified RL-inspired approach for educational purposes and does not implement full reinforcement learning algorithms like Q-learning.
