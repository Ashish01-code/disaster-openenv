# 🌍 Disaster Response OpenEnv Environment

## 🚀 Overview

This project implements a **disaster response simulation environment** using the OpenEnv specification.
The objective is to simulate real-world rescue scenarios where an agent must make strategic decisions to maximize the number of people rescued across multiple zones.

---

## ✨ Features

* OpenEnv compliant environment
* Multi-task setup: Easy, Medium, Hard
* Deterministic grading system
* Dockerized for reproducibility
* Structured logging for evaluation (`[START]`, `[STEP]`, `[END]`)

---

## 🧠 Environment Design

### Observation Space

At each step, the agent receives:

* Number of people trapped
* Available rescue teams
* Drone availability
* Disaster severity / uncertainty
* Zone status

---

### 🎯 Action Space

The agent can take the following actions:

* `dispatch_team_high`
* `dispatch_team_medium`
* `send_drone`
* `wait`

---

## 🧪 Tasks

### Easy

* Fewer zones
* Low uncertainty
* Focus on basic resource allocation

### Medium

* Moderate zones and uncertainty
* Requires balanced decision-making

### Hard

* High uncertainty
* Limited resources
* Requires optimal strategy

---

## 🏆 Reward System

* Positive reward for successful rescues
* Negative reward for delays or inefficient actions
* Final score reflects overall efficiency

---

## 🐳 Running the Project

### Using Docker

```bash
docker build -t disaster-env .
docker run disaster-env
```

---

## 📂 Project Structure

```
.
├── agent.py
├── disaster_env.py
├── openenv_wrapper.py
├── tasks.py
├── inference.py
├── Dockerfile
├── requirements.txt
├── openenv.yaml
└── README.md
```

---

## 🤖 Inference

The main entry point is:

```bash
python inference.py
```

Output follows structured logs:

```
[START] Running inference
[STEP] Task=easy Score=...
[STEP] Task=medium Score=...
[STEP] Task=hard Score=...
[END] Inference complete
```

---

## ⚙️ Environment Variables

Make sure to configure:

* `API_BASE_URL`
* `MODEL_NAME`
* `HF_TOKEN`

---

## 📦 Deployment

This project is deployed using **Hugging Face Spaces (Docker SDK)**.

---

## 🎯 Goal

Design an intelligent agent capable of:

* Efficient resource allocation
* Handling uncertainty
* Maximizing rescue outcomes

---

## 📌 Notes

* Built for OpenEnv evaluation pipelines
* Optimized for low-resource environments (2 vCPU, 8GB RAM)
* Execution time under 20 minutes

---

## 🧑‍💻 Author

Ashish D
