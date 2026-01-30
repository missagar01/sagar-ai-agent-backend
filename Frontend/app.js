/**
 * Botivate v1.0 - Frontend Application with STREAMING
 * Features:
 * - Real-time streaming responses (word-by-word)
 * - Status updates during processing
 * - Session management (create, list, switch, delete)
 * - Chat history per session
 * - Query caching visualization
 * - Request cancellation
 */

const API_BASE_URL = 'http://localhost:8000';

// DOM Elements
const chatDisplay = document.getElementById('chatDisplay');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const sendIcon = document.getElementById('sendIcon');
const welcomeScreen = document.getElementById('welcomeScreen');
const typingText = document.getElementById('typingText');
const sidebar = document.getElementById('sidebar');
const sessionList = document.getElementById('sessionList');
const newChatBtn = document.getElementById('newChatBtn');
const toggleSidebarBtn = document.getElementById('toggleSidebarBtn');
const clearChatBtn = document.getElementById('clearChatBtn');
const deleteChatBtn = document.getElementById('deleteChatBtn');
const cacheInfoBtn = document.getElementById('cacheInfoBtn');
const cacheModal = document.getElementById('cacheModal');
const closeCacheModal = document.getElementById('closeCacheModal');
const cacheModalBody = document.getElementById('cacheModalBody');
const clearCacheBtn = document.getElementById('clearCacheBtn');
const cacheIndicator = document.getElementById('cacheIndicator');
const clearOptionsModal = document.getElementById('clearOptionsModal');
const closeClearModal = document.getElementById('closeClearModal');
const confirmClearChatBtn = document.getElementById('confirmClearChat');
const confirmDeleteSessionBtn = document.getElementById('confirmDeleteSession');
const confirmClearCacheModalBtn = document.getElementById('confirmClearCacheFromModal');

// State
let currentSessionId = null;
let isGenerating = false;
let currentRequestId = null;
let abortController = null;

// ============================================================================
// INITIALIZATION
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
    startTypingAnimation();
    loadSessions();
    setupEventListeners();
});

function setupEventListeners() {
    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !isGenerating) {
            e.preventDefault();
            sendMessage();
        }
    });

    newChatBtn.addEventListener('click', createNewSession);
    toggleSidebarBtn.addEventListener('click', toggleSidebar);

    // Clear Button opens Modal now
    clearChatBtn.addEventListener('click', openClearModal);

    // Legacy delete button still works directly
    deleteChatBtn.addEventListener('click', deleteCurrentSession);

    cacheInfoBtn.addEventListener('click', showCacheStats);
    closeCacheModal.addEventListener('click', () => cacheModal.style.display = 'none');
    clearCacheBtn.addEventListener('click', clearCache);

    // Clear Modal Listeners
    closeClearModal.addEventListener('click', () => clearOptionsModal.style.display = 'none');
    confirmClearChatBtn.addEventListener('click', () => {
        clearCurrentChat(true);
        clearOptionsModal.style.display = 'none';
    });
    confirmDeleteSessionBtn.addEventListener('click', () => {
        deleteCurrentSession(true);
        clearOptionsModal.style.display = 'none';
    });
    confirmClearCacheModalBtn.addEventListener('click', () => {
        clearCache();
        clearOptionsModal.style.display = 'none';
    });

    // Close modals on outside click
    window.addEventListener('click', (e) => {
        if (e.target === cacheModal) cacheModal.style.display = 'none';
        if (e.target === clearOptionsModal) clearOptionsModal.style.display = 'none';
    });
}

function openClearModal() {
    clearOptionsModal.style.display = 'flex';
}

// ============================================================================
// TYPING ANIMATION
// ============================================================================

function startTypingAnimation() {
    if (!typingText) return;
    const text = "Ask Anything....";
    let i = 0;
    typingText.textContent = "";

    function type() {
        if (i < text.length && typingText) {
            typingText.textContent += text.charAt(i);
            i++;
            setTimeout(type, 100);
        } else if (typingText) {
            setTimeout(() => {
                i = 0;
                if (typingText) typingText.textContent = "";
                type();
            }, 2000);
        }
    }
    type();
}

// ============================================================================
// SESSION MANAGEMENT
// ============================================================================

async function loadSessions() {
    try {
        const response = await fetch(`${API_BASE_URL}/chat/sessions`);
        const sessions = await response.json();

        renderSessionList(sessions);

        if (sessions.length > 0 && !currentSessionId) {
            selectSession(sessions[0].session_id);
        }
    } catch (error) {
        console.error('Failed to load sessions:', error);
    }
}

