# 🔍 Guia de Consultas VQL (Velociraptor Query Language)

O VQL é uma linguagem declarativa similar a SQL que permite aos analistas de segurança fazer consultas complexas em arquivos, processos, conexões e chaves de registro diretamente nos endpoints.

---

## ⚡ Exemplos Práticos de VQL Utilizados no Laboratório

### 1. Caça a Processos com Executáveis Ocultos ou Desvinculados

```sql
name: Custom.Hunt.HiddenProcesses
description: Localiza processos em execução onde o binário no disco foi apagado ou renomeado.

sources:
  - query: |
      SELECT Pid, Ppid, Name, CommandLine, Exe, Username
      FROM pslist()
      WHERE Exe =~ "deleted" OR NOT Exe
```

### 2. Auditoria de Persistência em Inicialização (Linux Systemd)

```sql
name: Custom.Hunt.SuspiciousSystemdUnits
description: Varre serviços recém-adicionados no systemd procurando scripts em /tmp ou /dev/shm.

sources:
  - query: |
      SELECT Name, Path, ServiceContent
      FROM systemd()
      WHERE ServiceContent =~ "(shm|tmp|nc|bash -i)"
```
