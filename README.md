# 🤖 DB Assistant - Intelligent SQL Agent

> **An advanced, context-aware AI assistant that translates natural language into secure SQL queries with dual-layer validation and real-time streaming.**

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent-orange)

## 📖 Overview

**DB Assistant** is a full-stack application designed to interact with PostgreSQL databases using natural language. Unlike standard text-to-SQL tools, it employs a sophisticated **Agentic Workflow** with two distinct LLMs:
1.  **Generator Agent:** Crafts the SQL query based on schema and user intent.
2.  **Validator Agent:** Critiques the query for safety, accuracy, and intent matching before execution.

The system features real-time answer streaming, query caching (semantic search via ChromaDB), and sticky context management for follow-up questions.

---

## 🏗️ Architecture

The system follows a modular architecture separating the Frontend UI from the Agentic Backend.

```mermaid
graph TD
    User[User] -->|Natural Language| FE[Frontend (Vanilla JS)]
    FE -->|Stream Request| API[FastAPI Backend]
    
    subgraph "Backend Services"
        API -->|Check| Cache[(ChromaDB Cache)]
        Cache -- Hit --> API
        Cache -- Miss --> Agent[LangGraph Agent]
        
        subgraph "Agentic Workflow"
            Agent -->|1. List Tables| Schema[Schema Manager]
            Schema -->|2. Get Schema| GEN[Generative LLM (LLM 1)]
            GEN -->|3. Generate SQL| VAL[Validator LLM (LLM 2)]
            VAL -->|4. Critique| Decision{Approved?}
            Decision -- No --> GEN
            Decision -- Yes --> DB_Exec[DB Executor]
        end
        
        DB_Exec -->|5. Run Query| PG[(PostgreSQL DB)]
        PG -->|Results| Response[Answer Generator]
    end
    
    Response -->|Stream Chunks| FE
```

---

## ✨ Key Features

- **🧠 Dual-LLM Validation:** Ensures high accuracy by having a second "Critic" LLM review every query before execution.
- **⚡ Real-Time Streaming:** Responses are streamed token-by-token using Server-Sent Events (SSE).
- **💾 Intelligent Caching:** Validated queries are cached in a vector database (`ChromaDB`) for instant retrieval of similar questions.
- **🗣️ Context Awareness:** Remembers previous filters (e.g., "Show me Hem's tasks" -> "Now show pending") and maintains "Sticky Context".
- **🔒 Security First:** Read-only database permissions, restricted column access, and hardcoded `DELETE/UPDATE` prevention.
- **📱 Responsive UI:** Modern, clean interface with Dark/Light mode support (system default) and mobile responsiveness.

---

## 🛠️ Technology Stack

### Backend
- **Framework:** Python (FastAPI)
- **Agent Orchestration:** LangGraph (Stateful Multi-Actor Applications)
- **Database:** PostgreSQL (Core Data), ChromaDB (Vector Cache)
- **LLM:** OpenAI GPT-4o (or compatible) via LangChain
- **Server:** Uvicorn (ASGI)

### Frontend
- **Core:** HTML5, CSS3, Vanilla JavaScript (ES6+)
- **Icons:** FontAwesome
- **Formatting:** Marked.js (Markdown rendering)

---

## 🚀 Setup & Installation

Follow these steps to get the project running locally.

### Prerequisites
- Python 3.10+
- PostgreSQL Database
- OpenAI API Key

### 1. Clone the Repository
```bash
git clone https://github.com/Prabhat9801/DB_Assistant.git
cd DB_Assistant
```

### 2. Backend Setup
Navigate to the backend directory and set up the environment.

```bash
cd Backend_New

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate

# Install Dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in `Backend_New/` with your credentials:

```env
OPENAI_API_KEY=sk-your-openai-key
DB_HOST=your-db-host
DB_PORT=5432
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
```

### 4. Run the Backend
Start the FastAPI server.

```bash
# Make sure you are in Backend_New/ and .venv is active
uvicorn main:app --reload
```
*Server will start at `http://127.0.0.1:8000`*

### 5. Frontend Setup
The frontend is a static web application. You can simply open `Frontend/index.html` in your browser, or serve it using a lightweight server (recommended).

```bash
# Using Python to serve (Run in separate terminal from root)
cd Frontend
python -m http.server 5500
```
*Access the app at `http://127.0.0.1:5500`*

---

## 🔄 Workflow Details

The **Agentic Workflow** is defined in `app/services/agent_nodes.py`. Here is the detailed lifecycle of a user request:

### 1. Schema Loading
The agent connects to the database to fetch the list of tables (`checklist`, `delegation`) and their schemas.

### 2. Context Injection
If the user asks a follow-up question (e.g., "pending ones?"), the `ContextManager` injects details from the previous query (User Filters, Date Ranges) into the prompt.

### 3. Query Generation (Loop)
- **Generator (LLM 1):** Proposes a SQL query.
- **Validator (LLM 2):** Reviews the query against a strict checklist:
  - Is it read-only?
  - Does it match User Intent?
  - Are columns valid?
- **Feedback:** If rejected, the Validator provides specific feedback, and the Generator retries (up to 3 times).

### 4. Execution & Response
- Once approved, the query is executed securely.
- Results are passed to the **Answer Generator**, which crafts a natural language summary.
- The summary is **Streamed** to the frontend efficiently.

---

## 📁 Project Structure

```
DB_Assistant/
├── Backend_New/             # Python FastAPI Backend
│   ├── app/
│   │   ├── api/routes/      # API Endpoints (Chat, Sessions)
│   │   ├── core/            # Config & Security
│   │   ├── services/        # Business Logic
│   │   │   ├── agent_nodes.py   # LangGraph Nodes
│   │   │   ├── sql_agent.py     # Graph Definition
│   │   │   └── validator.py     # Validator Logic
│   │   └── main.py          # App Entrypoint
│   └── requirements.txt     # Python Dependencies
│
├── Frontend/                # UI Code
│   ├── index.html           # Main Interface
│   ├── app.js               # Frontend Logic & State
│   └── styles.css           # (Embedded in HTML/JS)
│
└── README.md                # Project Documentation
```

## 🤝 Contribution

Contributions are welcome! Please fork the repository and submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
