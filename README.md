# 🤖 Intelligent Multi-Database Assistant

**Version 2.0 - Deep Schema Aware**

An advanced AI-powered system designed to interact with **multiple disparate databases** (PostgreSQL) using natural language. Unlike standard Text-to-SQL bots, this system uses a **Router-Validator Architecture** to understand context, handle ambiguity across different business domains, and self-correct SQL errors.

---

## 🌟 Key Features

### 🧠 1. Intelligent "Deep Router"
*   **Schema-Aware Routing**: The router analyzes the **Actual Table & Column Names** of every registered database, not just keywords.
*   **Ambiguity Protocol**: If a user asks "Show me the status" and multiple databases have a "Status" column, the agent **pauses** and asks: *"Did you mean Lead Status or Machine Repair Status?"*
*   **Clarification Memory**: Once you clarify (e.g., "The machine one"), it merges this with your original question to execute the correct query.

### 🛡️ 2. Self-Correcting SQL Agents
*   **Generate-Validate-Regenerate Loop**:
    1.  **Generator**: Writes the initial SQL query.
    2.  **Validator (The Critic)**: Checks the query against business rules (e.g., "Did you use the allowed columns? Does this match the user's intent?").
    3.  **Refiner**: If the Validator rejects it, the Generator automatically rewrites the query with the specific feedback.
*   **Ghost Record Filtering**: Automatically ignores incomplete or "test" data (rows with NULL names/dates).

### 📊 3. Supported Integrations
The system currently integrates these distinct business domains:

| Database | Domain | Key Capabilities |
| :--- | :--- | :--- |
| **Checklist DB** | 📋 Employee Management | Track daily checklists, delegations, and employee performance. |
| **Sagar DB** | ⚙️ Machine Maintenance | Track breakdown history, repair status (`Actual_Date` vs `Start_Date`), and technician assignments. |
| **Lead-To-Order** | 💼 Sales CRM | Analyze leads (`fms_leads`), conversions, inquiries, and quotations (`make_quotation`). |

---

## 🛠️ System Architecture

The following diagram illustrates how a user query travels through the system:

```mermaid
graph LR
    %% -- Modern Color Palette --
    classDef userNode fill:#2d3436,stroke:#636e72,stroke-width:2px,color:#fff;
    classDef routerNode fill:#0984e3,stroke:#74b9ff,stroke-width:2px,color:#fff;
    classDef dbNode fill:#e17055,stroke:#fab1a0,stroke-width:2px,color:#fff;
    classDef agentNode fill:#00b894,stroke:#55efc4,stroke-width:2px,color:#fff;
    classDef errorNode fill:#d63031,stroke:#ff7675,stroke-width:2px,color:#fff;
    classDef outputNode fill:#6c5ce7,stroke:#a29bfe,stroke-width:2px,color:#fff;

    %% -- User Entry --
    User([👤 User]):::userNode --> API[📡 API Gateway]
    API --> Router{{🔀 Deep Schema Router}}:::routerNode

    %% -- Logic Fork --
    Router -- "Ambiguous?" --> Clarify[❓ Ambiguity Handler]:::errorNode
    Clarify -.-> User
    
    %% -- Routing --
    Router -- "Employee Intent" --> Check[(📋 Checklist DB)]:::dbNode
    Router -- "Machine Intent" --> Sagar[(⚙️ Sagar DB)]:::dbNode
    Router -- "Sales Intent" --> L2O[(💼 Sales DB)]:::dbNode
    
    %% -- The Autonomous Agent Core --
    subgraph Core_Agent_Logic [🤖 Autonomous SQL Agent Loop]
        direction TB
        Reformulate[🔄 Context Engine]:::agentNode
        Generator[[🧠 SQL Generator]]:::agentNode
        Validator{🛡️ Safety Validator}:::agentNode
        Executor[⚡ SQL Executor]:::agentNode
        
        Reformulate --> Generator
        Generator --> Validator
        Validator -- "❌ Reject" --> Generator
        Validator -- "✅ Approve" --> Executor
    end

    %% -- Connections to Core --
    Check & Sagar & L2O --> Reformulate

    %% -- Final Output --
    Executor --> Synthesizer([📝 Answer Synthesizer]):::outputNode
    Synthesizer --> User
```

---

## 📂 Project Structure

```text
DB_Assistant/
├── Backend_New/              # FastAPI Python Backend
│   ├── app/
│   │   ├── core/
│   │   │   ├── router.py     # Main Router Logic (The Brain)
│   │   │   ├── config.py     # Global Settings
│   │   ├── databases/        # 🔌 Modular Database Agents
│   │   │   ├── checklist/    # Employee DB Module
│   │   │   ├── sagar_db/     # Maintenance DB Module
│   │   │   └── lead_to_order/# Sales DB Module
│   │   └── services/         # Shared Utilities (Session, Graph)
├── Database_Schemas/         # 📊 Auto-Generated Schema Reports
│   ├── checklist/
│   ├── sagar_db/
│   └── ...
└── DATABASE_INTEGRATION_GUIDE.md  # 📘 How to add new DBs
```

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   PostgreSQL Database
*   OpenAI API Key

### Installation

1.  **Clone & Setup**:
    ```bash
    git clone repo_url
    cd DB_Assistant
    ```

2.  **Environment Variables**:
    Create a `.env` file in the root:
    ```properties
    OPENAI_API_KEY=sk-...
    DB_CHECKLIST_URL=postgresql://user:pass@localhost:5432/checklist
    DB_SAGAR_URL=postgresql://user:pass@localhost:5432/sagar_db
    DB_L2O_URL=postgresql://user:pass@localhost:5432/lead_to_order
    ```

3.  **Run the Backend**:
    ```bash
    cd Backend_New
    uvicorn main:app --reload
    ```
    The API will start at `http://127.0.0.1:8000`.

---

## 🔧 Developer Guide

### How to Add a New Database
1.  **Generate Schema**: Use `schema_generator_tool.py` to inspect your new database.
2.  **Create Module**: Copy the `app/databases/template/` structure to `app/databases/your_new_db/`.
3.  **Configure**:
    *   **`config.py`**: Add `ROUTER_METADATA` (Description) and `DB_SCHEMA` (Columns).
    *   **`prompts.py`**: Customize the system prompt with domain-specific rules.
4.  **Register**: Import your metadata in `app/core/router.py`.

### Troubleshooting Common Issues
*   **"Ambiguous Query" loop**: If the bot keeps asking for clarification, check if your `ROUTER_METADATA` descriptions are too similar.
*   **"Column does not exist"**: If using PostgreSQL Mixed-Case columns (e.g., `TaskID`), ensure you have added quotes in `config.py` (e.g., `"- "TaskID"`).
*   **"No result returned"**: The agent might be generating a query that validly returns 0 rows (e.g., searching for a name that doesn't exist). Check the debug logs.

---

### 📞 Support
For bugs or feature requests, please check the logs in `Backend_New/logs/` or contact the development team.
