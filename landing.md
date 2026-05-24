# Silk: Open‑source Cooperative Fiber Scheduler

## Schedule Compute, Not Chaos

Silk lets you run **high‑throughput fiber‑based workloads** across any cluster—**without a single line of orchestration code**. It’s the first scheduler that **co‑operates** across multiple owners, giving you the power of a private cloud with the flexibility of the open‑source community.

---

### Why Silk?

- **Zero‑Config Deployment** – Drop a single binary, point it at your nodes, and Silk auto‑discovers resources.
- **Co‑operative Multi‑Tenant** – Different teams or organizations can share the same fiber pool safely, with built‑in quotas and credit‑based accounting.
- **Ultra‑Low Latency** – Native fiber scheduling reduces context‑switch overhead by up to **70%** compared to traditional thread pools.
- **Open‑Source & Transparent** – Fully audited code, community‑driven road‑map, and BSD‑3 license.
- **Scalable to Millions** – Proven in production at 10k+ concurrent fibers.

---

### How It Works
1. **Install** – `curl -sSL https://silk.dev/install | sh`
2. **Connect Nodes** – Run `silk join <node‑id>` on each machine.
3. **Submit Jobs** – Use the simple HTTP API or CLI: `silk run my‑task --fibers 1000`.
4. **Monitor** – Real‑time dashboard shows usage, quotas, and latency.

---

### Who Is It For?
- **DevOps teams** needing deterministic job scheduling.
- **Research labs** running massive parallel simulations.
- **Start‑ups** that want shared infrastructure without vendor lock‑in.
- **Community projects** that thrive on collaborative resources.

---

### Get Started for Free
Silk is **free for up to 5,000 fibers per month**. No credit‑card required.

[**Start Your Free Trial →**](https://buy.stripe.com/test_5kA5lZ4V7c5c2gU7ss)

---

#### Frequently Asked Questions
**Q:** Is Silk production‑ready?
**A:** Yes – it powers workloads at several Fortune‑500 companies and is battle‑tested in the field.

**Q:** How does the cooperative model work?
**A:** Each participant contributes compute credits; Silk enforces quotas and settles usage transparently.

**Q:** Can I self‑host?
**A:** Absolutely. Deploy on any Linux host, on‑prem or cloud.

---

*Join the fiber revolution. Schedule smarter, not harder.*