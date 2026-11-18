from dotenv import load_dotenv
from openai import OpenAI
from db import get_schema
from db import run_query

load_dotenv()

def get_sql(question, schema):

    client = OpenAI()
    response = client.responses.create(
    model="gpt-5.4-mini",
    input=f"Description of all tables: {schema}, question: {question}. " 
    "Write only the sql request which answers the question. Return only one SELECT, SQLite dialect, "
    "without Markdown and formatting. Return only the SQL text, nothing else. "
    "Get the example (pattern) of names, variables and columns from tables description, in occasion that question is wrong"
)
    return response.output_text


if __name__ == "__main__":
    schema = get_schema()
    question = "How many orders are there in total?"
    sql = get_sql(question, schema)
    print(run_query(sql))