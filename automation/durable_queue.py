# Minimal durable queue, stream, pub/sub, and cron scheduler using SQLite
import sqlite3
import threading
import time
from datetime import datetime, timedelta

DB = 'durable_queue.db'

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    # Queue table
    cur.execute('''CREATE TABLE IF NOT EXISTS queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT NOT NULL,
        payload TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        processed INTEGER DEFAULT 0
    )''')
    # Cron table
    cur.execute('''CREATE TABLE IF NOT EXISTS cron (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        schedule TEXT NOT NULL,  -- ISO8601 interval e.g., 'PT5M'
        task TEXT NOT NULL,
        last_run TIMESTAMP
    )''')
    conn.commit()
    conn.close()

# Queue operations

def enqueue(topic, payload):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('INSERT INTO queue (topic, payload) VALUES (?,?)', (topic, payload))
    conn.commit()
    conn.close()

def dequeue(topic):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('SELECT id, payload FROM queue WHERE topic=? AND processed=0 ORDER BY id LIMIT 1', (topic,))
    row = cur.fetchone()
    if row:
        cur.execute('UPDATE queue SET processed=1 WHERE id=?', (row[0],))
        conn.commit()
        conn.close()
        return row[1]
    conn.close()
    return None

# Simple pub/sub using polling

def subscriber(topic, callback, poll_interval=1):
    def run():
        while True:
            msg = dequeue(topic)
            if msg:
                callback(msg)
            time.sleep(poll_interval)
    t = threading.Thread(target=run, daemon=True)
    t.start()
    return t

# Cron scheduler (basic)

def schedule_cron(task_name, interval_seconds, task_callable):
    def run():
        while True:
            task_callable()
            time.sleep(interval_seconds)
    t = threading.Thread(target=run, daemon=True)
    t.start()
    return t

# Example usage (run when script executed)
if __name__ == '__main__':
    init_db()
    # Enqueue sample
    enqueue('example', 'Hello world')
    # Subscribe
    subscriber('example', lambda msg: print('Received:', msg))
    # Cron every 10 seconds
    schedule_cron('heartbeat', 10, lambda: print('Cron tick at', datetime.now()))
    # Keep main thread alive
    while True:
        time.sleep(60)