function renderSessionList(sessions) {
    sessionList.innerHTML = '';

    sessions.forEach(session => {
        const item = document.createElement('div');
        item.className = `session-item ${session.session_id === currentSessionId ? 'active' : ''}`;
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

        item.querySelector('.session-info').addEventListener('click', () => {
            selectSession(session.session_id);
        });

        item.querySelector('.session-delete').addEventListener('click', (e) => {
            e.stopPropagation();
            deleteSession(session.session_id);
        });

        sessionList.appendChild(item);
    });
}

async function selectSession(sessionId) {
    currentSessionId = sessionId;

    document.querySelectorAll('.session-item').forEach(item => {
        item.classList.toggle('active', item.dataset.sessionId === sessionId);
    });

    updateSessionIndicator();
    await loadSessionMessages(sessionId);
}

async function loadSessionMessages(sessionId) {
    try {
        const response = await fetch(`${API_BASE_URL}/chat/sessions/${sessionId}/messages`);
        const data = await response.json();

        chatDisplay.innerHTML = '';

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
            data.messages.forEach(msg => {
                addMessage(msg.content, msg.role === 'user' ? 'user' : 'bot', false);
            });
        }

        chatDisplay.scrollTop = chatDisplay.scrollHeight;

    } catch (error) {
        console.error('Failed to load messages:', error);
    }
}

