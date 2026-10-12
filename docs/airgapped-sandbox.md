# 🧱 Sandbox Air-Gapped & Simulação INetSim

Para detonar malwares com segurança absoluta e sem risco de contaminação cruzada com a rede de produção ou com a internet residencial, construímos uma **bridge Proxmox estritamente isolada (`vmbr1`)**.

---

## 🔒 Arquitetura da Bridge `vmbr1`

```mermaid
flowchart LR
    subgraph AIRGAPPED_NET ["Bridge Isolada vmbr1 (192.168.199.0/24)"]
        direction TB
        MalwareTarget["VM Cobaia (192.168.199.205)<br>[Malware Executando]"]
        INetSim["CT INetSim (192.168.199.202)<br>[Serviços Falsos de Internet]"]
        VeloAgent["Velociraptor Agent<br>[Coleta de Artefatos Forenses]"]
    end

    MalwareTarget -->|Consultas DNS Sintéticas (Porta 53)| INetSim
    MalwareTarget -->|Payloads HTTP/HTTPS Falsos| INetSim
    MalwareTarget -.->|Detecção em Memória| VeloAgent
```

---

## 🎭 O Papel do INetSim

Muitos malwares modernos encerram sua execução imediatamente se detectarem que a internet está inativa. O **INetSim** resolve esse problema simulando serviços comuns da internet:
* **DNS Falso:** Responde a qualquer domínio com o IP do próprio simulador (`192.168.199.202`).
* **HTTP / HTTPS:** Retorna códigos HTTP 200 e páginas HTML fictícias.
* **SMTP / FTP / NTP:** Responde requisições de e-mail e sincronização de tempo, enganando o malware e forçando-o a revelar seus estágios secundários de infecção na memória.
