# Stage 0 Profile API

FastAPI service that returns profile info + a random cat fact.

## Setup

**Dependencies:** `fastapi[standard]`, `python-dotenv`, `uvicorn`

1. Create `.env` file:
   ```env
   EMAIL=your@email.com
   NAME=Your Name
   STACK=Python/FastAPI
   ```

2. Install:
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -e .
   ```

3. Run:
   ```powershell
   uvicorn server:app --reload --host 0.0.0.0 --port 8000
   ```

## API

**GET /me**

Returns your profile with a cat fact from [catfact.ninja](https://catfact.ninja/fact).

Response:
```json
{
  "status": "success",
  "user": {
    "email": "your@email.com",
    "name": "Your Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-18T12:34:56.789Z",
  "fact": "Cats sleep 70% of their lives."
}
```

- Timestamp is current UTC in ISO 8601 format
- New cat fact fetched on every request
- Fallback message if API fails