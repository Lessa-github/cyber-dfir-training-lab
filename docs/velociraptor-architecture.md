# ⚡ Velociraptor: Enterprise DFIR in a 67 MB RAM Baseline

**Velociraptor** is an advanced digital forensics, incident response (DFIR), and threat hunting platform written in native Go, originally designed by researchers at Google and Recursoft.

---

## 📊 Forensic Platform Hardware Benchmark

```
┌────────────────────────────────────────────────────────────────────────┐
│             FORENSIC BENCHMARK: HOMELAB HIGH-DENSITY PROFILE           │
├────────────────────────┬─────────────┬─────────────┬───────────────────┤
│ Platform               │ Idle RAM    │ Average CPU │ Monthly Storage   │
├────────────────────────┼─────────────┼─────────────┼───────────────────┤
│ Wazuh + OpenSearch     │ ~6,200 MB   │ 12 - 25%    │ ~45 GB            │
│ Splunk Enterprise      │ ~4,800 MB   │ 10 - 18%    │ ~60 GB            │
│ Velociraptor Server    │ 67 MB       │ < 1.5%      │ < 2 GB            │
└────────────────────────┴─────────────┴─────────────┴───────────────────┘
  Memory Footprint Reduction: 98.9%
```

---

## 🔒 Bidirectional mTLS Agent Communication Architecture

Endpoint agents interface with the central server over bidirectional gRPC channels secured with mutual TLS (mTLS):
* **Cryptographic Tunneling:** TLS 1.3 point-to-point encryption for all forensic telemetry.
* **Lightweight Session Polling:** Agents maintain persistent HTTP/2 sessions with near-zero idle CPU consumption.
* **In-Memory Query Evaluation:** When an investigator dispatches a *Hunt*, declarative VQL is evaluated directly within agent process memory, avoiding forensic disk contamination.
