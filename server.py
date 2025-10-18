from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from datetime import datetime, timezone
import os
import dotenv
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

dotenv.load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CATFACT_URL = "https://catfact.ninja/fact"

EMAIL = os.getenv("EMAIL")
NAME = os.getenv("NAME")
STACK = os.getenv("STACK")
REQUEST_TIMEOUT = 30

@app.get("/me")
async def me() -> JSONResponse:
    fact = "Could not fetch a cat fact at this time because all the cats are playing with the wires in the server room."

    try:
        with requests.get(
            url=CATFACT_URL,
            timeout=REQUEST_TIMEOUT
            ) as r:
            if r.status_code == 200:
                payload = r.json()
                fact = payload.get("fact", fact)
            else:
                raise Exception(r.status_code)
    except Exception as e:
        print(f"Error: {e}")
        

    timestamp = datetime.now(timezone.utc).isoformat()
    headers={
        "Content-Type":"application/json"
    }
    content={
        "status": "success",
        "user": {
            "email": EMAIL,
            "name": NAME,
            "stack": STACK
        },
        "timestamp": timestamp,
        "fact": fact
    }
    return JSONResponse(content=content, headers=headers)
