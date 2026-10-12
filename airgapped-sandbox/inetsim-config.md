# INetSim Configuration for Synthetic Internet Emulation

The INetSim daemon binds to the following virtual ports within the isolated `192.168.199.0/24` subnet:
* **DNS (53/UDP):** Resolves all queried domain names to `192.168.199.10`, trapping Command & Control (C2) beaconing.
* **HTTP/HTTPS (80, 443/TCP):** Serves synthetic HTTP responses and benign executable binaries to satisfy secondary payload fetchers without external network egress.
* **SMTP (25/TCP):** Sinks credential exfiltration attempts and captures outbound spam payloads in memory.
