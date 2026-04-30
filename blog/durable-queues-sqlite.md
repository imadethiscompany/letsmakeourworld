# Durable Queues, Streams, Pub/Sub, and Cron Scheduler in SQLite

**Overview**

- **Durable Queues**: Persistent job queues stored directly in SQLite, guaranteeing delivery even after process restarts.
- **Streams**: Real‑time data streams backed by SQLite tables, enabling low‑latency consumption.
- **Pub/Sub**: Publish/Subscribe pattern using SQLite triggers and a lightweight broker library.
- **Cron Scheduler**: Schedule recurring tasks with cron‑like syntax, persisted in SQLite and executed by a tiny daemon.

**Why SQLite?**
- Zero‑configuration, server‑less, single‑file deployment.
- ACID guarantees ensure reliable queue semantics.
- Ideal for edge devices, small SaaS back‑ends, or prototyping.

**Getting Started**
1. Add `sqlite-automation` package.
2. Initialize the database:
```python
import sqlite3
conn = sqlite3.connect('automation.db')
from sqlite_automation import init
init(conn)
```
3. Create a queue and push a job:
```python
from sqlite_automation import Queue
q = Queue(conn, 'email_jobs')
q.enqueue({'to': 'user@example.com', 'subject': 'Welcome'})
```
4. Consume jobs:
```python
for job in q.consume():
    send_email(job['to'], job['subject'])
```
5. Define a cron task:
```python
from sqlite_automation import Cron
cron = Cron(conn)
cron.schedule('*/5 * * * *', lambda: print('Runs every 5 minutes'))
```

**Live Demo**: https://github.com/yourorg/sqlite-automation-demo

**Buy the Full Package**: [Purchase Now](https://buy.stripe.com/example)
