# Stage 0 Backend Profile API

## Overview
- Lightweight FastAPI service for the HNG Stage 0 backend task
- Exposes a single `/me` endpoint that returns profile information and a live cat fact
- Fetches cat facts from https://catfact.ninja/fact with graceful fallbacks when the upstream API fails
- Uses environment variables so you can ship the same code without hard‑coding personal details

## Tech Stack
- Python (>= 3.13)
- FastAPI with the standard extras bundle
- Requests (via the FastAPI standard extras) for outbound HTTP calls
- Uvicorn for local development server
- python-dotenv for loading configuration from a `.env` file

## Prerequisites
- Python 3.13 or newer installed
- Git (optional, for cloning the repository)
- Internet connectivity for fetching cat facts while the service runs

## Installation
1. Clone the repository and switch into the project folder:
	```bash
	git clone <your-repo-url>
	cd hng/stage0
	```
2. Create and activate a virtual environment (Windows PowerShell shown; adapt for your shell if different):
	```powershell
	py -m venv .venv
	.venv\Scripts\Activate.ps1
	```
3. Install dependencies via `pip` using the `pyproject.toml` metadata:
	```bash
	pip install -e .
	```

## Environment Variables
Create a `.env` file in `stage0/` (it is ignored by Git by default) with the following keys:
```env
EMAIL=you@example.com
NAME=Your Full Name
STACK=Python/FastAPI
```
These values are injected into the `/me` payload so your personal details never live in source control.

## Running Locally
1. Ensure your virtual environment is active.
2. Start the FastAPI development server with Uvicorn:
	```bash
	uvicorn server:app --reload --host 0.0.0.0 --port 8000
	```
3. Visit `http://127.0.0.1:8000/me` in your browser or use `curl` to inspect the response:
	```bash
	curl http://127.0.0.1:8000/me
	```

## API Reference
- **GET** `/me`
  - **200 OK**
  - **Response Body:**
	 ```json
	 {
		"status": "success",
		"user": {
		  "email": "you@example.com",
		  "name": "Your Full Name",
		  "stack": "Python/FastAPI"
		},
		"timestamp": "2025-10-15T12:34:56.789Z",
		"fact": "Cats sleep 70% of their lives."
	 }
	 ```
  - **Notes:** Every request triggers a fresh call to the Cat Facts API. If that call fails, the service responds with a friendly fallback message while still returning `200 OK`.

## Logging & Error Handling
- The service logs upstream API failures to the console for quick diagnosis in development.
- A default message is returned if the cat facts provider is unreachable or slow.
- Request timeouts are capped at 30 seconds to prevent hanging responses.

## Testing
- Automated tests are not included yet. You can manually verify the endpoint with `curl`, HTTP clients such as Postman, or by writing `pytest` suites around `FastAPI`'s TestClient.

## Deployment Tips
- Use a production-grade ASGI server (e.g., Uvicorn with Gunicorn, Hypercorn, or another ASGI host) when deploying.
- Provision environment variables (`EMAIL`, `NAME`, `STACK`) in your hosting platform.
- Make sure outbound HTTPS traffic is allowed so the service can reach `catfact.ninja`.

## Useful Links
- FastAPI documentation: https://fastapi.tiangolo.com/
- Cat Fact API reference: https://catfact.ninja/
- Uvicorn documentation: https://www.uvicorn.org/

