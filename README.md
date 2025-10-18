# 🧙‍♀️ Backend Track — Stage 0 Task  
### Build a Dynamic Profile Endpoint with FastAPI

This project implements a simple RESTful API that returns my profile information along with a dynamic cat fact fetched from an external API.  
It’s built using **Python (FastAPI)** as part of the **Backend Wizards Stage 0** task.

---

## 🚀 Endpoint

**GET `/me`**

### ✅ Response Format
```json
{
  "status": "success",
  "user": {
    "email": "amarachiegeobetta@gmail.com",
    "name": "Ege-Obetta Amarachi Naomi",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-15T12:34:56.789Z",
  "fact": "Cats sleep for 70% of their lives."
}
```
## Features

1. Returns user profile data (email, name, stack)
2. Fetches a new random cat fact on every request
3. Shows current UTC timestamp in ISO 8601 format
4. Handles network failures gracefully
5. Fast and lightweight API using FastAPI


## Setup Instructions

1.  **Clone the repository**
```bash
git clone https://github.com/Amarachi2006/HNG-Task0.git
cd HNG-Task0
```
2.  **Create and activate virtual environment**
```bash
python -m venv .venv
# Activate it
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```
3.  **Install dependencies**
```bash
pip install -r requirements.txt
```
4.  **Run the FastAPI app**
```bash
uvicorn main:app --reload
```
5.  **Test the endpoint**
```bash
http://127.0.0.1:8000/me
```

## Project Structure
```
HNG-Task0/
├── main.py              # Core FastAPI app
├── requirements.txt     # Dependencies
├── README.md            # Documentation
└── .gitignore           # Ignored files/folders
```
