## Dynamic Profile API

Single-file FastAPI app exposing GET /me.

Quick start

Dependencies: fastapi[standard], python-dotenv, uvicorn.

1. Create `.env` with EMAIL, NAME, STACK.
2. Create and activate a virtualenv, then install:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

Run:

```powershell
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

Endpoint

- GET /me — returns 200 with JSON:

```json
{
	"status": "success",
	"user": {"email": "you@example.com", "name": "Your Full Name", "stack": "Python/FastAPI"},
	"timestamp": "2025-10-15T12:34:56.789Z",
	"fact": "A cat fact fetched from https://catfact.ninja/fact"
}
```

Notes

- Timestamp is current UTC in ISO8601 with Z suffix.
- Cat fact is fetched on every request; a fallback message is returned if upstream fails.
- ENV vars keep personal info out of source.
