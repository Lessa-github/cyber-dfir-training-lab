# ⚡ Velociraptor: Enterprise DFIR in a 67 MB RAM Baseline

**Velociraptor** is an advanced digital forensics, incident response (DFIR), and threat hunting platform written in native Go, originally designed by researchers at Google and Recursoft.

---

## 📊 Forensic Platform Hardware Benchmark

| Forensic Platform | Idle RAM Baseline | Host CPU Overhead | Monthly Storage IO | SRE Footprint Reduction |
| :--- | :---: | :---: | :---: | :---: |
| **Wazuh + OpenSearch** | ~6,200 MB | 12% – 25% | ~45 GB | Heavy SIEM Cluster |
| **Splunk Enterprise** | ~4,800 MB | 10% – 18% | ~60 GB | Enterprise Proprietary |
| **Velociraptor Server** | **67 MB** | **< 1.5%** | **< 2 GB** | **98.9% Physical RAM Reduction** |

---

## 🔒 Bidirectional mTLS Agent Communication Architecture

Endpoint agents interface with the central server over bidirectional gRPC channels secured with mutual TLS (mTLS):
* **Cryptographic Tunneling:** TLS 1.3 point-to-point encryption for all forensic telemetry.
* **Lightweight Session Polling:** Agents maintain persistent HTTP/2 sessions with near-zero idle CPU consumption.
* **In-Memory Query Evaluation:** When an investigator dispatches a *Hunt*, declarative VQL is evaluated directly within agent process memory, avoiding forensic disk contamination.
