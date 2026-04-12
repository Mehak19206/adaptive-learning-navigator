# 🎓 Adaptive Learning Navigator

## 📌 Overview

Adaptive Learning Navigator is a reinforcement learning-inspired environment that simulates real-world study decision-making.

The system models how a student chooses between different types of learning activities (easy, medium, hard, revise, skip) to maximize knowledge while minimizing time.

---

## 🎯 Motivation

In real-world learning scenarios, students must balance:

* Time constraints
* Learning efficiency
* Task difficulty

This project simulates that decision process and evaluates how effectively an agent can optimize learning outcomes.

---

## ⚙️ Environment Design

### 🧠 State (Observation)

The environment tracks:

* `knowledge` → learning progress (0–100)
* `time_spent` → total effort/time invested

---

### 🎮 Actions

The agent can choose:

* `easy`
* `medium`
* `hard`
* `revise`
* `skip`

Each action provides different knowledge gains and time costs.

---

### 🏆 Reward Function

```
reward = knowledge_gain - time_spent
```

This encourages:

* Efficient learning
* Avoiding unnecessary time usage

---

## 📊 Tasks & Evaluation

The environment includes **3 tasks**:

| Task   | Target Knowledge | Difficulty   |
| ------ | ---------------- | ------------ |
| Easy   | 50               | Beginner     |
| Medium | 75               | Intermediate |
| Hard   | 100              | Advanced     |

---

### 🧪 Grading Function

Each task is scored between **0 and 1**:

```
score = achieved_knowledge / target_knowledge
```

---

## 🤖 Baseline Agent

A heuristic-based agent is implemented:

* Prefers easier tasks at low knowledge
* Switches to harder tasks as knowledge increases
* Uses revise near completion

---

## 📈 Baseline Results

Example output:

```
Easy: 1.0  
Medium: ~0.9  
Hard: ~0.8  
```

---

## 🌐 API (OpenEnv Compatible)

The environment exposes:

* `POST /reset`
* `POST /step`
* `GET /state`

Built using FastAPI.

---

## 🧪 Inference Script

Run baseline:

```
python inference.py
```

---

## 🖥️ UI (Streamlit Demo)

Run:

```
python -m streamlit run app.py
```

Features:

* Goal selection
* Difficulty selection
* Step-by-step logs
* Final score display

---

## 🐳 Docker Support

Run environment using:

```
docker build -t learning-env .
docker run -p 8000:8000 learning-env
```

---

## 🛠️ Setup Instructions

Install dependencies:

```
pip install -r requirements.txt
```

Run API:

```
python -m uvicorn main:app --reload
```

---

## 📁 Project Structure

```
env.py          # Environment logic  
agent.py        # Decision-making agent  
tasks.py        # Task grading  
models.py       # Pydantic models  
main.py         # API (OpenEnv)  
app.py          # UI (Streamlit)  
inference.py    # Baseline script  
```

---

## 🚀 Deployment

Deployed on Hugging Face Spaces using Streamlit.

---

## 👨‍💻 Authors

* Mehak Rai (Team Lead)
* Ayush Pandey
* Yash Kumar

---

## ✅ Status

✔ OpenEnv compliant
✔ Fully functional
✔ Ready for evaluation
