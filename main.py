from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from datetime import datetime, timezone

app = FastAPI()

@app.get("/me", response_class=JSONResponse)
def get_profile():
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        fact = response.json().get("fact", "Could not fetch cat fact.")
    except Exception:
        fact = "Cat fact unavailable at the moment. Try again later."

    data = {
        "status": "success",
        "user": {
            "email": "amy1234obetta@gmail.com",
            "name": "Ege-Obetta Amarachi",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": fact
    }

    return JSONResponse(content=data)


