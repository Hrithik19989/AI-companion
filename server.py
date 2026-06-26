import os
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv

# Load environment variables from .env (project-local)
load_dotenv()


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_PATH = os.path.join(BASE_DIR, "system_prompt.txt")


def load_personality() -> str:
    try:
        with open(PROMPT_PATH, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""


def generate_response(user_text: str) -> str:
    personality = load_personality()

    if not user_text.strip():
        return "Say something and I’ll answer out loud."

    # -------- ADK/Python LLM integration (OpenAI-compatible) --------
    # Env vars:
    # - OPENAI_API_KEY (required)
    # - OPENAI_MODEL (optional, default: gpt-4o-mini)
    # - OPENAI_BASE_URL (optional for compatible endpoints)
    api_key = os.environ.get("OPENAI_API_KEY")
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    if not api_key:
        # Keep app usable without keys.
        if user_text.lower().startswith("hi") or "hello" in user_text.lower():
            return "Hi! I’m here. Add an OPENAI_API_KEY to enable real intelligence."
        return "I’m not connected to a language model yet. Set OPENAI_API_KEY to enable full responses."

    try:
        from openai import OpenAI

        base_url = os.environ.get("OPENAI_BASE_URL")
        client_kwargs = {"api_key": api_key}
        if base_url:
            client_kwargs["base_url"] = base_url

        client = OpenAI(**client_kwargs)

        messages = []
        if personality:
            messages.append({"role": "system", "content": personality})

        # Keep it short for mouth animation.
        messages.append(
            {
                "role": "user",
                "content": user_text.strip(),
            }
        )

        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
        )

        content = (resp.choices[0].message.content or "").strip()
        return content if content else "Got it."
    except Exception as e:
        # Avoid breaking the UI, but expose useful info during development.
        err = str(e)
        if "429" in err or "quota" in err:
            return "I’m connected, but my API quota is exhausted (429). Check billing/plan and try again."
        return "I tried to think, but something went wrong. Try again."


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    response_text = generate_response(message)
    return jsonify({"response": response_text})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/app.js")
def js():
    return send_from_directory(BASE_DIR, "app.js")


@app.route("/styles.css")
def css():
    return send_from_directory(BASE_DIR, "styles.css")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)

