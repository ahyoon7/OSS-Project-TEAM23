import sqlite3
from datetime import datetime

DB_NAME = "routine_records.db"


def connect_db():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS routine_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mission TEXT NOT NULL,
            completed INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_record(mission, completed=1):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO routine_records (mission, completed, created_at)
        VALUES (?, ?, ?)
    """, (mission, completed, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()


def get_all_records():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, mission, completed, created_at
        FROM routine_records
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows
