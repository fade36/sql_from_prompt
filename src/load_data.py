import pandas as pd
import sqlite3
from pathlib import Path
import glob
import os

def change_name(csv):
    return csv.stem.lower().strip().replace(" ", "_").replace("-","_")

def load_data():
    project_root = Path(__file__).resolve().parents[1]
    data_dir = project_root / "data"
    db_path = project_root / "database" / "datawarehouse.db"

    db_path.parent.mkdir(parents=True, exist_ok=True)
    connect = sqlite3.connect(db_path)
    loaded = 0

    for csv_path in sorted(data_dir.glob("*.csv")):
        table_name = change_name(csv_path)
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, connect, if_exists="replace", index=False)
        print(f"{table_name}: {len(df)} rows")
        loaded+=1

    connect.close()

    if loaded == 0:
        print("There are no CSV files in directory 'data'")

if __name__ == "__main__":
    load_data()

    

