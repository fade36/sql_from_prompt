import sqlite3
from pathlib import Path
import pandas as pd

path = Path(__file__).resolve().parents[1] / "database" / "datawarehouse.db"

def get_schema():
    connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:

        tables = connection.execute(
        "Select name from sqlite_master where type = 'table' "
        "and name not like 'sqlite_%'"
        ).fetchall()

        lines = []

        for (table_name,) in tables:
            cols = connection.execute(f'PRAGMA table_info("{table_name}")').fetchall()
            cols_desrciption = ", ".join(f"{col[1]} {col[2]}" for col in cols)
            lines.append(f"{table_name} ({cols_desrciption})")
    finally:
        connection.close()
        
    return "\n".join(lines)  #to get text, not list

def run_query(sql_request):
    
    connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:
        res = pd.read_sql_query(sql_request, connection)

    finally: connection.close()

    return res
    

if __name__ == "__main__":
    print(get_schema())
    print(run_query("Select count(*) from olist_order_items_dataset"))





