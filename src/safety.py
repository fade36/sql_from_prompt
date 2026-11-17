import sqlglot
from sqlglot import exp
from sqlglot.errors import SqlglotError

class UnsafeSQLError(Exception):
    """SQL is not a single safe SELECT."""

allowed = (exp.Select, exp.Union)

def check_sql(sql):
    try:
        statements = sqlglot.parse(sql, read="sqlite")
    except SqlglotError:
        raise UnsafeSQLError("The text could not be parsed as SQL.")

    # drop an empty string or a more then 1 - ';'
    statements = [s for s in statements if s is not None]

    if len(statements) != 1:
        raise UnsafeSQLError("Exactly one SQL statement is required.")

    if not isinstance(statements[0], allowed):
        raise UnsafeSQLError("Only SELECT queries are allowed.")