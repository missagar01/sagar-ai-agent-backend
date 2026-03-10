/**
 * Sagar TMT Pipes - Frontend Application with STREAMING
 * Features:
 * - Admin login authentication (JWT)
 * - Real-time streaming responses (word-by-word)
 * - Status updates during processing
 * - Session management (create, list, switch, delete)
 * - Chat history per session
 * - Query caching visualization
 * - Request cancellation
 */
const API_BASE_URL = window.location.protocol === 'file:'
  ? 'http://localhost:8000'
  : '/api';

// ============================================================================
// AUTH MODULE
// ============================================================================

function getAuthToken() {
  return localStorage.getItem('auth_token');
}

function getAuthHeaders() {
  const token = getAuthToken();
  const headers = { 'Content-Type': 'application/json' };
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  return headers;
}

async function authFetch(url, options = {}) {
  options.headers = { ...getAuthHeaders(), ...(options.headers || {}) };
  const response = await fetch(url, options);
  if (response.status === 401 || response.status === 403) {
    handleAuthFailure();
    throw new Error('Authentication required');
  }
  return response;
}

function handleAuthFailure() {
  localStorage.removeItem('auth_token');
  localStorage.removeItem('auth_user');
  document.getElementById('loginOverlay').style.display = 'flex';
  document.getElementById('appContainer').style.display = 'none';
}

async function verifyStoredToken() {
  const token = getAuthToken();
  if (!token) return false;

  try {
    const response = await fetch(`${API_BASE_URL}/auth/verify-token`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ token })
    });
    if (response.ok) {
      const data = await response.json();
      return data.valid === true;
    }
    return false;
  } catch {
    return false;
  }
}

async function initAuth() {
  const isValid = await verifyStoredToken();
  if (isValid) {
    document.getElementById('loginOverlay').style.display = 'none';
    document.getElementById('appContainer').style.display = 'flex';
    initApp();
  } else {
    localStorage.removeItem('auth_token');
    localStorage.removeItem('auth_user');
    document.getElementById('loginOverlay').style.display = 'flex';
    document.getElementById('appContainer').style.display = 'none';
  }
}

function setupLoginForm() {
  const loginForm = document.getElementById('loginForm');
  const loginBtn = document.getElementById('loginBtn');
  const loginBtnText = document.getElementById('loginBtnText');
  const loginSpinner = document.getElementById('loginSpinner');
  const loginError = document.getElementById('loginError');
  const loginErrorText = document.getElementById('loginErrorText');

  loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const login = document.getElementById('loginInput').value.trim();
    const password = document.getElementById('loginPassword').value;

    if (!login || !password) return;

    // Show loading state
    loginBtn.disabled = true;
    loginBtnText.textContent = 'Authenticating...';
    loginSpinner.style.display = 'inline-block';
    loginError.style.display = 'none';

    try {
      const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ login, password })
      });

      const data = await response.json();

      if (response.ok && data.success) {
        localStorage.setItem('auth_token', data.token);
        localStorage.setItem('auth_user', JSON.stringify(data.user));

        document.getElementById('loginOverlay').style.display = 'none';
        document.getElementById('appContainer').style.display = 'flex';
        initApp();
      } else {
        loginErrorText.textContent = data.detail || 'Access denied. Only authorized admin can access this system.';
        loginError.style.display = 'flex';
      }
    } catch (error) {
      loginErrorText.textContent = 'Connection error. Please try again.';
      loginError.style.display = 'flex';
    } finally {
      loginBtn.disabled = false;
      loginBtnText.textContent = 'Login';
      loginSpinner.style.display = 'none';
    }
  });
}

function setupLogout() {
  const logoutBtn = document.getElementById('logoutBtn');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', () => {
      localStorage.removeItem('auth_token');
      localStorage.removeItem('auth_user');
      document.getElementById('loginOverlay').style.display = 'flex';
      document.getElementById('appContainer').style.display = 'none';
      // Clear form
      document.getElementById('loginInput').value = '';
      document.getElementById('loginPassword').value = '';
      document.getElementById('loginError').style.display = 'none';
    });
  }
}

