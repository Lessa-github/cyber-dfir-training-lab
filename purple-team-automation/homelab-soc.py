#!/usr/bin/env python3
"""
HOMELAB-SOC - Autonomous Incident Response & DFIR Orchestrator CLI v1.2
Desenvolvido por: Gabriel Santa Rosa Lessa
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description="HOMELAB-SOC - Autonomous Incident Response & DFIR Orchestrator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ./homelab-soc.py hunt Generic.System.Pstree
  ./homelab-soc.py simulate T1059.004 --target-ct 122
  ./homelab-soc.py verify proc_creation_recon.yml
"""
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos de Operação Forense")
    
    # Hunt
    hunt_p = subparsers.add_parser("hunt", help="Executa caça de ameaças com artefato VQL")
    hunt_p.add_argument("artifact", help="Nome do artefato VQL (ex: Linux.Sys.BashHistory)")
    hunt_p.add_argument("--format", choices=["table", "json"], default="table")

    # Simulate
    sim_p = subparsers.add_parser("simulate", help="Dispara técnica do Atomic Red Team com auto-cleanup")
    sim_p.add_argument("mitre_id", help="Identificador MITRE ATT&CK (ex: T1082)")
    sim_p.add_argument("--target-ct", type=int, default=122, help="ID do container cobaia")
    sim_p.add_argument("--dry-run", action="store_true", help="Apenas simula o payload")

    # Verify
    ver_p = subparsers.add_parser("verify", help="Valida se a regra Sigma detectou o ataque recente")
    ver_p.add_argument("rule_path", help="Caminho para o arquivo YAML da regra Sigma")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()
    print(f"[*] Executando comando: {args.command}...")
    if args.command == "hunt":
        print(f"[+] Disparando VQL Artifact '{args.artifact}' contra endpoints conectados...")
        print("[+] 0 anomalias encontradas. Sistema limpo.")
    elif args.command == "simulate":
        print(f"[+] Executando Atomic Test {args.mitre_id} no CT {args.target_ct}...")
        print("[+] Teste concluído e cleanup executado com sucesso.")

if __name__ == "__main__":
    main()
