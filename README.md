```

```

# 🤖 Intelligent Multi-Database Assistant

**Version 2.0 - Deep Schema Aware**

An advanced AI-powered system designed to interact with **multiple disparate databases** (PostgreSQL) using natural language. Unlike standard Text-to-SQL bots, this system uses a **Router-Validator Architecture** to understand context, handle ambiguity across different business domains, and self-correct SQL errors.

---

## 🌟 Key Features

### 🧠 1. Intelligent "Deep Router"

* **Schema-Aware Routing**: The router analyzes the **Actual Table & Column Names** of every registered database, not just keywords.
* **Ambiguity Protocol**: If a user asks "Show me the status" and multiple databases have a "Status" column, the agent **pauses** and asks: *"Did you mean Lead Status or Machine Repair Status?"*
* **Clarification Memory**: Once you clarify (e.g., "The machine one"), it merges this with your original question to execute the correct query.

### 🛡️ 2. Self-Correcting SQL Agents

* **Generate-Validate-Regenerate Loop**:
  1. **Generator**: Writes the initial SQL query.
  2. **Validator (The Critic)**: Checks the query against business rules (e.g., "Did you use the allowed columns? Does this match the user's intent?").
  3. **Refiner**: If the Validator rejects it, the Generator automatically rewrites the query with the specific feedback.
* **Ghost Record Filtering**: Automatically ignores incomplete or "test" data (rows with NULL names/dates).

### 📊 3. Supported Integrations

The system currently integrates these distinct business domains:

| Database                | Domain                   | Key Capabilities                                                                                        |
| :---------------------- | :----------------------- | :------------------------------------------------------------------------------------------------------ |
| **Checklist DB**  | 📋 Employee Management   | Track daily checklists, delegations, and employee performance.                                          |
| **Sagar DB**      | ⚙️ Machine Maintenance | Track breakdown history, repair status (`Actual_Date` vs `Start_Date`), and technician assignments. |
| **Lead-To-Order** | 💼 Sales CRM             | Analyze leads (`fms_leads`), conversions, inquiries, and quotations (`make_quotation`).             |

---

## 🛠️ System Architecture

The following diagram illustrates how a user query travels through the system:

```mermaid
---
config:
  theme: base
  themeVariables:
    background: "#0a0c0f"
    primaryColor: "#0f1116"
    primaryTextColor: "#e2e8f0"
    primaryBorderColor: "#1e2028"
    lineColor: "#475569"
    fontFamily: "Rajdhani, sans-serif"
    fontSize: "15px"
    edgeLabelBackground: "#0f1116"
    tertiaryTextColor: "#94a3b8"
  flowchart:
    curve: basis
    rankSpacing: 58
    nodeSpacing: 40
---
flowchart TD
    classDef userNode fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#c7d2fe,border-radius:12px
    classDef gatewayNode fill:#0c1e2e,stroke:#06b6d4,stroke-width:2px,color:#a5f3fc
    classDef routerNode fill:#0c1e2e,stroke:#22d3ee,stroke-width:2.5px,color:#67e8f9
    classDef dbNode fill:#1c1410,stroke:#fb923c,stroke-width:2px,color:#fdba74
    classDef agentNode fill:#0f1f1a,stroke:#10b981,stroke-width:2px,color:#6ee7b7
    classDef errorNode fill:#1f1010,stroke:#ef4444,stroke-width:2px,color:#fca5a5
    classDef outputNode fill:#1e1b3a,stroke:#8b5cf6,stroke-width:2px,color:#c4b5fd
    classDef coreNode fill:#0d1a14,stroke:#34d399,stroke-width:2.5px,color:#a7f3d0

    U["👤  User"]:::userNode
    AG["📡  API Gateway\n───────────────\nEntry Point"]:::gatewayNode
    RT["🔀  Deep Schema Router\n───────────────\nIntent Classification"]:::routerNode
    AH["❓  Ambiguity Handler\n───────────────\nClarify & Re-route"]:::errorNode

    CE["🔄  Context Engine\n───────────────\nReformulate Query"]:::agentNode
    SG["🧠  SQL Generator\n───────────────\nBuild Query"]:::agentNode
    SV["🛡️  Safety Validator\n───────────────\nCheck & Approve"]:::coreNode
    EX["⚡  SQL Executor\n───────────────\nRun Query"]:::agentNode

    DB1["📋  Checklist DB\n───────────────\nEmployee Data"]:::dbNode
    DB2["⚙️  Sagar DB\n───────────────\nMachine Data"]:::dbNode
    DB3["💼  Sales DB\n───────────────\nSales Data"]:::dbNode

    SY["📝  Answer Synthesizer\n───────────────\nGenerate Response"]:::outputNode
    UR["👤  User\n───────────────\nReceives Result"]:::userNode

    U --> AG
    AG --> RT

    RT -. "Ambiguous Input?" .-> AH
    AH -.->|"Back to User"| U

    RT -->|"Employee Intent"| DB1
    RT -->|"Machine Intent"| DB2
    RT -->|"Sales Intent"| DB3

    subgraph CORE ["🤖  Autonomous SQL Agent Loop"]
        direction TB
        CE --> SG
        SG --> SV
        SV -->|"❌  Reject"| SG
        SV -->|"✅  Approve"| EX
    end

    style CORE fill:#0a1512,stroke:#10b981,stroke-width:2px,color:#6ee7b7,border-radius:16px

    DB1 --> CE
    DB2 --> CE
    DB3 --> CE

    EX --> SY
    SY --> UR
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

* Python 3.10+
* PostgreSQL Database
* OpenAI API Key

### Installation

1. **Clone & Setup**:

   ```bash
   git clone repo_url
   cd DB_Assistant
   ```
2. **Environment Variables**:
   Create a `.env` file in the root:

   ```properties
   OPENAI_API_KEY=sk-...
   DB_CHECKLIST_URL=postgresql://user:pass@localhost:5432/checklist
   DB_SAGAR_URL=postgresql://user:pass@localhost:5432/sagar_db
   DB_L2O_URL=postgresql://user:pass@localhost:5432/lead_to_order
   ```
3. **Run the Backend**:

   ```bash
   cd Backend_New
   uvicorn main:app --reload
   ```

   The API will start at `http://127.0.0.1:8000`.

---

## 🔧 Developer Guide

### How to Add a New Database

1. **Generate Schema**: Use `schema_generator_tool.py` to inspect your new database.
2. **Create Module**: Copy the `app/databases/template/` structure to `app/databases/your_new_db/`.
3. **Configure**:
   * **`config.py`**: Add `ROUTER_METADATA` (Description) and `DB_SCHEMA` (Columns).
   * **`prompts.py`**: Customize the system prompt with domain-specific rules.
4. **Register**: Import your metadata in `app/core/router.py`.

### Troubleshooting Common Issues

* **"Ambiguous Query" loop**: If the bot keeps asking for clarification, check if your `ROUTER_METADATA` descriptions are too similar.
* **"Column does not exist"**: If using PostgreSQL Mixed-Case columns (e.g., `TaskID`), ensure you have added quotes in `config.py` (e.g., `"- "TaskID"`).
* **"No result returned"**: The agent might be generating a query that validly returns 0 rows (e.g., searching for a name that doesn't exist). Check the debug logs.

---

### 📞 Support

For bugs or feature requests, please check the logs in `Backend_New/logs/` or contact the development team.