// DOM Elements
const chatDisplay = document.getElementById("chatDisplay");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const sendIcon = document.getElementById("sendIcon");
const welcomeScreen = document.getElementById("welcomeScreen");
const typingText = document.getElementById("typingText");
const sidebar = document.getElementById("sidebar");
const sessionList = document.getElementById("sessionList");
const newChatBtn = document.getElementById("newChatBtn");
const toggleSidebarBtn = document.getElementById("toggleSidebarBtn");
const clearChatBtn = document.getElementById("clearChatBtn");
const deleteChatBtn = document.getElementById("deleteChatBtn");
const cacheInfoBtn = document.getElementById("cacheInfoBtn");
const cacheModal = document.getElementById("cacheModal");
const closeCacheModal = document.getElementById("closeCacheModal");
const cacheModalBody = document.getElementById("cacheModalBody");
const clearCacheBtn = document.getElementById("clearCacheBtn");
const cacheIndicator = document.getElementById("cacheIndicator");
const clearOptionsModal = document.getElementById("clearOptionsModal");
const closeClearModal = document.getElementById("closeClearModal");
const confirmClearChatBtn = document.getElementById("confirmClearChat");
const confirmDeleteSessionBtn = document.getElementById("confirmDeleteSession");
const confirmClearCacheModalBtn = document.getElementById(
  "confirmClearCacheFromModal",
);

// State
let currentSessionId = null;
let isGenerating = false;
let currentRequestId = null;
let abortController = null;

// ============================================================================
// INITIALIZATION
// ============================================================================

document.addEventListener("DOMContentLoaded", () => {
  setupLoginForm();
  setupLogout();
  initAuth();
});

function initApp() {
  startTypingAnimation();
  loadSessions();
  setupEventListeners();
}

function setupEventListeners() {
  sendBtn.addEventListener("click", sendMessage);
  userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter" && !isGenerating) {
      e.preventDefault();
      sendMessage();
    }
  });

  newChatBtn.addEventListener("click", createNewSession);
  toggleSidebarBtn.addEventListener("click", toggleSidebar);

  // Mobile Close Button Listener
  const closeSidebarMobile = document.getElementById("closeSidebarMobile");
  if (closeSidebarMobile) {
    closeSidebarMobile.addEventListener("click", () => {
      sidebar.classList.add("collapsed");
      sidebarOverlay.classList.remove("active");
    });
  }

  // Clear Button opens Modal now
  clearChatBtn.addEventListener("click", openClearModal);

  // Legacy delete button still works directly
  deleteChatBtn.addEventListener("click", deleteCurrentSession);

  cacheInfoBtn.addEventListener("click", showCacheStats);
  closeCacheModal.addEventListener(
    "click",
    () => (cacheModal.style.display = "none"),
  );
  clearCacheBtn.addEventListener("click", clearCache);

  // Clear Modal Listeners
  closeClearModal.addEventListener(
    "click",
    () => (clearOptionsModal.style.display = "none"),
  );
  confirmClearChatBtn.addEventListener("click", () => {
    clearCurrentChat(true);
    clearOptionsModal.style.display = "none";
  });
  confirmDeleteSessionBtn.addEventListener("click", () => {
    deleteCurrentSession(true);
    clearOptionsModal.style.display = "none";
  });
  confirmClearCacheModalBtn.addEventListener("click", () => {
    clearCache();
    clearOptionsModal.style.display = "none";
  });

  // Close modals on outside click
  window.addEventListener("click", (e) => {
    if (e.target === cacheModal) cacheModal.style.display = "none";
    if (e.target === clearOptionsModal)
      clearOptionsModal.style.display = "none";
  });
}

function openClearModal() {
  clearOptionsModal.style.display = "flex";
}

// ============================================================================
// TYPING ANIMATION
// ============================================================================

let typingAnimationActive = false;
let typingTimeoutId = null;

function startTypingAnimation() {
  const typingElement = document.getElementById("typingText");
  if (!typingElement) return;

  // Clear any existing animation state
  if (typingTimeoutId) {
    clearTimeout(typingTimeoutId);
  }

  const text = "Ask Anything....";
  let i = 0;
  typingElement.textContent = "";

  function type() {
    const currentTypingElement = document.getElementById("typingText");
    if (!currentTypingElement) {
      typingAnimationActive = false;
      return;
    }

    if (i < text.length) {
      currentTypingElement.textContent += text.charAt(i);
      i++;
      typingTimeoutId = setTimeout(type, 100);
    } else {
      typingTimeoutId = setTimeout(() => {
        i = 0;
        if (currentTypingElement) currentTypingElement.textContent = "";
        type();
      }, 2000);
    }
  }

  typingAnimationActive = true;
  type();
}

