# 🔍 VQL Threat Hunting Guide (Velociraptor Query Language)

VQL is a declarative SQL-like query language empowering security analysts to execute expressive investigations across filesystems, process trees, network sockets, and registry keys directly on remote endpoints.

---

## ⚡ Production VQL Threat Hunting Artifacts

### 1. Hunting Unlinked or In-Memory Hidden Processes

```sql
name: Custom.Hunt.HiddenProcesses
description: Identifies running processes whose disk binaries have been unlinked or deleted from the filesystem.

sources:
  - query: |
      SELECT Pid, Ppid, Name, CommandLine, Exe, Username
      FROM pslist()
      WHERE Exe =~ "deleted" OR NOT Exe
```

### 2. Auditing Persistence Mechanisms in Linux Systemd Units

```sql
name: Custom.Hunt.SuspiciousSystemdUnits
description: Scans newly created or modified systemd services referencing execution binaries located in /tmp or /dev/shm.

sources:
  - query: |
      SELECT Name, Path, ServiceContent
      FROM systemd()
      WHERE ServiceContent =~ "(shm|tmp|nc|bash -i)"
```
