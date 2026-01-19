AI RESUME EVALUATOR:

 AI Resume Evaluator is a full-stack web application that analyzes resumes and provides AI-generated feedback on content, skills, and formatting. The project was built to help users quickly understand the strengths and weaknesses of their resumes and improve them for better job opportunities.

TECH STACK:

Backend: Python, FastAPI
AI Layer: Pydantic AI
Frontend: HTML, CSS, JavaScript

PROJECT STRUCTURE:

ai-resume-evaluator/
├─ backend/
│   ├─ main.py
│   └─ requirements.txt
├─ frontend/
│   ├─ index.html
│   ├─ style.css
│   └─ script.js
├─ new_screenshots/
│   ├─ screenshot1.jpeg
│   └─ screenshot2.jpeg
├─ README.md
└─ .gitignore

ARCHITECTURE:

The frontend communicates with the FastAPI backend via API calls. The backend uses Pydantic AI to process input text, evaluate the resume, and return structured feedback to the frontend. This allows users to interact with the AI in real-time through a simple web interface.