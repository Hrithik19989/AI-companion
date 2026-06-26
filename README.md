# AI Companion Puppet (Visual + Voice)

A simple interactive “puppet” web companion: you type a message, it responds with text **and** speaks out loud, while its mouth animates.

## Project layout
- `index.html` - Frontend UI (puppet face, chat log, input)
- `styles.css` - Styling + mouth animation
- `app.js` - Frontend logic (calls backend, speaks response)
- `server.py` - Backend API (`/chat`, `/health`)
- `system_prompt.txt` - Personality instructions loaded by the backend

## Requirements
- Python 3.10+
- Flask
- A browser that supports the Web Speech API (`speechSynthesis`) for voice.

## Setup
From the project folder:

```bash
cd "d:\Python\PY Projects\AI Companion"
python -m pip install flask==3.0.3
```

## Run
Start the backend:

```bash
cd "d:\Python\PY Projects\AI Companion" && python server.py
```

The server runs on:
- http://127.0.0.1:5000

## Use
1. Open `index.html` in your browser.
2. Type a message and press **Send**.
3. The puppet will:
   - display the response text
   - speak it out loud
   - animate the mouth while speaking (best-effort; depends on browser capabilities)

## API
### `POST /chat`
Request JSON:
```json
{ "message": "Hello" }
```
Response JSON:
```json
{ "response": "Hi! I’m here. What would you like to talk about?" }
```

### `GET /health`
Returns:
```json
{ "status": "ok" }
```

## Next steps (planned)
- Replace the placeholder “brain” in `server.py` with a real ADK/Python LLM integration
- Add “superpowers” via tool endpoints (internet search, etc.)
- Generate a unique avatar asset