// ============================================================================
// SESSION MANAGEMENT
// ============================================================================

async function loadSessions() {
  try {
    const response = await authFetch(`${API_BASE_URL}/chat/sessions`);
    const sessions = await response.json();

    renderSessionList(sessions);

    if (sessions.length > 0 && !currentSessionId) {
      selectSession(sessions[0].session_id);
    }
  } catch (error) {
    console.error("Failed to load sessions:", error);
  }
}

function renderSessionList(sessions) {
  sessionList.innerHTML = "";

  sessions.forEach((session) => {
    const item = document.createElement("div");
    item.className = `session-item ${session.session_id === currentSessionId ? "active" : ""}`;
    item.dataset.sessionId = session.session_id;

    item.innerHTML = `
            <div class="session-info">
                <div class="session-title">${escapeHtml(session.title)}</div>
                <div class="session-meta">${session.message_count} messages</div>
            </div>
            <button class="session-delete" title="Delete session">
                <i class="fas fa-times"></i>
            </button>
        `;

    item.querySelector(".session-info").addEventListener("click", () => {
      selectSession(session.session_id);
      if (window.innerWidth <= 768) {
        sidebar.classList.add("collapsed");
        sidebarOverlay.classList.remove("active");
      }
    });

    item.querySelector(".session-delete").addEventListener("click", (e) => {
      e.stopPropagation();
      deleteSession(session.session_id);
    });

    sessionList.appendChild(item);
  });
}

async function selectSession(sessionId) {
  currentSessionId = sessionId;

  document.querySelectorAll(".session-item").forEach((item) => {
    item.classList.toggle("active", item.dataset.sessionId === sessionId);
  });

  updateSessionIndicator();
  await loadSessionMessages(sessionId);
}

async function loadSessionMessages(sessionId) {
  try {
    const response = await authFetch(
      `${API_BASE_URL}/chat/sessions/${sessionId}/messages`,
    );
    const data = await response.json();

    chatDisplay.innerHTML = "";

    if (data.messages.length === 0) {
      chatDisplay.innerHTML = `
                <div class="welcome-screen" id="welcomeScreen">
                    <div class="welcome-orb"></div>
                    <h1 id="typingText"></h1>
                    <p class="welcome-subtitle">Your intelligent database assistant</p>
                </div>
            `;
      startTypingAnimation();
    } else {
      data.messages.forEach((msg) => {
        addMessage(msg.content, msg.role === "user" ? "user" : "bot", false);
      });
    }

    chatDisplay.scrollTop = chatDisplay.scrollHeight;
  } catch (error) {
    console.error("Failed to load messages:", error);
  }
}

async function createNewSession() {
  try {
    const response = await authFetch(`${API_BASE_URL}/chat/sessions`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({}),
    });

    const session = await response.json();
    currentSessionId = session.session_id;

    await loadSessions();
    selectSession(session.session_id);

    chatDisplay.innerHTML = `
            <div class="welcome-screen" id="welcomeScreen">
                <div class="welcome-orb"></div>
                <h1 id="typingText"></h1>
                <p class="welcome-subtitle">Your intelligent database assistant</p>
            </div>
        `;
    startTypingAnimation();
  } catch (error) {
    console.error("Failed to create session:", error);
  }
}

async function deleteSession(sessionId, skipConfirm = false) {
  console.log(
    `Attempting to delete session: ${sessionId}, skipConfirm: ${skipConfirm}`,
  );

  if (!skipConfirm) {
    const confirmed = await showConfirmDialog(
      "Are you sure you want to delete this conversation?",
    );
    if (!confirmed) {
      console.log("Delete cancelled by user");
      return;
    }
  }

  try {
    const response = await authFetch(`${API_BASE_URL}/chat/sessions/${sessionId}`, {
      method: "DELETE",
    });

    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

    console.log("Session deleted successfully");

    if (sessionId === currentSessionId) {
      currentSessionId = null;
    }

    await loadSessions();

    if (!currentSessionId) {
      await createNewSession();
    }

    // visual feedback for successful deletion helps confirm action happened
    // alert("Session deleted successfully"); // Optional, maybe annoying if frequent?
  } catch (error) {
    console.error("Failed to delete session:", error);
    showSystemMessage(`Failed to delete session: ${error.message}`, "error");
  }
}

