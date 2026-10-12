# Velociraptor Memory Optimization Guide (67 MB RAM Baseline)

## Architectural Benchmarking: Velociraptor vs. Wazuh SIEM
* **Wazuh Manager + OpenSearch Cluster:** Requires a minimum of 4,096 MB to 6,144 MB of dedicated RAM merely to initialize JVM heaps and Elasticsearch indices.
* **Velociraptor (Static Go Binary):** Single self-contained static binary (`velociraptor-linux-amd64-musl`) utilizing lightweight flat-file telemetry datastores without Java runtime bloat.

### Measured Memory Footprint:
```text
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
velocir+ 14210  0.2  0.2 712400 68608 ?        Ssl  14:00   0:08 /usr/local/bin/velociraptor --config /etc/velociraptor/server.config.yaml frontend
```
Operates at exactly **67 Megabytes of physical resident RAM (RSS)** in steady state.
