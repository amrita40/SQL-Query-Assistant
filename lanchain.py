from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import requests

# ✅ Load environment variables
load_dotenv()

# ✅ Get your OpenRouter key securely
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Define the schema to convert natural language into SQL
schema = """
You are working with a SQLite database with the following table:

employees(id, name, role, salary, hire_date)

Translate the following natural language question into an SQL query that can be executed on this table.
"""

# ✅ Build prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template=schema + "\nQuestion: {question}\nSQL:"
)

# ✅ Use ChatOpenAI for OpenRouter (because OpenRouter provides Chat Models like GPT-3.5-turbo)
llm = ChatOpenAI(
    temperature=0,
    openai_api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-3.5-turbo"
)

# ✅ Chain: prompt formatting + LLM invocation
def ask_question(question):
    # First format the full prompt string manually
    formatted_prompt = prompt.format(question=question)

    # Now pass this formatted prompt to ChatOpenAI via `.invoke` using `messages`
    sql_query = llm.invoke([{"role": "user", "content": formatted_prompt}])

    print(f"\n🧠 Generated SQL:\n{sql_query.content}\n")

    # Send query to your MCP backend
    try:
        response = requests.post("http://127.0.0.1:8000/execute-sql", json={"query": sql_query.content})
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# ✅ Main execution
if __name__ == "__main__":
    user_question = input("🗨️ Ask a question: ")
    result = ask_question(user_question)

    print("\n📊 Response:")
    if "error" in result:
        print("❌ Error:", result["error"])
    else:
        print("🧾 Columns:", result["columns"])
        for row in result["rows"]:
            print("🔸 Row:", row)
