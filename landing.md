# Durable Queues, Streams, Pub/Sub & Cron Scheduler – All Inside Your SQLite File

**Never add another external service.**

---

## Why embed data pipelines in SQLite?
- **Zero ops** – No separate brokers, no cloud costs.
- **Atomic durability** – SQLite’s ACID guarantees protect every message.
- **Instant local latency** – Reads/writes are micro‑seconds, not network hops.
- **Portable** – Ship a single file to any server, edge, or desktop app.

---

## What you get
- **Durable Queues** – FIFO queues that survive crashes, with back‑pressure handling.
- **Realtime Streams** – Subscribe to live data changes via a lightweight pub/sub API.
- **Cron Scheduler** – Define recurring jobs using familiar cron syntax, stored in the same DB.
- **Simple API** – One‑line Python/JS/Go calls, no extra dependencies.

---

## Who benefits?
- **Start‑ups** building MVPs that can’t afford Kafka or Redis.
- **Edge developers** needing a tiny, self‑contained data pipeline.
- **IoT platforms** where each device ships a single SQLite file.

---

## Quick demo
```python
import sqlite3, sqlean

# Create a queue
conn = sqlite3.connect('app.db')
conn.execute("CREATE VIRTUAL TABLE queue USING sqlean_queue('tasks')")

# Push a job
conn.execute("INSERT INTO queue VALUES ('email', 'Send welcome email')")

# Pull a job
job = conn.execute("SELECT * FROM queue POP LIMIT 1").fetchone()
print('Processing', job)
```

---

## Ready to eliminate external brokers?
[**Get early‑access now →**](https://buy.stripe.com/example)

*No credit card required for the beta. Deploy in minutes.*
