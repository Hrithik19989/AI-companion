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

- [ ] Step 3: Wire frontend -> backend `/chat`
  - [ ] Send user message
  - [ ] Render AI response text
  - [ ] Speak response out loud and animate mouth

- [x] Step 4: Run & verify end-to-end
  - [x] Start backend
  - [ ] Open frontend in browser


- [ ] Step 5 (next iteration): Replace placeholder brain with ADK/Python LLM integration

- [ ] Step 6 (next iteration): Add tools (internet access/search) endpoint + UI

- [ ] Step 7 (next iteration): Add avatar generation pipeline

