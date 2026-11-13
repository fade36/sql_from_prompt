# SQL from Prompt

Ask questions about your data in plain English and get the answer as a table.
An LLM translates the question into SQL; the app validates it and runs it
on a read-only database connection.

> Status: work in progress.

## How it works

question → schema + prompt → LLM → SQL → safety check → read-only execution → table

## Project structure

- `data/` – source CSV files (demo dataset included)
- `database/` – generated database file (not committed)
- `src/load_data.py` – loads every CSV from `data/` into the database
- `src/db.py` – reads the schema, runs queries
- `src/llm.py` – builds the prompt, calls the LLM API
- `src/safety.py` – checks that the SQL is a single SELECT
- `src/app.py` – Streamlit interface
- `tests/` – unit tests for the safety checks
- `eval/` – test questions with reference SQL and the evaluation script

## Setup

1. Clone the repo and install dependencies: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and put your API key in it
3. Load the demo data: `python src/load_data.py`
4. Run the app: `streamlit run src/app.py`

## Safety

Model output is never trusted. Layers: read-only connection, single-SELECT
validation, row limit, SQL shown to the user.

## Evaluation

_To be added._

## Limitations

_To be added._