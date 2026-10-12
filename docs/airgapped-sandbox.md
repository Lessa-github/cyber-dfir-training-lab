# 🧱 Air-Gapped Sandbox & INetSim Simulation

To detonate live malware samples safely without cross-contamination risks to production services or the residential WAN, the lab operates an **isolated Proxmox L2 virtual bridge (`vmbr1`)**.

---

## 🔒 Virtual Bridge Architecture (`vmbr1`)

```mermaid
flowchart LR
    subgraph AIRGAPPED_NET ["Isolated Bridge vmbr1 (192.168.199.0/24)"]
        direction TB
        MalwareTarget["Victim Detonation VM (192.168.199.205)<br>[Malware Executing]"]
        INetSim["CT INetSim (192.168.199.202)<br>[Synthetic Internet Daemons]"]
        VeloAgent["Velociraptor Agent<br>[Forensic Artifact Ingestion]"]
    end

    MalwareTarget -->|Synthetic DNS Queries (Port 53)| INetSim
    MalwareTarget -->|Mock HTTP/HTTPS Handshakes| INetSim
    MalwareTarget -.->|Live In-Memory Telemetry| VeloAgent
```

---

## 🎭 The Role of INetSim Emulation

Modern malware families often terminate execution early upon detecting an inactive internet connection. **INetSim** eliminates sandbox evasion by emulating standard internet protocols:
* **Synthetic DNS Resolver:** Returns the simulator's IP (`192.168.199.202`) for any queried domain name.
* **HTTP / HTTPS Emulators:** Serves mock HTTP 200 responses and generic payload files to satisfy secondary droppers.
* **SMTP / FTP / NTP Daemons:** Sinks outbound credentials and synchronizes system clocks, inducing malware to execute subsequent in-memory stages without egress leaks.
