# 🧠 SQL Query Assistant

A Natural Language to SQL translator powered by LangChain and OpenRouter. Ask your database questions in plain English and get real-time answers from your SQLite database.

---

## 🚀 Features

- Translate English to SQL queries using LLMs
- Execute queries on live SQLite database
- Modular FastAPI server for SQL execution
- Uses LangChain and OpenRouter API for flexibility

---
## 🖼️ Demo Screenshot

> ✨ Here's what it looks like in action:

![Demo Screenshot](assets/demo.png)

## 🛠️ Tech Stack

| Layer         | Tech                                |
| ------------- | ----------------------------------- |
| Backend       | `FastAPI`, `SQLite`                 |
| LLM Pipeline  | `LangChain`, `OpenRouter`           |
| Language      | `Python 3.10+`                      |

---

## 📁 Structure
SQL-Query-Assistant/
│
├── init_db.py # Creates sample employees database
├── mcp_server.py # FastAPI server to run SQL
├── lanchain.py # Chat-based SQL query assistant
├── sql.db # SQLite database
├── .env # API key for OpenRouter
├── .gitignore
└── README.md
## Create and seed the database
python init_db.py

## Run the FastAPI backend
uvicorn mcp_server:app --reload

## Run the Assistant

python lanchain.py

## Example input:
🗨️ Ask a question: Show all employees hired after 2022
## Sample Output
🧠 Generated SQL:
SELECT * FROM employees WHERE hire_date > '2022-01-01';

📊 Response:
🧾 Columns: ['id', 'name', 'role', 'salary', 'hire_date']
🔸 Row: (3, 'Charlie', 'Manager', 90000, '2023-05-01')

## 🙌 Acknowledgements
LangChain

FastAPI

OpenRouter



