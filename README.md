# 🎫 SmartTicket AI – Prioritize & Respond

![SmartTicket AI](https://img.shields.io/badge/Status-Active-success.svg)
![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-black)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**SmartTicket AI** is an intelligent customer support agent designed to streamline ticket management workflows. By leveraging OpenAI's GPT models and Scikit-Learn's Machine Learning clustering, it automatically analyzes incoming support tickets for urgency, detects customer sentiment, groups similar issues, and suggests rapid response templates.

---

## 📖 Table of Contents
- [Problem & Solution](#problem--solution)
- [How It Works](#how-it-works)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)

---

## ⚡ Problem & Solution

**The Problem:** Support teams receive hundreds of tickets daily, leading to urgent, critical issues getting buried under low-priority requests. This causes delays, frustrates customers, and ties up human agents in manual triage.

**The Solution:** SmartTicket AI operates as an intelligent middle-layer, actively sorting, analyzing, and prioritizing the ticket backlog before human intervention is required.

---

## ⚙️ How It Works

1. **Input:** Upload raw ticket text (Title + Description) via CSV.
2. **AI Analysis:** Each ticket is run through OpenAI's language models to determine:
   - **Urgency Classification:** (High / Medium / Low)
   - **Sentiment Detection:** (Frustrated / Neutral / Happy)
   - **Response Suggestion:** Instant, tailored draft replies.
3. **Clustering:** Tickets are vectorized and grouped using unsupervised machine learning (K-Means) to easily identify widespread outages or related bugs.
4. **Actionable Dashboard:** Results are presented in a fast, responsive Bootstrap/Flask web interface for seamless workflow integration.

---

## 🌟 Key Features
- **Hours Saved:** Removes manual sorting and triage from the support workflow.
- **Immediate Escalation:** Ensures high-priority requests are flagged for immediate action.
- **Actionable AI Responses:** Provides human-like response drafts to get back to users quicker.
- **Outbreak Detection:** ML Clustering automatically groups similar simultaneous issues to detect system-wide bugs.
- **Python 3.13 Compatible:** Runs efficiently on the latest Python standard utilizing lightweight web architecture.

---

## 🛠 Tech Stack
- **Backend/Routing:** Python 3.x, Flask
- **AI Integration:** OpenAI GPT API (`gpt-3.5-turbo`)
- **Data & Machine Learning:** Pandas, Scikit-learn (K-Means, TF-IDF)
- **Frontend Design:** HTML5, CSS3, Bootstrap 5

---

## 🚀 Getting Started

Ensure you have **Python 3.8+** (Supports 3.13+) installed on your machine.

### 1. Clone the repository
```bash
git clone https://github.com/YAGAVI2006/SmartTicket-AI.git
cd SmartTicket-AI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a file named `.env` in the root directory and add your OpenAI API Key:
```env
OPENAI_API_KEY=sk-...your-key...
```
*(Alternatively, you can provide the API key directly in the web dashboard).*

### 4. Start the Application
```bash
python app.py
```
Go to **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

---

## 📊 Usage

1. Open the dashboard.
2. Use the provided **`tickets.csv`** sample file to test functionality.
3. Once analyzed, filter by high urgency or frustrated sentiment securely via the table UI.
4. **Download** the resulting `analyzed_tickets_smart_ai.csv` locally for record keeping.
