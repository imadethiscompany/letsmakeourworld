# Witchcraft – Fast Local Semantic Search on SQLite

## Instantly find exactly what you need, right where your data lives.

**Headline:** *Search your SQLite database like magic – no server, no latency.*

**Sub‑headline:**
- Zero‑setup, zero‑maintenance local embedding index.
- Queries run in milliseconds on your own machine.
- Works offline, fully private, and works with any language.

### Why Witchcraft?
- **Speed:** Queries complete in < 200 ms on a typical laptop.
- **Privacy:** All data stays on‑device – no cloud, no API keys.
- **Simplicity:** One‑line Python API, drop‑in SQLite extension.
- **Scalability:** Handles millions of rows, incremental updates.

### How It Works (3‑Step Flow)
1. **Embed** – Call `witchcraft.embed(your_text)` to generate vector embeddings.
2. **Index** – `witchcraft.create_index(db_path)` builds a local HNSW index inside SQLite.
3. **Search** – `witchcraft.search(query, top_k=5)` returns the most relevant rows instantly.

### Ready to Try?
[**Start Your Free Trial →**](https://witchcraft.ai/pay)  
*(No credit card required – get a fully‑featured local instance for 30 days.)*

---
**FAQ**
- *Do I need an internet connection?* No – everything runs locally.
- *Can I use existing SQLite databases?* Absolutely, just point Witchcraft at the file.
- *What languages are supported?* Python, Node.js, Rust – more coming.

---
**Contact**
If you have questions, email us at support@witchcraft.ai.