async function deleteCurrentSession(skipConfirm = false) {
  if (!currentSessionId) {
    console.error("No active session to delete");
    showSystemMessage("No active session selected", "error");
    return;
  }
  await deleteSession(currentSessionId, skipConfirm);
}

async function clearCurrentChat(skipConfirm = false) {
  if (!currentSessionId) return;

  if (!skipConfirm) {
    const confirmed = await showConfirmDialog(
      "Clear all messages in this conversation?",
    );
    if (!confirmed) return;
  }

  try {
    const response = await authFetch(
      `${API_BASE_URL}/chat/sessions/${currentSessionId}/clear`,
      {
        method: "POST",
      },
    );
    const result = await response.json();

    await loadSessionMessages(currentSessionId);
    await loadSessions();

    showSystemMessage(result.message, "success");
  } catch (error) {
    console.error("Failed to clear chat:", error);
    showSystemMessage("Failed to clear chat", "error");
  }
}

function updateSessionIndicator() {
  if (currentSessionId) {
    sessionIndicator.innerHTML = `<i class="fas fa-circle"></i> Active Session`;
  } else {
    sessionIndicator.innerHTML = `<i class="fas fa-circle"></i> New Session`;
  }
}

// ============================================================================
// STREAMING CHAT FUNCTIONALITY
// ============================================================================

