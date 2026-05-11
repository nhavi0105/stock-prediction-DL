import sqlite3
import pandas as pd

DB_NAME = "stock.db"

def save_to_db(df):
    conn = sqlite3.connect(DB_NAME)

    df.to_sql(
        "predictions",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()


def load_latest():
    conn = sqlite3.connect(DB_NAME)

    query = """
    SELECT * FROM predictions
    ORDER BY timestamp DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()
    return df