# 🐬 MySQL MCP Server (FastMCP-Powered)

Leverage the power of AI to automate your MySQL workflows with **FastMCP**.  
This tool enables AI agents like Claude, OpenAI, or DeepSeek to interact with your MySQL database using natural language, making database management seamless and intelligent.

Whether you're generating synthetic data, querying your tables, or performing updates, this MCP server allows AI to operate on your database through standardized interfaces — all from your local machine.

🔎 Best use for generating synthetic data for testing your apis.
---

## 💡 Key Features

- Automates SQL tasks via AI (Claude, OpenAI, DeepSeek, etc.)
- Works over **Stdio**, ideal for local desktop integration
- Generates **synthetic data** based on your schema and recent values
- No manual SQL knowledge required
- Highly useful for **test environments** and **data prototyping**

---

## 🛠️ Supported Tools

| Tool | Description |
|------|-------------|
| `get_column_names(table_name)` | Retrieve all column names of a table |
| `get_all_table_names()` | List all table names in the database |
| `select(...)` | Fetch records from any table |
| `insert(...)` | Insert data into a table |
| `update(...)` | Update records with conditions |
| `delete(...)` | Delete records based on criteria |

These are internally used by the AI to understand and manipulate your database efficiently.

---

## ⚙️ Configuration & Setup


### 📋 Prerequisites

- Python 3.10+
- MySQL (running locally or remotely)
- Anthropic Claude Desktop app (or Cursor)
- UV (Python package manager), install with `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Steps

1. **Clone this repository**

   ```bash
   git clone https://github.com/Ashutosh-rajput/mysql-mcp.git
   cd mysql-mcp
   uv pip install -r requirements.txt
   ```

2. **Fill the .env**
    ```
    MYSQL_HOST=localhost
    MYSQL_PORT=3306
    MYSQL_USER=root
    MYSQL_PASSWORD=yourpassword
    MYSQL_DATABASE=yourdatabase
   ```


3. **Connect to the MCP server**

   Copy the below json with the appropriate {{PATH}} values:

   ```json
       {
      "mcpServers": {
        "Mysql": {
          "command": "[path to uv]/uv",
          "args": [
            "run",
            "--with", "fastmcp",
            "--with", "mysql-connector-python",
            "--with", "python-dotenv",
            "fastmcp",
            "run",
            "[path to your main.py]/main.py"
          ]
        }
      }
    }
   ```

   For **Claude**, save this as `claude_desktop_config.json` in your Claude Desktop configuration directory at:

   ```
   ~/Library/Application Support/Claude/claude_desktop_config.json
   ```

   For **Cursor**, save this as `mcp.json` in your Cursor configuration directory at:

   ```
   ~/.cursor/mcp.json
   ```

4. **Restart Claude Desktop / Cursor**

   Open Claude Desktop and you should now see WhatsApp as an available integration.

   Or restart Cursor.


## 🧠 Tip

Use this project as a backbone to build intelligent, event-driven Mysql bots, agents.

---

## 📜 License

MIT License. Feel free to use and modify as per your needs.

---

> 👤 Author: Ashutosh Rajput  
> 🌐 Project: [MySql-MCP](#)