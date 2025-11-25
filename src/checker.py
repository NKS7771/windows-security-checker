from firewall import check_firewall
from antivirus import check_antivirus
from processes import check_suspicious_processes
from network import check_open_ports
from report import generate_report

def main():
    print("🔍 Executando checagens de segurança...")

    results = {
        "firewall": check_firewall(),
        "antivirus": check_antivirus(),
        "processes": check_suspicious_processes(),
        "ports": check_open_ports()
    }

    generate_report(results)
    print("📄 Relatório gerado em: data/reports/security_report.txt")

if __name__ == "__main__":
    main()
