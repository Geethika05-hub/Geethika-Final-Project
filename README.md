
# Auto Interview Pro

---

## 📌 Project Overview
Auto Interview Pro is a modular, Flask-based Generative AI application that automates interview preparation by dynamically generating technical questions, behavioral questions, interview tips, and resume suggestions based on user inputs (topics or job descriptions).  
It uses a local LLM server (Ollama) to ensure security and fast response times, achieving high levels of SDLC automation without reliance on cloud services.

---

## 🎯 Core Features
- 🔹 **Automated Interview Question Generation** (Technical + Behavioral)
- 🔹 **Tips Extraction** from Job Descriptions
- 🔹 **Resume Booster** suggestions based on Job Descriptions
- 🔹 **Practice Mode** mixing different question types
- 🔹 **CSV Export** of generated interview questions
- 🔹 **Responsive UI** built using Bootstrap
- 🔹 **Multi-Agent System**: Clean modular separation (QuestionAgent, TipsAgent, ResumeAgent)

---

## ⚙️ Technology Stack
- Python 3.x
- Flask
- Bootstrap 5
- Local LLM Server (Ollama, using Llama3 8B/13B)
- CSV Handling (Python `csv` module)

---

## 🏗️ How to Run
1. Ensure Python 3.x is installed.
2. Install Flask:  
   ```
   pip install flask
   ```
3. Ensure Ollama is installed locally and running a model like Llama3.
4. Clone or download this repository.
5. Navigate to the project directory and run:
   ```
   python app.py
   ```
6. Open your browser and go to `http://localhost:5000/`

---

## 🛠️ Solution Architecture Summary
- Frontend: User Browser (Bootstrap + Flask templates)
- Backend: Flask Web Server
- Logic Layer: QuestionAgent, TipsAgent, ResumeAgent
- LLM Inference Layer: Local Ollama LLM Server
- Optional: Export Module for CSV downloads

> User → Flask Web Server → Appropriate Agent → Ollama LLM → Result Rendered on Browser

---

## 📊 Percentage of Automation Across SDLC Phases
| SDLC Phase | Automation Achieved | Manual Effort Needed |
|:---|:---:|:---:|
| Requirement Gathering (Prompts Creation) | 90% | 10% |
| System Design (Architecture + Modeling) | 85% | 15% |
| Implementation (Web App, Agents, API Calls) | 95% | 5% |
| Testing (Manual Testing of Outputs) | 70% | 30% |
| Deployment (Local Server Only) | 80% | 20% |
| Maintenance & Updates | 70% | 30% |

**Overall Automation Achieved: ≈ 85%** 🔥

---

## 🧠 Future Enhancements
- Integrate a login system for personalized practice sessions.
- Dockerize the solution for easy cloud deployment.
- Add Feedback Module to collect user evaluations on generated outputs.
- Integrate RAG (Retrieval-Augmented Generation) to enrich context dynamically.

---

## 👥 Credits
Developed by: **Geethika**  
Part of Final Project for:  
**COT6930 – Generative AI and Software Development Lifecycles**

---
