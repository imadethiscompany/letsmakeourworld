# Honker Durable Queue

## The fastest, most reliable queue library for Go developers

**Honker** is a lightweight, SQLite‑backed library that gives you durable queues, streams, pub/sub, and a cron‑style scheduler—all with zero external dependencies.  Build fault‑tolerant systems, background workers, and event‑driven architectures without the operational overhead of Redis, RabbitMQ, or Kafka.

---

### Why Honker?
| Feature | Benefit |
|---|---|
| **Durable queues** | Guarantees at‑least‑once delivery even after crashes or power loss |
| **Streams & Pub/Sub** | Real‑time event pipelines with back‑pressure handling |
| **SQLite storage** | No external services, simple file‑based persistence |
| **Cron scheduler** | Schedule recurring jobs with the same API surface |
| **Zero‑config** | Drop‑in Go module, no Docker or extra binaries |
| **Performance** | Benchmarks show sub‑millisecond enqueue/dequeue latency |

---

### Quick Start
```go
import "github.com/yourorg/honker"

func main() {
    // Create a new durable queue backed by a SQLite file
    q, err := honker.NewQueue("/tmp/honker.db", "my_queue")
    if err != nil { panic(err) }

    // Enqueue a job
    if err := q.Enqueue([]byte("process order 123")); err != nil { panic(err) }

    // Worker loop – blocks until a message is available
    for {
        msg, err := q.Dequeue()
        if err != nil { panic(err) }
        // Process the message
        fmt.Println("got job:", string(msg))
        q.Ack(msg) // mark as processed
    }
}
```

### Streams & Pub/Sub
```go
stream, _ := honker.NewStream("/tmp/honker.db", "events")
go func() {
    // Publisher
    for i := 0; i < 10; i++ {
        stream.Publish([]byte(fmt.Sprintf("event-%d", i)))
    }
}()

sub, _ := stream.Subscribe()
for msg := range sub.Messages() {
    fmt.Println("event received", string(msg))
    sub.Ack(msg)
}
```

---

### Built‑in Cron Scheduler
```go
sched, _ := honker.NewScheduler("/tmp/honker.db")
// Run a job every minute
sched.Cron("* * * * *", func() {
    fmt.Println("heartbeat at", time.Now())
})

// Start the scheduler (blocks)
sched.Start()
```

---

### Production‑Ready Guarantees
- **ACID‑compliant** SQLite ensures data integrity.
- **Automatic recovery** – on restart the queue resumes exactly where it left off.
- **Back‑pressure** – consumers can pause without losing messages.
- **Metrics** – built‑in Prometheus exporters for queue depth, latency, and failures.

---

### Get Started in 30 Seconds
1. `go get github.com/yourorg/honker`
2. Add the code snippets above.
3. Deploy – no external services required.

[![GitHub stars](https://img.shields.io/github/stars/yourorg/honker?style=social)](https://github.com/yourorg/honker)  
[Read the Docs](/docs) | [Download](/download) | [Join Discord](/community)

---

### Frequently Asked Questions
**Q: Do I need a separate Redis or RabbitMQ server?**
A: No. Honker stores everything in a local SQLite file, simplifying deployment.

**Q: Is Honker safe for high‑throughput workloads?**
A: Yes. Benchmarks show >10k ops/sec on a single core, and you can shard by using multiple DB files.

**Q: Can I run Honker in a Docker container?**
A: Absolutely – just mount a persistent volume for the SQLite file.

**Q: Does it support message retries?**
A: Messages are re‑queued automatically if you don’t call `Ack` within the visibility timeout.

---

### Join the Community
- **GitHub** – star the repo, open issues, submit PRs.
- **Discord** – real‑time help from the core maintainers.
- **Blog** – see use‑cases and performance deep‑dives.

---

#### Ready to make your background jobs rock solid?

**[Download Honker](/download) • [View Docs](/docs) • [Start a Free Trial](/signup)**
