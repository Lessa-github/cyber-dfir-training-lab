# 🛡️ Cyber DFIR Training Lab & Purple Team Automation

Plataforma de Forense Digital, Resposta a Incidentes (DFIR) e simulação de adversários automatizada, construída em ambiente isolado no Proxmox VE.

O laboratório permite detonar malwares em sandbox air-gapped e validar 344 técnicas MITRE ATT&CK sem depender de SIEMs pesados baseados em Java ou Elasticsearch.

---

## ⚡ Destaque de Engenharia: DFIR com 67 MB de RAM
Enquanto clusters convencionais de Wazuh ou Splunk exigem entre 4 e 8 GB de RAM, este lab implementa o **Velociraptor** em binário estático Go compilado para Linux musl, consumindo exatamente **67 MB de RAM física** enquanto provê caça forense instantânea em velocidade de memória via consultas **VQL (Velociraptor Query Language)**.
