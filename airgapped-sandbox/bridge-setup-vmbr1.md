# Proxmox VE Isolated L2 Bridge Configuration (`vmbr1`)

Configured within `/etc/network/interfaces` on the Proxmox VE host:

```text
auto vmbr1
iface vmbr1 inet manual
	bridge-ports none
	bridge-stp off
	bridge-fd 0
# Air-gapped isolated virtual switch for Cyber Lab detonation (no host IP, no default gateway)
```

### Isolation Guarantees:
* Zero physical NIC attachment (`bridge-ports none`).
* No host gateway assignment, trapping all frames strictly at Layer 2.
* Complete physical and logical isolation from the production subnet (`172.28.40.0/24`) and the residential WAN router.
