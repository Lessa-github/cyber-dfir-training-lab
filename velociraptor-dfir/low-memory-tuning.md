# Guia de Otimização do Servidor Velociraptor (67 MB RAM)

## Por que Velociraptor em vez de Wazuh?
* **Wazuh Manager + Indexer (OpenSearch):** Exige no mínimo 4 GB de memória RAM dedicada apenas para subir o daemon Java.
* **Velociraptor (Go):** Binário único estático (`velociraptor-v0.77.3-linux-amd64-musl`). Banco de dados embutido baseado em flat-files.

### Consumo Medido em Produção:
```text
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
velocir+ 14210  0.2  0.2 712400 68608 ?        Ssl  14:00   0:08 /usr/local/bin/velociraptor --config /etc/velociraptor/server.config.yaml frontend
```
Exatamente **67 Megabytes de RAM física** consumidos em repouso.
