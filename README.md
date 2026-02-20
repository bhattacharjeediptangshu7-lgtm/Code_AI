# 🤖 GitHub Agent — Autonomous AI Software Engineer

GitHub Agent is an autonomous AI Software Engineer that can plan, generate, execute, fix, and publish complete software projects directly from a natural language prompt.

It simulates how a real software engineer works — understanding requirements, writing code, running it, fixing errors, and pushing the final result to GitHub.

This is the foundation of a self-evolving, multi-agent AI engineering system.

---

# ✨ Features

• Autonomous project planning  
• AI-generated production-ready code  
• Automatic project execution  
• Self-healing error fixing  
• Automatic GitHub repository creation and upload  
• Clean terminal UI with live agent status  
• Supports Python, Web, and Node projects  

---

# 🧠 How It Works

The agent follows a structured workflow:

User Prompt  
↓  
Planner Agent → creates project plan  
↓  
Code Generator Agent → writes complete code  
↓  
Executor Agent → runs the project  
↓  
Fixer Agent → fixes errors if found  
↓  
GitHub Agent → uploads project to GitHub  

---

# 🏗 Project Structure


github-agent/
│
├── agent/
│ ├── graph.py
│ └── state.py
│
├── app/
│ └── main.py
│
├── nodes/
│ ├── planner.py
│ ├── code_generator.py
│ ├── executor.py
│ ├── fixer.py
│ └── github_push.py
│
├── config/
│ └── settings.py
│
├── utils/
│ ├── logger.py
│ └── ui.py
│
├── generated_projects/
│
├── requirements.txt
│
└── README.md


---

# ⚙ Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/github-agent.git

cd github-agent
2. Create Virtual Environment
python -m venv venv

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Install and Run Ollama

Download:

https://ollama.com

Pull required models:

ollama pull qwen2.5:7b-instruct

ollama pull deepseek-coder:6.7b

ollama pull qwen2.5-coder:7b
5. Configure Environment

Create .env

OLLAMA_BASE_URL=http://localhost:11434

GITHUB_TOKEN=your_github_token
▶ Run the Agent
python app/main.py

Example prompt:

Create a portfolio website in HTML, CSS and JavaScript
📁 Generated Projects Location

Projects will be created in:

generated_projects/

Outside the main project folder.

🚀 Example Capabilities

The agent can build:

• Web Apps
• Python Tools
• Portfolio Websites
• APIs
• CLI tools
• Automation scripts

🧠 Current Architecture

Single-Agent Sequential Workflow

Planner → Generator → Executor → Fixer → GitHub
🔮 Future Roadmap

This project will evolve into a fully autonomous multi-agent AI engineering system.

🧩 Phase 1 — Memory System

Persistent memory using:

• Vector Database
• Project history
• Error learning

Agent will learn from past mistakes.

🤖 Phase 2 — Multi-Agent Architecture

Separate specialized agents:

• Architect Agent
Designs system architecture

• Developer Agent
Writes production code

• Tester Agent
Writes and runs tests

• Debug Agent
Fixes issues

• DevOps Agent
Deploys project

• GitHub Agent
Manages repositories

⚡ Phase 3 — Parallel Agents

Agents will work simultaneously.

Example:

Developer Agent writing code
while
Tester Agent preparing tests

🌐 Phase 4 — Fully Autonomous Engineering

The system will:

• Build SaaS products
• Fix production bugs
• Improve its own code
• Maintain projects automatically

🎯 Long Term Vision

To create a fully autonomous AI Software Engineer comparable to Devin-class systems.

🛠 Technology Stack

Python
LangChain
Ollama
LLMs
GitHub API

📊 Current Status

Core autonomous loop working

Planning ✅
Code Generation ✅
Execution ✅
Fixing ✅
GitHub Upload ✅

🤝 Contribution

Contributions are welcome.

Future work includes:

Multi-agent orchestration
Memory system
Cloud deployment
Self-improvement

📜 License

MIT License

👨‍💻 Author

Diptangshu Bhattacharjee

Senior Product Support Engineer
AI Engineer

⭐ Support

If you like this project, give it a star.