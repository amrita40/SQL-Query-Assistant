from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Model to accept SQL query
class SQLRequest(BaseModel):
    query: str

@app.post("/execute-sql")
async def execute_sql(request: SQLRequest):
    conn = sqlite3.connect("sql.db")  # ✅ Use your actual database name
    cursor = conn.cursor()
    try:
        cursor.execute(request.query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        return {"columns": columns, "rows": rows}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()
