# Configuração da Bridge Isolada vmbr1 no Proxmox

No arquivo `/etc/network/interfaces` do Proxmox host:

```text
auto vmbr1
iface vmbr1 inet manual
	bridge-ports none
	bridge-stp off
	bridge-fd 0
# Bridge isolada air-gapped para o CyberLab (sem IP no host e sem gateway)
```

Nenhum container ou VM conectado à `vmbr1` consegue alcançar a rede `172.28.40.0/24` ou a internet física.