async function sendMessage() {
  if (isGenerating) {
    return; // Strictly disable send action while generating
  }

  const question = userInput.value.trim();
  if (!question) return;

  // Create session if none exists
  if (!currentSessionId) {
    try {
      const response = await authFetch(`${API_BASE_URL}/chat/sessions`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({}),
      });
      const session = await response.json();
      currentSessionId = session.session_id;
      await loadSessions();
    } catch (error) {
      console.error("Failed to create session:", error);
      showSystemMessage("Failed to create session: " + error.message, "error");
      return;
    }
  }

  // Set generating state
  isGenerating = true;
  abortController = new AbortController();

  // Disable send button but KEEP INPUT ENABLED
  sendBtn.disabled = true;
  sendBtn.style.opacity = "0.5";
  sendBtn.style.cursor = "not-allowed";
  // userInput.disabled = true; // REMOVED per requirements

  // Hide welcome screen
  const welcomeEl = document.getElementById("welcomeScreen");
  if (welcomeEl) {
    welcomeEl.remove();
  }

  // Add user message
  addMessage(question, "user");
  userInput.value = "";

  // Add bot message container with status
  const botMsgId = addMessage("", "bot");
  const botMsgDiv = document.getElementById(botMsgId);

  // Create status and content containers
  botMsgDiv.innerHTML = `
        <div class="stream-status" id="streamStatus-${botMsgId}">
            <div class="status-dot"></div>
            <span>Thinking...</span>
        </div>
        <div class="stream-content" id="streamContent-${botMsgId}"></div>
    `;

  const statusDiv = document.getElementById(`streamStatus-${botMsgId}`);
  const contentDiv = document.getElementById(`streamContent-${botMsgId}`);

  // Hide cache indicator
  cacheIndicator.style.display = "none";

  let fullText = "";
  let isCacheHit = false;

  try {
    // Use streaming endpoint
    const response = await fetch(`${API_BASE_URL}/chat/stream`, {
      method: "POST",
      headers: getAuthHeaders(),
      body: JSON.stringify({
        question,
        session_id: currentSessionId,
      }),
      signal: abortController.signal,
    });

    if (!response.ok) throw new Error("Network response was not ok");

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      const chunk = decoder.decode(value, { stream: true });
      const lines = chunk.split("\n");

      // SMART SCROLL: Check if user is near bottom BEFORE updating content
      // Threshold of 100px. If user is within 100px of bottom, we auto-scroll.
      const threshold = 150;
      const isNearBottom =
        chatDisplay.scrollHeight -
        chatDisplay.scrollTop -
        chatDisplay.clientHeight <
        threshold;

      for (const line of lines) {
        if (!line.trim() || !line.startsWith("data: ")) continue;

        try {
          const jsonStr = line.replace("data: ", "").trim();
          if (!jsonStr) continue;

          const data = JSON.parse(jsonStr);

          switch (data.type) {
            case "status":
              // Always show "Thinking..." regardless of backend status message
              statusDiv.innerHTML = `
                                <div class="status-dot active"></div>
                                <span>Thinking...</span>
                            `;
              break;

            case "cache_hit":
              isCacheHit = data.value;
              if (isCacheHit) {
                statusDiv.innerHTML = `
                                    <div class="status-dot cached"></div>
                                    <span>⚡ Using cached query</span>
                                `;
              }
              break;

            case "sql":
              statusDiv.innerHTML = `
                                <div class="status-dot active"></div>
                                <span>Thinking...</span>
                            `;
              break;

            case "chunk":
              if (statusDiv.style.display !== "none") {
                statusDiv.style.display = "none";
              }
              fullText += data.content;

              // Render markdown incrementally
              // CLEANUP: Silently hide (Note: ...) technical sections at the end
              let displayContent = fullText;

              // Hide internal logging messages
              if (displayContent.includes("Validation failed") ||
                displayContent.includes("LLM 1:") ||
                displayContent.includes("LLM 2:") ||
                displayContent.includes("Generating query") ||
                displayContent.includes("Storing schema context") ||
                displayContent.includes("❌")) {
                // We just don't parse these specific segments at all to keep UI clean
                displayContent = "";
              }

              const noteRegex = /\n*\s*\(Note:[\s\S]*$/i;
              if (noteRegex.test(displayContent)) {
                displayContent = displayContent.replace(noteRegex, "").trim();
              }

              const techNoteRegex = /\n*\s*Technical note:[\s\S]*$/i;
              if (techNoteRegex.test(displayContent)) {
                displayContent = displayContent.replace(techNoteRegex, "").trim();
              }

              if (displayContent) {
                try {
                  let rendered = marked.parse(displayContent);
                  rendered = rendered.replace(
                    /<table>/g,
                    '<div class="table-wrapper"><table>',
                  );
                  rendered = rendered.replace(/<\/table>/g, "</table></div>");
                  contentDiv.innerHTML = rendered;
                } catch (e) {
                  contentDiv.innerText = displayContent;
                }
              } else if (!statusDiv.style.display || statusDiv.style.display === "none") {
                // If we hid the content and the status div is also hidden, we should show the thinking state
                statusDiv.style.display = "flex";
                statusDiv.innerHTML = `
                                <div class="status-dot active"></div>
                                <span>Thinking...</span>
                            `;
              }
              break;

            case "done":
              if (isCacheHit) {
                botMsgDiv.classList.add("cached");
                cacheIndicator.style.display = "flex";
              }
              await loadSessions();
              break;

            case "error":
              statusDiv.style.display = "none";
              contentDiv.innerHTML = `<div class="error" style="color: #ff4d4d;">${data.message}</div>`;
              break;
          }
        } catch (parseError) {
          console.log("Parse error for line:", line);
        }
      }

      // SMART SCROLL: Apply scroll ONLY if criteria met
      if (isNearBottom) {
        chatDisplay.scrollTop = chatDisplay.scrollHeight;
      }
    }
  } catch (error) {
    if (error.name === "AbortError") {
      statusDiv.style.display = "none";
      if (fullText) {
        contentDiv.innerHTML +=
          '<p class="stopped-indicator">(Stopped by user)</p>';
      } else {
        contentDiv.innerHTML =
          '<p class="stopped-indicator">(Stopped by user)</p>';
      }
    } else {
      statusDiv.style.display = "none";
      contentDiv.innerHTML = `<div class="error" style="color: #ff4d4d;">Connection error: ${error.message}</div>`;
    }
  } finally {
    isGenerating = false;
    currentRequestId = null;
    abortController = null;

    // Restore Send Button
    sendIcon.className = "fas fa-arrow-up";
    sendBtn.disabled = false;
    sendBtn.style.opacity = "1";
    sendBtn.style.cursor = "pointer";

    // Focus back on input so user can type next query immediately
    userInput.focus();

    // Final scroll check
    const threshold = 150;
    const isNearBottom =
      chatDisplay.scrollHeight -
      chatDisplay.scrollTop -
      chatDisplay.clientHeight <
      threshold;
    if (isNearBottom) chatDisplay.scrollTop = chatDisplay.scrollHeight;
  }
}

