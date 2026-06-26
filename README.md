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

# (Optional) If using the backend with Ollama/OpenAI-compatible LLM
python -m pip install openai requests beautifulsoup4 lxml

```

### Enable real intelligence (LLM)
The backend uses an **OpenAI-compatible** chat-completions endpoint.

#### Option A) Local Ollama (free)
1) Make sure Ollama is running.
2) Install a model in Ollama (example: `llama3.2:1b`).
3) The project already includes a project-local `.env` configured for Ollama:
- `OPENAI_BASE_URL=http://localhost:11434/v1`
- `OPENAI_API_KEY=ollama` (dummy)
- `OPENAI_MODEL=llama3.2:1b`

#### Option B) OpenAI API (paid)
Set environment variables:
- `OPENAI_API_KEY` (required)
- `OPENAI_MODEL` (optional, default: `gpt-4o-mini`)
- `OPENAI_BASE_URL` (optional, if using a compatible provider)

Example (Windows):

```bat
set OPENAI_API_KEY=your_key_here
```

If `OPENAI_API_KEY` is not set, the UI will still work, but you’ll get a message telling you to add the key.


## Run
Start the backend:

```bash
cd "d:\Python\PY Projects\AI Companion" && .venv\Scripts\python server.py
```


The server runs on:
- http://127.0.0.1:5000

> If you want to use Ollama, ensure your model is available in Ollama:
> - http://localhost:11434/v1/models


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
- Add “superpowers” via tool endpoints (internet search, etc.)
- Generate a unique avatar asset

