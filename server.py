import os
from flask import Flask, request, jsonify, send_from_directory

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
    # Placeholder brain. Next iteration: replace with real ADK/Python LLM integration.
    personality = load_personality()
    if not user_text.strip():
        return "Say something and I’ll answer out loud."

    # Simple personality-tinted echo.
    # Keep it short for the mouth animation.
    if user_text.lower().startswith("hi") or "hello" in user_text.lower():
        return "Hi! I’m here. What would you like to talk about?"

    # Include a tiny bit of character without being too verbose.
    return f"I heard you: '{user_text.strip()}'. Tell me more!"


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

