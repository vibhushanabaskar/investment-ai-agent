import sqlite3


def get_accuracy():

    conn = sqlite3.connect("investment.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT result FROM performance
        WHERE result != 'NEUTRAL'
    """)

    rows = cur.fetchall()

    conn.close()

    if not rows:
        return 0

    correct = sum(1 for r in rows if r[0] == "CORRECT")

    accuracy = correct / len(rows)

    return round(accuracy * 100, 2)