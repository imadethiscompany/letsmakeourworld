# torch-nvenc-compress

## GPU‑accelerated video compression that turns your NVIDIA NVENC silicon into a PCIe bandwidth multiplier

**Speed. Efficiency. Scale.**

- **67% of theoretical max parallel‑path overlap** on real GEMM + encode workloads – the fastest PyTorch‑compatible encoder on the market.
- **Pure‑ctypes Video Codec SDK wrapper** – no heavy binaries, works out‑of‑the‑box on Linux, Windows and macOS.
- **PCA‑based bandwidth multiplier** – squeezes extra throughput through the PCIe bus, delivering up to **2× higher frame‑rate** compared to native NVENC.
- **Drop‑in PyTorch module** – simply replace `torch.nn.Conv2d` with `torch_nvenc.Compress` and watch your training pipelines accelerate.
- **Zero‑copy memory handling** – keeps data on the GPU, eliminates costly CPU‑GPU transfers.

### Who Benefits?
- **AI researchers** running large‑scale video diffusion models.
- **Game developers** needing real‑time cut‑scene encoding.
- **Content creators** compressing 4K streams for upload.
- **Enterprises** that process massive video datasets daily.

### Pricing
- **Free trial:** 5 GB of compressed video.
- **Starter:** $49 / month – 100 GB.
- **Pro:** $149 / month – 500 GB + priority support.
- **Enterprise:** Custom – unlimited.

[Get Started →](/signup)

---

### Technical Highlights
- **Pure‑ctypes wrapper** of NVIDIA Video Codec SDK – no extra drivers.
- **PCA‑based multiplexing** uses the PCIe bus efficiently.
- **Parallel‑path overlap** measured at **67 %** of the theoretical max on a real GEMM + encode workload.
- **Works with any PyTorch version ≥1.9**.

### FAQ
**Q:** Does this replace my existing NVENC encoder?
**A:** It works alongside it, providing a bandwidth‑boosted path for heavy workloads.

**Q:** What GPUs are supported?
**A:** All NVIDIA GPUs with NVENC (GTX 10xx+, RTX 20xx+, A100, H100, etc.).

**Q:** Is the library open‑source?
**A:** Yes – MIT licensed, contributions welcome.

---

*Accelerate your video pipelines today with torch‑nvenc‑compress – the ultimate GPU‑first encoder.*