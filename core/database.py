import sqlite3

DB_PATH = "investment.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with open("models/schema.sql") as f:
        schema = f.read()

    conn = get_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()

def save_signal(ticker, signal, confidence, price):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO signals (ticker, signal, confidence, price_at_signal)
        VALUES (?, ?, ?, ?)
    """, (ticker, signal, confidence, price))

    conn.commit()
    conn.close()

def get_last_signal(ticker):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT signal FROM signals
        WHERE ticker = ?
        ORDER BY id DESC LIMIT 1
    """, (ticker,))

    row = cur.fetchone()
    conn.close()

    return row[0] if row else None