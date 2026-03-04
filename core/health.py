from core.database import get_connection

def log_run(status, message):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO runs (status, message)
        VALUES (?, ?)
    """, (status, message))

    conn.commit()
    conn.close()