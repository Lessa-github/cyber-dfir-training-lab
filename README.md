# 🛡️ Cyber DFIR Training Lab & Purple Team Automation

[![Documentation](https://img.shields.io/badge/Docs-Docsify_Live-06b6d4?style=for-the-badge&logo=googledocs&logoColor=white)](https://lessa-github.github.io/cyber-dfir-training-lab/)
[![MITRE ATT&CK](https://img.shields.io/badge/Coverage-344_Techniques-red?style=for-the-badge&logo=target&logoColor=white)](https://attack.mitre.org)
[![Engine](https://img.shields.io/badge/DFIR-Velociraptor_67MB_RAM-10b981?style=for-the-badge&logo=go&logoColor=white)](https://docs.velociraptor.app)
[![Status](https://img.shields.io/badge/Sandbox-Airgapped_vmbr1-blue?style=for-the-badge)](https://lessa-github.github.io/gabriel-portfolio/)

Autonomous Digital Forensics, Incident Response (DFIR), and purple team adversarial emulation platform built inside an isolated Proxmox VE environment.

The lab provides safe malware detonation inside an **air-gapped sandbox (`vmbr1`) and validates 344 MITRE ATT&CK techniques** without relying on heavy Java or Elasticsearch SIEM clusters.

---

## ⚡ Engineering Highlight: Enterprise DFIR in 67 MB RAM

While conventional Wazuh, Elastic Security, or Splunk clusters require between **4 and 8 GB of RAM** just to keep the ingestion stack operational, this lab deploys a lean, high-velocity architecture:
* **Velociraptor Server:** Static Go binary compiled for Linux musl, running with an exact **67 MB physical RAM footprint**.
* **VQL (Velociraptor Query Language):** Live memory-speed anomaly hunting across endpoints, collecting only necessary forensic artifacts.
* **Storage Reduction:** Eliminates terabytes of verbose log indexing; artifacts are pulled on demand via declarative queries.

```
┌────────────────────────────────────────────────────────────────────────┐
│               HOMELAB FORENSIC RESOURCE CONSUMPTION BENCHMARK          │
├────────────────────────┬─────────────┬─────────────┬───────────────────┤
│ Platform               │ Idle RAM    │ Average CPU │ Monthly Disk I/O  │
├────────────────────────┼─────────────┼─────────────┼───────────────────┤
│ Wazuh + OpenSearch     │ ~6,200 MB   │ 12 - 25%    │ ~45 GB (Indices)  │
│ Splunk Enterprise      │ ~4,800 MB   │ 10 - 18%    │ ~60 GB (Indexed)  │
│ Velociraptor (Go Core) │ 67 MB       │ < 1.5%      │ < 2 GB (Raw DFIR) │
└────────────────────────┴─────────────┴─────────────┴───────────────────┤
  Hardware Efficiency: 98.9% physical RAM reduction!
```

---

## 📐 Air-Gapped Sandbox Topology (`vmbr1`)

```mermaid
flowchart TD
    subgraph HYPERVISOR ["Proxmox VE Hypervisor Host"]
        Bridge0["vmbr0 (Production Network / 172.28.40.0/24)"]
        Bridge1["vmbr1 (Air-Gapped Sandbox / 192.168.199.0/24)"]
    end

    subgraph PROD_NET ["Production & Monitoring"]
        Bridge0 --> VelServer["Velociraptor Server (IP: 172.28.40.123)"]
        Bridge0 --> Admin["SOC Analyst Workstation"]
    end

    subgraph ISOLATED_SANDBOX ["Strictly Contained Detonation Environment"]
        Bridge1 --> Victim1["VM 205 Lab Target (Metasploitable / Windows Test)"]
        Bridge1 --> INetSim["CT 202 INetSim Daemon (Fake DNS, HTTP, SMTP)"]
        Bridge1 --> VeloAgent["Velociraptor Client (Endpoint Telemetry)"]
    end

    VelServer -.->|Mutual mTLS Dedicated Pipe| VeloAgent
    Victim1 -->|All Synthetic Traffic Trapped| INetSim
```

---

## 🎯 Purple Teaming & MITRE ATT&CK Coverage

The automated test harness executes atomic tests with guaranteed post-run cleanup:

| MITRE ATT&CK Tactic | Technique ID & Name | Forensic VQL Artifact |
| :--- | :--- | :--- |
| **Execution** | T1059.001 (PowerShell Obfuscated Commands) | `Generic.Client.ProcessTracker` |
| **Persistence** | T1547.001 (Registry Run Keys & Startup Folder) | `Windows.Sys.Autoruns` |
| **Privilege Escalation** | T1068 (Exploitation for Privilege Escalation) | `Linux.Sys.PrivilegeAudit` |
| **Defense Evasion** | T1070.004 (File Deletion & Timestomping) | `Windows.NTFS.MFT` / `Linux.Search.FileFinder` |
| **Credential Access** | T1003.001 (LSASS Process Memory Dumping) | `Windows.Detection.MemoryInjection` |
| **Discovery** | T1082 (System Information Discovery) | `Generic.System.Info` |

---

## 🛠️ CLI Orchestrator: `homelab-soc.py`

```text
===================================================================
  HOMELAB-SOC - Autonomous Incident Response & DFIR Orchestrator
===================================================================
Usage: ./homelab-soc [COMMAND] [ARGUMENTS]

Commands:
  hunt <vql_artifact>      Execute a forensic threat hunt across all endpoints
  simulate <mitre_id>      Trigger Atomic Red Team technique in air-gapped target
  verify <sigma_rule>      Validate if recent telemetry triggered a detection rule
  quarantine <client_id>   Isolate target endpoint at the kernel bridge layer

Options:
  --target-ct <id>         Specify target LXC or VM ID (default: test sandbox)
  --format <table|json>    Output presentation format
  --dry-run                Simulate execution without running atomic payload
  --help                   Display command options and forensic syntax
```

---

## 🌐 Live Technical Documentation

Explore the complete single-page interactive whitepaper with smooth section scrolling:

👉 **[https://lessa-github.github.io/cyber-dfir-training-lab/](https://lessa-github.github.io/cyber-dfir-training-lab/)**