function stopGeneration() {
  // Legacy function, might not be triggered via UI anymore but good to keep clean
  if (abortController) {
    abortController.abort();
  }
  isGenerating = false;
  sendIcon.className = "fas fa-arrow-up";
  sendBtn.disabled = false;
  sendBtn.style.opacity = "1";
  sendBtn.style.cursor = "pointer";
  userInput.focus();
}

/**
 * System Message Helper (Replaces Alerts)
 */
function showSystemMessage(message, type = "info") {
  const msgDiv = document.createElement("div");
  msgDiv.className = "message system";
  msgDiv.innerHTML = `
        <div class="system-msg-content ${type}">
            <i class="fas ${type === "error" ? "fa-exclamation-circle" : "fa-info-circle"}"></i>
            <span>${message}</span>
        </div>
    `;
  chatDisplay.appendChild(msgDiv);
  chatDisplay.scrollTop = chatDisplay.scrollHeight;

  // Auto-dismiss logic
  setTimeout(() => {
    // Fade out transition
    msgDiv.style.transition = "opacity 0.5s ease, margin-top 0.5s ease";
    msgDiv.style.opacity = "0";
    msgDiv.style.marginTop = "-50px"; // Slide up effect

    // Remove from DOM after transition completes
    setTimeout(() => {
      if (msgDiv.parentNode) {
        msgDiv.remove();
      }
    }, 500);
  }, 3000); // 3 seconds delay
}

