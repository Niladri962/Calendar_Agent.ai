# db.py
import sqlite3

conn = sqlite3.connect("data/events.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    date TEXT,
    time TEXT
)
""")

def add_event(title, date, time):
    cursor.execute("INSERT INTO events (title, date, time) VALUES (?, ?, ?)", 
                   (title, date, time))
    conn.commit()

def get_events():
    cursor.execute("SELECT * FROM events")
    return cursor.fetchall()

def clear_events():
    cursor.execute("DELETE FROM events")
    conn.commit()