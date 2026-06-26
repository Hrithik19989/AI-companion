# TODO - AI Companion Puppet (Web)

- [ ] Step 1: Create initial web frontend (`index.html`, `styles.css`, `app.js`)
  - [ ] Face + mouth element
  - [ ] Chat input UI
  - [ ] Speech output (Web Speech API)
  - [ ] Mouth animation sync (best-effort)

- [ ] Step 2: Create backend server (`server.py`)
  - [ ] Serve an API endpoint `/chat`
  - [ ] Load personality from `system_prompt.txt`
  - [ ] Generate response (placeholder first)

- [x] Step 3: Wire frontend -> backend `/chat`
  - [x] Send user message
  - [x] Render AI response text
  - [x] Speak response out loud and animate mouth

- [x] Step 4: Run & verify end-to-end
  - [x] Start backend
  - [ ] Open frontend in browser

- [ ] Step 5: Replace placeholder brain with real ADK/Python LLM integration
  - [ ] Add LLM client to `server.py`
  - [ ] Inject `system_prompt.txt`
  - [ ] Add basic conversation history

- [ ] Step 6: Add tools (internet access/search) endpoint + LLM tool calling
  - [ ] Add `GET /tools/search?q=...`
  - [ ] Add tool usage guidance to `system_prompt.txt`

- [ ] Step 7: Add avatar generation pipeline
  - [ ] Generate unique avatar asset (SVG/PNG)
  - [ ] Serve it from Flask and render in `index.html`

- [ ] Step 8: Update README with env var setup (LLM key)

