# 🎯 Purple Teaming & Cobertura MITRE ATT&CK

Nossa abordagem de Purple Teaming combina o ataque simulado com a validação defensiva imediata.

---

## 📋 Matriz de Testes com Atomic Red Team

A esteira de automação cobre **344 técnicas da matriz MITRE ATT&CK Enterprise**:

```mermaid
flowchart LR
    A["Atomic Runner (Python)"] -->|1. Dispara Técnica MITRE| B["Alvo Cobaia"]
    B -->|2. Gera Telemetria| C["Agente Velociraptor"]
    C -->|3. Consulta VQL Coleta Evidência| D["Validador Sigma"]
    A -->|4. Executa Auto-Cleanup| B
    D -->|5. Confirma Detecção| E["Relatório SOC"]
```

### Exemplos de Técnicas Validadas:
* **T1059.001 - PowerShell Execution:** Validação de processos com parâmetros codificados em Base64.
* **T1547.001 - Registry Run Keys:** Criação de chaves de persistência no registro do Windows / systemd units no Linux.
* **T1003.001 - OS Credential Dumping:** Tentativas de acesso direto à memória de processos sensíveis.
* **T1070.004 - Timestomping:** Manipulação deliberada de datas de modificação de arquivos para enganar peritos.
