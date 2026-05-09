# Nylas CLI

## Supercharge Your Email & Calendar Automation

**Write once, run everywhere.**

Nylas CLI lets developers interact with the Nylas API directly from their terminal—no SDKs, no boilerplate, just fast, reliable automation.

---

### Why Nylas CLI?
- **Instant setup** – Install with a single `npm i -g nylas-cli` and start syncing in seconds.
- **Full API coverage** – Access email, calendar, contacts, and webhooks without writing code.
- **Secure & compliant** – OAuth2 token management, GDPR‑ready, and PCI‑level encryption.
- **Team friendly** – Share scripts across your org, version‑control them, and audit every run.

---

### Key Benefits
1. **Cut integration time by 80%** – No more waiting for SDK releases.
2. **Reduce operational costs** – Automate inbox triage, meeting scheduling, and follow‑ups from the command line.
3. **Boost developer productivity** – Prototype features in minutes, ship to production in hours.
4. **Maintain compliance** – Built‑in consent handling and audit logs.

---

### How It Works
1. **Authenticate** – `nylas login` opens a secure OAuth flow.
2. **Run commands** – `nylas messages list --inbox`, `nylas events create "Team Sync" --when tomorrow 10am`.
3. **Pipe & script** – Combine with `jq`, `grep`, or any shell tool to build powerful pipelines.

---

### Quick Start
```bash
# Install globally
npm i -g nylas-cli

# Authenticate your account
nylas login

# List recent emails
nylas messages list --limit 10

# Auto‑reply all unread messages
nylas messages list --unread | nylas messages reply --template "Thanks for reaching out! I’ll get back shortly."
```

---

### Who Should Use Nylas CLI?
- **Developers** building email‑driven features.
- **Ops teams** automating inbox cleanup and calendar syncs.
- **Product managers** prototyping workflows without writing a line of code.

---

### Frequently Asked Questions
**Q:** Do I need a Nylas account?
**A:** Yes – sign up for a free developer account and get 10,000 API calls/month.

**Q:** Is it secure?
**A:** All traffic is encrypted; tokens are stored locally with OS‑level protection.

**Q:** Can I use it in CI/CD pipelines?
**A:** Absolutely – the CLI works in any environment with Node.js.

---

### Get Started Now
[**Download Nylas CLI**](https://www.nylas.com/cli) – No credit card required.

---

*Boost your productivity. Automate email & calendar tasks with a single command.*
