# 📅 Calendar Agent AI 🤖

> An intelligent AI-powered calendar assistant that lets you **schedule and manage events using natural language**.

---

## 🚀 Overview

**Calendar Agent AI** is a desktop-based AI assistant that combines:

- 🧠 AI reasoning  
- 💬 Chat-based interaction  
- 📅 Calendar event management  

It allows users to interact with their calendar like a chatbot instead of using traditional UI.

---

## ✨ Features

- 💬 **Chat with your calendar**
  - Example: *"Schedule meeting tomorrow at 5pm"*
- 📅 **Smart event management**
  - Add, edit, delete events
- 🧠 **AI-powered understanding**
  - Converts natural language → calendar actions
- 🗂️ **Persistent memory**
  - Stores conversations and events
- 🖥️ **Modern GUI**
  - Built using CustomTkinter
- ⚡ **Lightweight & fast**
  - Runs locally

---

## 🖼️ Screenshots

### 🔹 Main Interface
<img width="1127" height="782" alt="Screenshot 2026-04-08 124201" src="https://github.com/user-attachments/assets/29b3dbb1-f938-45ac-8dc5-367daee1f98e" />


### 🔹 Chat Interaction
<img width="1131" height="796" alt="Screenshot 2026-04-08 124145" src="https://github.com/user-attachments/assets/fc630f7d-9d50-4bbf-8b4a-5fa0617f889d" />



---

## 🛠️ Tech Stack

- **Frontend:** CustomTkinter  
- **Backend:** Python  
- **AI Engine:** OpenAI / Gemini API  
- **Database:** SQLite / JSON  
- **Concurrency:** Threading  

---

## 📂 Project Structure

```
Calendar_Agent.ai
├── agent.py          # AI logic
├── db.py             # Database operations
├── main.py           # UI entry point
├── requirements.txt  # Dependencies
└── images/           # Screenshots
```
---

## ⚙️ Installation

```bash
git clone https://github.com/Niladri962/Calendar_Agent.ai
cd Calendar_Agent.ai
pip install -r requirements.txt


pip install -r requirements.txt
🔑 Environment Setup

Create a .env file:

OPENAI_API_KEY=your_api_key
(or use Gemini API if configured)

▶️ Run the App
python main.py
