# Silk: Open‑source Cooperative Fiber Scheduler

## Supercharge Your Rust Services with Cooperative Multitasking

**Silk** is a lightweight, open‑source fiber scheduler that lets you run thousands of concurrent tasks with near‑zero overhead. Forget heavyweight async runtimes – Silk cooperates across fibers, giving you deterministic performance and simpler code.

---

### Why Choose Silk?
- **Blazing Speed** – Up to 3× faster than Tokio for I/O‑bound workloads.
- **Zero‑Cost Context Switches** – Fibers share a single OS thread, eliminating thread‑pool contention.
- **Easy Integration** – Drop‑in API works with existing `std::future` code.
- **Fully Open‑Source** – MIT license, community‑driven roadmap, and transparent governance.

---

### How It Works
1. **Create a Fiber** – Wrap any async block with `silk::fiber`.
2. **Schedule Cooperatively** – Fibers yield voluntarily, letting others run.
3. **Run the Scheduler** – One call to `silk::run()` drives the whole system.

```rust
use silk::fiber;

let f = fiber(async move {
    // your async code here
});

silk::run();
```

---

### Who Benefits?
- **Rust Backend Engineers** building high‑throughput services.
- **Embedded Systems** needing predictable latency.
- **Open‑Source Maintainers** looking for a community‑friendly runtime.

---

### Get Started Now
- **GitHub:** https://github.com/silk-scheduler/silk
- **Documentation:** https://silk.dev/docs
- **Join the Community:** Discord & mailing list (link below)

[**Download Latest Release**](https://github.com/silk-scheduler/silk/releases/latest) – **Free & Open‑Source**

---

### Frequently Asked Questions
**Q:** Does Silk replace Tokio?
**A:** It can complement or replace Tokio for workloads that benefit from cooperative scheduling.

**Q:** Is there commercial support?
**A:** Yes – we offer paid support contracts and custom integration services.

**Q:** How many fibers can I run?
**A:** Practically unlimited – limited only by memory.

---

### Ready to Accelerate Your Rust Apps?

[**Get a Support Contract**](https://silk.dev/support) – 30‑day money‑back guarantee.

---

*Silk is maintained by a global community of Rust developers. Join us and shape the future of cooperative multitasking.*
