import sqlite3
import yfinance as yf


def update_performance():

    conn = sqlite3.connect("investment.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT id, ticker, signal, price_at_signal
        FROM signals
        WHERE id NOT IN (
            SELECT id FROM performance
        )
    """)

    rows = cur.fetchall()

    for row in rows:

        id_, ticker, signal, entry_price = row

        try:

            data = yf.download(ticker, period="5d")

            if len(data) < 3:
                continue

            future_price = data["Close"].iloc[-1]

            if signal == "BUY":
                result = "CORRECT" if future_price > entry_price else "WRONG"

            elif signal == "SELL":
                result = "CORRECT" if future_price < entry_price else "WRONG"

            else:
                result = "NEUTRAL"

            cur.execute("""
                INSERT INTO performance
                (id, ticker, signal, price_at_signal, price_after, result)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (id_, ticker, signal, entry_price, future_price, result))

        except:
            continue

    conn.commit()
    conn.close()