🤖 TalentScout – AI Hiring Assistant Chatbot
📌 Project Overview

TalentScout Hiring Assistant is an AI-powered chatbot designed to automate the initial screening process for technology candidates.

The chatbot:

Collects essential candidate details

Gathers declared tech stack

Generates tailored technical interview questions

Maintains conversation context

Provides structured and professional interactions

This project demonstrates practical implementation of:

Prompt Engineering

Large Language Model integration

Context-aware conversation flow

Streamlit UI development

Secure API handling

🎯 Objective

The goal of this project is to design an intelligent hiring assistant that:

Collects candidate information

Identifies technical stack

Dynamically generates relevant interview questions

Maintains smooth conversational flow

Handles unexpected inputs gracefully

🏗️ System Architecture
User
  ↓
Streamlit Frontend
  ↓
Prompt Engineering Layer
  ↓
Groq API (Llama 3.1 Model)
  ↓
Response Generation
  ↓
Session State Memory
  ↓
UI Display


Conversation context is managed using:

st.session_state

🖥️ Features
✅ 1. Candidate Information Collection

The chatbot collects:

Full Name

Email Address

Phone Number

Years of Experience

Desired Position

Current Location

Tech Stack

If information is missing, it politely requests the remaining fields.

✅ 2. Tech Stack Declaration

Candidates can specify:

Programming Languages

Frameworks

Databases

Tools

Example:

Python, Django, PostgreSQL, AWS

✅ 3. Dynamic Technical Question Generation

For each declared technology, the chatbot generates:

3–5 technical questions

Mixed difficulty (Basic → Advanced)

Practical knowledge-based questions

Clear professional formatting

✅ 4. Context-Aware Interaction

The chatbot uses staged conversation flow:

Stage 1 → Information Collection

Stage 2 → Technical Question Generation

Stage 3 → Completion

This prevents duplicate responses and ensures smooth user experience.

✅ 5. Fallback Mechanism

If unclear input is detected, the chatbot responds professionally and requests clarification.

✅ 6. Graceful Exit

Typing:

exit
quit
bye


Will terminate the conversation with a professional closing message.

🧠 Prompt Engineering Strategy
🔹 Information Collection Prompt

Designed to:

Gather structured candidate details

Maintain professional tone

Avoid JSON responses

Ask only for missing information

🔹 Technical Question Generation Prompt

Designed to:

Generate grouped questions by technology

Include varying difficulty levels

Focus on practical problem-solving

Avoid generic theoretical questions

Temperature is set to 0.7 to balance creativity and relevance.

🛠️ Tech Stack

Python

Streamlit

Groq API

Llama 3.1 (8B Instant)

python-dotenv

Git

🤖 Model Used
Llama 3.1 (8B Instant) via Groq API


Chosen because:

Free tier availability

Fast inference speed

Modern open-source LLM

Suitable for real-time chatbot applications

⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/yourusername/talentscout-hiring-assistant.git
cd talentscout-hiring-assistant

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Groq API Key

Create a .env file:

GROQ_API_KEY=your_api_key_here


⚠ Do NOT upload .env to GitHub.

5️⃣ Run Application
streamlit run app.py


Application will open at:

http://localhost:8501

📂 Project Structure
talentscout-hiring-assistant/
│
├── app.py
├── prompts.py
├── utils.py
├── requirements.txt
├── README.md
└── .env

🔐 Data Privacy & Security

API keys stored in environment variables

No permanent storage of candidate data

Session-based temporary storage only

Designed with GDPR data minimization principles in mind

🧩 Challenges & Solutions
Challenge	Solution
Model quota issues	Switched to free Groq API
Double responses	Implemented stage-based flow
JSON output formatting	Modified prompt to enforce conversational replies
Model deprecation	Updated to Llama 3.1
🚀 Future Enhancements

Candidate scoring system

Resume parsing integration

Sentiment analysis

Multilingual support

Secure database storage

Cloud deployment (AWS / Streamlit Cloud)

🎥 Demo

A short video demonstration includes:

Greeting

Information collection

Tech stack detection

Question generation

Conversation termination

(Insert demo link here)

🏁 Conclusion

The TalentScout Hiring Assistant demonstrates:

Real-world LLM integration

Structured prompt engineering

Context management

Secure API usage

Clean user interface implementation

This project reflects practical AI application in recruitment automation.