async function createNewSession() {
    try {
        const response = await fetch(`${API_BASE_URL}/chat/sessions`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({})
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
        console.error('Failed to create session:', error);
    }
}

async function deleteSession(sessionId, skipConfirm = false) {
    console.log(`Attempting to delete session: ${sessionId}, skipConfirm: ${skipConfirm}`);

    if (!skipConfirm && !confirm('Are you sure you want to delete this conversation?')) {
        console.log('Delete cancelled by user');
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/chat/sessions/${sessionId}`, {
            method: 'DELETE'
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

        console.log('Session deleted successfully');

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
        console.error('Failed to delete session:', error);
        alert(`Failed to delete session: ${error.message}`);
    }
}

async function deleteCurrentSession(skipConfirm = false) {
    if (!currentSessionId) {
        console.error('No active session to delete');
        alert('No active session selected');
        return;
    }
    await deleteSession(currentSessionId, skipConfirm);
}

async function clearCurrentChat(skipConfirm = false) {
    if (!currentSessionId) return;

    if (!skipConfirm && !confirm('Clear all messages in this conversation?')) return;

    try {
        const response = await fetch(`${API_BASE_URL}/chat/sessions/${currentSessionId}/clear`, {
            method: 'POST'
        });
        const result = await response.json();

        await loadSessionMessages(currentSessionId);
        await loadSessions();

        alert(`✅ ${result.message}`);

    } catch (error) {
        console.error('Failed to clear chat:', error);
        alert('Failed to clear chat');
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
        stopGeneration();
        return;
    }

    const question = userInput.value.trim();
    if (!question) return;

    // Create session if none exists
    if (!currentSessionId) {
        try {
            const response = await fetch(`${API_BASE_URL}/chat/sessions`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({})
            });
            const session = await response.json();
            currentSessionId = session.session_id;
            await loadSessions();
        } catch (error) {
            console.error('Failed to create session:', error);
            return;
        }
    }

    // Set generating state
    isGenerating = true;
    abortController = new AbortController();
    sendIcon.className = 'fas fa-stop';
    userInput.disabled = true;

    // Hide welcome screen
    const welcomeEl = document.getElementById('welcomeScreen');
    if (welcomeEl) {
        welcomeEl.remove();
    }

    // Add user message
    addMessage(question, 'user');
    userInput.value = '';

    // Add bot message container with status
    const botMsgId = addMessage('', 'bot');
    const botMsgDiv = document.getElementById(botMsgId);

    // Create status and content containers
    botMsgDiv.innerHTML = `
        <div class="stream-status" id="streamStatus-${botMsgId}">
            <div class="status-dot"></div>
            <span>Connecting...</span>
        </div>
        <div class="stream-content" id="streamContent-${botMsgId}"></div>
    `;

    const statusDiv = document.getElementById(`streamStatus-${botMsgId}`);
    const contentDiv = document.getElementById(`streamContent-${botMsgId}`);

    // Hide cache indicator
    cacheIndicator.style.display = 'none';

    let fullText = '';
    let isCacheHit = false;

    try {
        // Use streaming endpoint
        const response = await fetch(`${API_BASE_URL}/chat/stream`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                question,
                session_id: currentSessionId
            }),
            signal: abortController.signal
        });

        if (!response.ok) throw new Error('Network response was not ok');

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value, { stream: true });
            const lines = chunk.split('\n');

            for (const line of lines) {
                if (!line.trim() || !line.startsWith('data: ')) continue;

                try {
                    const jsonStr = line.replace('data: ', '').trim();
                    if (!jsonStr) continue;

                    const data = JSON.parse(jsonStr);

                    switch (data.type) {
                        case 'status':
                            // Update status message with animation
                            statusDiv.innerHTML = `
                                <div class="status-dot active"></div>
                                <span>${data.message}</span>
                            `;
                            break;

                        case 'cache_hit':
                            isCacheHit = data.value;
                            if (isCacheHit) {
                                statusDiv.innerHTML = `
                                    <div class="status-dot cached"></div>
                                    <span>⚡ Using cached query</span>
                                `;
                            }
                            break;

                        case 'sql':
                            // Show SQL was generated
                            statusDiv.innerHTML = `
                                <div class="status-dot active"></div>
                                <span>Query ready, generating response...</span>
                            `;
                            break;

                        case 'chunk':
                            // Stream text chunk - INSTANT feel
                            if (statusDiv.style.display !== 'none') {
                                statusDiv.style.display = 'none';
                            }
                            fullText += data.content;
                            // Render markdown incrementally
                            let rendered = marked.parse(fullText);
                            rendered = rendered.replace(/<table>/g, '<div class="table-wrapper"><table>');
                            rendered = rendered.replace(/<\/table>/g, '</table></div>');
                            contentDiv.innerHTML = rendered;
                            chatDisplay.scrollTop = chatDisplay.scrollHeight;
                            break;

                        case 'done':
                            // Streaming complete
                            if (isCacheHit) {
                                botMsgDiv.classList.add('cached');
                                cacheIndicator.style.display = 'flex';
                            }
                            await loadSessions(); // Refresh counts
                            break;

                        case 'error':
                            statusDiv.style.display = 'none';
                            contentDiv.innerHTML = `<div class="error" style="color: #ff4d4d;">${data.message}</div>`;
                            break;
                    }
                } catch (parseError) {
                    console.log('Parse error for line:', line);
                }
            }
        }

    } catch (error) {
        if (error.name === 'AbortError') {
            statusDiv.style.display = 'none';
            if (fullText) {
                contentDiv.innerHTML += '<p class="stopped-indicator">(Stopped by user)</p>';
            } else {
                contentDiv.innerHTML = '<p class="stopped-indicator">(Stopped by user)</p>';
            }
        } else {
            statusDiv.style.display = 'none';
            contentDiv.innerHTML = `<div class="error" style="color: #ff4d4d;">Connection error: ${error.message}</div>`;
        }
    } finally {
        isGenerating = false;
        currentRequestId = null;
        abortController = null;
        sendIcon.className = 'fas fa-arrow-up';
        userInput.disabled = false;
        userInput.focus();
        chatDisplay.scrollTop = chatDisplay.scrollHeight;
    }
}

function stopGeneration() {
    if (abortController) {
        abortController.abort();
    }

    isGenerating = false;
    sendIcon.className = 'fas fa-arrow-up';
    userInput.disabled = false;
    userInput.focus();
}

function addMessage(text, type, animate = true) {
    const messageDiv = document.createElement('div');
    const id = 'msg-' + Math.random().toString(36).substr(2, 9);
    messageDiv.id = id;
    messageDiv.className = `message ${type}`;

    if (!animate) {
        messageDiv.style.animation = 'none';
    }

    if (type.includes('bot') && text) {
        let renderedHtml = marked.parse(text);
        renderedHtml = renderedHtml.replace(/<table>/g, '<div class="table-wrapper"><table>');
        renderedHtml = renderedHtml.replace(/<\/table>/g, '</table></div>');
        messageDiv.innerHTML = renderedHtml;
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

function toggleSidebar() {
    sidebar.classList.toggle('collapsed');
}

// ============================================================================
// CACHE MANAGEMENT
// ============================================================================

async function showCacheStats() {
    cacheModal.style.display = 'flex';
    cacheModalBody.innerHTML = 'Loading...';

    try {
        const response = await fetch(`${API_BASE_URL}/chat/cache/stats`);
        const stats = await response.json();

        cacheModalBody.innerHTML = `
            <div class="stat-item">
                <span class="stat-label">Status</span>
                <span class="stat-value">${stats.enabled ? '✅ Enabled' : '❌ Disabled'}</span>
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
    if (!confirm('Are you sure you want to clear the System Cache?')) return;
    try {
        const response = await fetch(`${API_BASE_URL}/chat/cache/clear`, {
            method: 'POST'
        });
        const result = await response.json();

        // Refresh cache stats if modal is open
        if (cacheModal.style.display !== 'none') {
            await showCacheStats();
        }

        alert(`✅ ${result.message}`);
    } catch (error) {
        console.error('Failed to clear cache:', error);
        alert('Failed to clear cache');
    }
}

// ============================================================================
// UTILITIES
// ============================================================================

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
