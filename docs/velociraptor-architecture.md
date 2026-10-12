# ⚡ Velociraptor: DFIR Corporativo em 67 MB de RAM

O **Velociraptor** é uma plataforma avançada de resposta a incidentes e caça digital desenvolvida originalmente por pesquisadores da Google/Recursoft e escrita em Go nativo.

---

## 📊 Análise Comparativa de Hardware

```
┌────────────────────────────────────────────────────────────────────────┐
│             BENCHMARK FORENSE: CONSUMO EM AMBIENTE HOMELAB             │
├────────────────────────┬─────────────┬─────────────┬───────────────────┤
│ Plataforma             │ RAM Idle    │ CPU Médio   │ Armazenamento Mês │
├────────────────────────┼─────────────┼─────────────┼───────────────────┤
│ Wazuh + OpenSearch     │ ~6.200 MB   │ 12 - 25%    │ ~45 GB            │
│ Splunk Enterprise      │ ~4.800 MB   │ 10 - 18%    │ ~60 GB            │
│ Velociraptor Server    │ 67 MB       │ < 1.5%      │ < 2 GB            │
└────────────────────────┴─────────────┴─────────────┴───────────────────┤
  Redução de Footprint de Memória: 98.9%
```

---

## 🔒 Arquitetura de Comunicação mTLS

Os clientes comunicam-se com o servidor através de canais gRPC bidirecionais mutuamente autenticados com certificados criptográficos dedicados:
* **Canal Criptografado:** Criptografia TLS 1.3 ponta a ponta.
* **Polling Leve:** Agentes mantêm sessões HTTP/2 ativas com quase zero consumo de CPU em repouso.
* **Execução em Memória:** Quando o analista dispara uma *Hunt*, o código VQL é interpretado na memória volátil do agente sem gravar binários em disco.
