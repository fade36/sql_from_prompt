# SQL from Prompt

Ask questions about your data in plain English and get the answer as a table.
An LLM translates the question into SQL; the app validates it and runs it
on a read-only database connection.

> Status: work in progress.

## How it works

question → schema + prompt → LLM → SQL → safety check → read-only execution → table

## Project structure

- `data/` – source CSV files (not commited, see Data)
- `database/` – generated database file (not committed)
- `src/load_data.py` – loads every CSV from `data/` into the database
- `src/db.py` – reads the schema, runs queries
- `src/llm.py` – builds the prompt, calls the LLM API
- `src/safety.py` – checks that the SQL is a single SELECT
- `src/app.py` – Streamlit interface
- `tests/` – unit tests for the safety checks
- `eval/` – test questions with reference SQL and the evaluation script

## Data

As an example, this project uses the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) from Kaggle.
The dataset is licensed under CC BY-NC-SA 4.0 and is intended for non-commercial use only. Because of its size and license, the CSV files are not included in this repository.

## Setup

1. Clone the repo and install dependencies: `pip install -r requirements.txt`
2. Download the dataset from Kaggle.
3. Unzip the CSV files into the `data/` folder.
4. Copy `.env.example` to `.env` and put your API key in it
5. Load the demo data: `python src/load_data.py`
6. Run the app: `streamlit run src/app.py`

## Safety

Model output is never trusted. Layers: read-only connection, single-SELECT
validation, row limit, SQL shown to the user.

## Evaluation

_To be added._

## Limitations

_To be added._