function addMessage(text, type, animate = true) {
  const messageDiv = document.createElement("div");
  const id = "msg-" + Math.random().toString(36).substr(2, 9);
  messageDiv.id = id;
  messageDiv.className = `message ${type}`;

  if (!animate) {
    messageDiv.style.animation = "none";
  }

  if (type.includes("bot") && text) {
    // CLEANUP: Remove (Note: ...) section from view
    let cleanedText = text;
    const noteRegex = /\n*\s*\(Note:[\s\S]*$/i;
    if (noteRegex.test(text)) {
      cleanedText = text.replace(noteRegex, "").trim();
    }

    const techNoteRegex = /\n*\s*Technical note:[\s\S]*$/i;
    if (techNoteRegex.test(cleanedText)) {
      cleanedText = cleanedText.replace(techNoteRegex, "").trim();
    }

    try {
      let renderedHtml = marked.parse(cleanedText);
      renderedHtml = renderedHtml.replace(
        /<table>/g,
        '<div class="table-wrapper"><table>',
      );
      renderedHtml = renderedHtml.replace(/<\/table>/g, "</table></div>");
      messageDiv.innerHTML = renderedHtml;
    } catch (e) {
      messageDiv.innerText = cleanedText;
    }
  } else if (text) {
    messageDiv.innerText = text;
  }

  chatDisplay.appendChild(messageDiv);
  chatDisplay.scrollTop = chatDisplay.scrollHeight;
  return id;
}

// ============================================================================
// SIDEBAR
// ============================================================================

// ============================================================================
// SIDEBAR
// ============================================================================

const sidebarOverlay = document.getElementById("sidebarOverlay");

function toggleSidebar() {
  const isMobile = window.innerWidth <= 768;

  sidebar.classList.toggle("collapsed");

  if (isMobile) {
    if (sidebar.classList.contains("collapsed")) {
      sidebarOverlay.classList.remove("active");
      document.body.style.overflow = ""; // Restore scroll
    } else {
      sidebarOverlay.classList.add("active");
      document.body.style.overflow = "hidden"; // Prevent scroll when sidebar is open
    }
  }
}

// Mobile Sidebar Initialization
function initSidebar() {
  // Determine initial state
  if (window.innerWidth <= 768) {
    sidebar.classList.add("collapsed");
    sidebarOverlay.classList.remove("active");
  }

  // Close sidebar when clicking overlay
  if (sidebarOverlay) {
    sidebarOverlay.addEventListener("click", () => {
      sidebar.classList.add("collapsed");
      sidebarOverlay.classList.remove("active");
      document.body.style.overflow = "";
    });
  }

  // Handle Resize events
  window.addEventListener("resize", () => {
    if (window.innerWidth > 768) {
      // Moving to Desktop
      sidebarOverlay.classList.remove("active");
      sidebar.classList.remove("collapsed"); // Always show sidebar on desktop unless user manually collapses
      document.body.style.overflow = "";
    } else {
      // Moving to Mobile
      if (!sidebar.classList.contains("collapsed")) {
        sidebar.classList.add("collapsed"); // Ensure it starts closed on mobile resize
      }
      sidebarOverlay.classList.remove("active");
      document.body.style.overflow = "";
    }
  });
}
// Call Init immediately
initSidebar();

// ============================================================================
// CACHE MANAGEMENT
// ============================================================================

async function showCacheStats() {
  cacheModal.style.display = "flex";
  cacheModalBody.innerHTML = "Loading...";

  try {
    const response = await authFetch(`${API_BASE_URL}/chat/cache/stats`);
    const stats = await response.json();

    cacheModalBody.innerHTML = `
            <div class="stat-item">
                <span class="stat-label">Status</span>
                <span class="stat-value">${stats.enabled ? "✅ Enabled" : "❌ Disabled"}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Total Entries</span>
                <span class="stat-value">${stats.total_entries || 0}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Cache Hits</span>
                <span class="stat-value">${stats.cache_hits || 0}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Cache Misses</span>
                <span class="stat-value">${stats.cache_misses || 0}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Hit Rate</span>
                <span class="stat-value">${stats.hit_rate?.toFixed(1) || 0}%</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Threshold</span>
                <span class="stat-value">${((stats.similarity_threshold || 0.85) * 100).toFixed(0)}%</span>
            </div>
        `;
  } catch (error) {
    cacheModalBody.innerHTML = `<p style="color: var(--danger);">Failed to load cache stats: ${error.message}</p>`;
  }
}

async function clearCache() {
  const confirmed = await showConfirmDialog(
    "Are you sure you want to clear the System Cache?",
    "<strong>Note:</strong> This will delete all cached SQL queries. The next queries might take longer to process.",
  );
  if (!confirmed) return;
  try {
    const response = await authFetch(`${API_BASE_URL}/chat/cache/clear`, {
      method: "POST",
    });
    const result = await response.json();

    // Refresh cache stats if modal is open
    if (cacheModal.style.display !== "none") {
      await showCacheStats();
    }

    showSystemMessage(result.message, "success");
  } catch (error) {
    console.error("Failed to clear cache:", error);
    showSystemMessage("Failed to clear cache", "error");
  }
}

// ============================================================================
// UTILITIES
// ============================================================================

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

/**
 * Replaces native confirm() with a custom inline system message that has Yes/No buttons.
 * Returns a Promise that resolves to true (confirmed) or false (cancelled).
 */
/**
 * Shows the Global Confirmation Modal (Overlay)
 * Returns a Promise that resolves to true (confirmed) or false (cancelled).
 */
function showConfirmDialog(messageText, noteText = "") {
  return new Promise((resolve) => {
    const modal = document.getElementById("confirmationModal");
    const messageEl = document.getElementById("confirmMessage");
    const noteEl = document.getElementById("confirmNote");
    const closeBtn = document.getElementById("closeConfirmModal");
    const cancelBtn = document.getElementById("cancelConfirmBtn");
    const actionBtn = document.getElementById("actionConfirmBtn");

    // Set Content
    messageEl.textContent = messageText;

    if (noteText) {
      noteEl.innerHTML = noteText;
      noteEl.style.display = "block";
    } else {
      noteEl.style.display = "none";
    }

    // Show Modal
    modal.style.display = "flex";

    // Cleanup function to remove event listeners and hide modal
    let cleanup = () => {
      modal.style.display = "none";
      // Remove listeners to prevent duplicates next time
      closeBtn.removeEventListener("click", onClose);
      cancelBtn.removeEventListener("click", onCancel);
      actionBtn.removeEventListener("click", onAction);
      window.removeEventListener("click", onWindowClick);
    };

    // Handlers
    const onClose = () => {
      cleanup();
      resolve(false);
    };
    const onCancel = () => {
      cleanup();
      resolve(false);
    };
    const onAction = () => {
      cleanup();
      resolve(true);
    };
    const onWindowClick = (e) => {
      if (e.target === modal) {
        cleanup();
        resolve(false);
      }
    };

    // Attach Listeners
    closeBtn.addEventListener("click", onClose);
    cancelBtn.addEventListener("click", onCancel);
    actionBtn.addEventListener("click", onAction);
    window.addEventListener("click", onWindowClick);
  });
}
