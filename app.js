const chatLog = document.getElementById('chatLog');
const composer = document.getElementById('composer');
const messageInput = document.getElementById('messageInput');
const statusEl = document.getElementById('status');
const mouthEl = document.getElementById('mouth');

let speaking = false;
let currentUtterance = null;

function addMessage(role, text){
  const wrap = document.createElement('div');
  wrap.className = `msg msg--${role}`;

  const bubble = document.createElement('div');
  bubble.className = 'msg__bubble';
  bubble.textContent = text;

  wrap.appendChild(bubble);
  chatLog.appendChild(wrap);
  chatLog.scrollTop = chatLog.scrollHeight;
}

function setStatus(text){
  statusEl.textContent = text;
}

function stopSpeech(){
  speaking = false;
  if (currentUtterance) {
    try { window.speechSynthesis.cancel(); } catch (e) {}
  }
  mouthEl.classList.remove('is-speaking');
}

function speak(text){
  stopSpeech();

  if (!('speechSynthesis' in window)) {
    setStatus('Speech synthesis not supported in this browser.');
    return;
  }

  const utter = new SpeechSynthesisUtterance(text);
  currentUtterance = utter;

  utter.onstart = () => {
    speaking = true;
    mouthEl.classList.add('is-speaking');
    setStatus('Speaking...');
  };

  // Best-effort mouth sync: when boundary events are supported, we keep the animation active.
  // Many browsers don’t expose phoneme/word boundaries consistently; fallback is duration-based.
  utter.onboundary = () => {
    if (!speaking) return;
    mouthEl.classList.add('is-speaking');
  };

  utter.onend = () => {
    speaking = false;
    mouthEl.classList.remove('is-speaking');
    setStatus('Ready.');
  };

  utter.onerror = () => {
    speaking = false;
    mouthEl.classList.remove('is-speaking');
    setStatus('Speech error.');
  };

  window.speechSynthesis.speak(utter);
}

async function sendMessage(message){
  const res = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  });

  if (!res.ok) {
    const txt = await res.text().catch(() => '');
    throw new Error(`HTTP ${res.status}: ${txt}`);
  }

  const data = await res.json();
  return data.response;
}

composer.addEventListener('submit', async (e) => {
  e.preventDefault();

  const text = messageInput.value.trim();
  if (!text) return;

  addMessage('user', text);
  messageInput.value = '';

  composer.querySelector('button[type="submit"]').disabled = true;
  setStatus('Thinking...');

  try {
    const reply = await sendMessage(text);
    addMessage('bot', reply);
    speak(reply);
  } catch (err) {
    console.error(err);
    addMessage('bot', 'Sorry—I got stuck. Try again.');
    setStatus('Error.');
    stopSpeech();
  } finally {
    composer.querySelector('button[type="submit"]').disabled = false;
  }
});

// If user focuses input, stop current speech so it doesn’t overlap.
messageInput.addEventListener('focus', () => stopSpeech());

