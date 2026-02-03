# 🗄️ Database Integration Guide (DB Assistant)

This guide details exactly how to **Add (Integrate)**, **Update**, or **Remove** a database from the generic DB Assistant chatbot system.

---

## 🏗️ Part 1: How to Integrate a NEW Database

### 0. Analyze the Database (Schema Generation)
Before writing any code, you need to know what is inside the database (tables, columns, types).

1.  **Create a Schema Folder:**
    Create a folder for your report: `Database_Schemas/inventory_db/`

2.  **Create the Generator Script:**
    Copy an existing script (e.g., from `Database_Schemas/checklist/generate_schema.py`) into your new folder.
    *   **Edit the `DB_URL`**: Update it to your new database connection string.
    *   **Edit the `DB_NAME`**: Give it a friendly name.

3.  **Run the Script:**
    ```powershell
    python Database_Schemas/inventory_db/generate_schema.py
    ```
    
4.  **Use the Output:**
    *   `schema_report.md`: Read this to pick which tables you want.
    *   `metadata_analysis.json`: Use the AI-suggested descriptions for your `config.py`.

### 1. Configuration (`.env`)
Add the connection string to your `.env` file (both in Root and `Backend_New/`).
```properties
# Example: Inventory DB
DB_INVENTORY_URL=postgresql://user:pass@host:5432/inventory_db
```
> **Tip:** If the database usage Mixed-Case columns (e.g., `ProductID`), remember that you will need to interpret them carefully later.

### 2. Update Core Config (`app/core/config.py`)
Add the new variable to the `Settings` class so the app can read it.
```python
class Settings(BaseSettings):
    # ... existing ...
    DB_INVENTORY_URL: str = os.getenv("DB_INVENTORY_URL", "")
```

### 3. Create the Database Module
Create a new folder: `Backend_New/app/databases/inventory_db/`.
Inside, create these 4 required files:

#### A. `config.py` (The Rules)
Define **Metadata** (for the Router), **Allowed Tables**, and **Strict Schema**.
```python
ROUTER_METADATA = {
    "name": "inventory_db",
    "description": "Tracks stock levels, warehouses, and product locations.",
    "keywords": ["stock", "inventory", "warehouse", "sku", "product count"]
}

ALLOWED_TABLES = ["products", "stock_ledger"]

# CRITICAL: If columns are Mixed-Case (e.g. 'StockLevel'), use double quotes here!
DB_SCHEMA = """
Table: products
Columns:
- "ProductID" (INT)
- "StockLevel" (INT)
"""
```

#### B. `prompts.py` (The Brain)
Define the System Prompts.
```python
from .config import DB_SCHEMA

GENERATE_QUERY_SYSTEM_PROMPT = f"""
You are an Inventory Analyst.
### SCHEMA
{DB_SCHEMA}
### RULES
- Use ONLY allowed columns.
- CRITICAL: Use double quotes for column names (e.g. "StockLevel").
"""
# Import standard reformulation prompt
from app.databases.lead_to_order.prompts import REFORMULATE_QUESTION_PROMPT 
```

#### C. `connection.py` (The Connection)
Handle the connection using the URL from Step 2.
```python
from langchain_community.utilities import SQLDatabase
from app.core.config import settings
from .config import ALLOWED_TABLES

def get_db_instance():
    return SQLDatabase.from_uri(
        settings.DB_INVENTORY_URL,
        include_tables=ALLOWED_TABLES
    )
```

#### D. `workflow.py` (The Agent)
Copy the standard file from an existing DB (e.g., `sagar_db`) and update imports.
```python
from .connection import get_db_instance
from .prompts import GENERATE_QUERY_SYSTEM_PROMPT
# ... Update the compile name ...
inventory_app = workflow.compile()
```

### 4. Register the Database (`app/core/router.py`)
Tell the central router about the new module.

1.  **Import Metadata AND Schema:**
    ```python
    from app.databases.inventory_db.config import ROUTER_METADATA as INVENTORY_META, DB_SCHEMA as INVENTORY_SCHEMA
    
    # Add to the Registry as a Tuple: (Metadata, Schema)
    REGISTERED_DATABASES = [
        (CHECKLIST_META, CHECKLIST_SCHEMA),
        (SAGAR_META, SAGAR_SCHEMA),
        (INVENTORY_META, INVENTORY_SCHEMA) # <--- Add your new tuple here
    ]
    ```

2.  **Update Agent Factory (`get_agent_for_database`):**
    ```python
    if db_name == "inventory_db":
        from app.databases.inventory_db.workflow import inventory_app
        return inventory_app
    ```
3.  **Update Answer Factory (`get_answer_generator`):**
    ```python
    if db_name == "inventory_db":
        from app.databases.inventory_db.prompts import ANSWER_SYNTHESIS_SYSTEM_PROMPT
        return create_answer_generator(ANSWER_SYNTHESIS_SYSTEM_PROMPT)
    ```

---

## 🔄 Part 2: How to UPDATE an Existing Database

### To Add New Tables/Columns
1.  **Edit `config.py`**:
    *   Add the new table to `ALLOWED_TABLES`.
    *   Add the new columns to `DB_SCHEMA` (Remember: Double quote valid mixed-case names!).
    *   Add columns to `COLUMNS_RESTRICTION` (if using strict mode).
2.  **Restart Server**: Changes to `config.py` usually require a restart.

### To Update Descriptions/Keywords (Router Logic)
1.  **Edit `config.py`**:
    *   Modify `ROUTER_METADATA["description"]` or `["keywords"]`.
    *   Making descriptions distinct prevents the Router from getting confused.

---

## 🗑️ Part 3: How to REMOVE (Delete) a Database

### 1. Deregister from Router (`app/core/router.py`)
*   Remove the import line: `from ... import ROUTER_METADATA as INVENTORY_META`
*   Remove it from `REGISTERED_DATABASES`.
*   Remove the `if db_name == "inventory_db":` blocks from both factory functions.

### 2. Remove Config (`app/core/config.py`)
*   Remove the `DB_INVENTORY_URL` field from the `Settings` class.

### 3. Delete Files
*   Delete the folder `Backend_New/app/databases/inventory_db/`.
*   Remove the URL from `.env`.

---

## 🛡️ CRITICAL NOTES regarding PostgreSQL Case Sensitivity
If your database has Mixed-Case column names (e.g., `Task_Start_Date` vs `task_start_date`):

1.  **Always Quote in Schema**: Define it as `"- "Task_Start_Date"` in `config.py`.
2.  **Explicit Instruction**: In `prompts.py`, explicitly tell the AI: *"You MUST use double quotes around all column names."*
3.  **Correction**: If the AI fails, double-check your `DB_SCHEMA` definition.
