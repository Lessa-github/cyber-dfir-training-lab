# Configuração do INetSim para Simulação de Serviços Falsos

O INetSim responde nas seguintes portas dentro da rede `192.168.199.0/24`:
* **DNS (53/udp):** Responde a qualquer lookup apontando para `192.168.199.10`.
* **HTTP/HTTPS (80, 443/tcp):** Entrega binários PE falsos e páginas padrão para desarmar estágios secundários de downloaders maliciosos.
* **SMTP (25/tcp):** Captura tentativas de exfiltração de credenciais via e-mail.
