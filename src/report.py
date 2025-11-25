import os
from datetime import datetime
import json

def generate_report(results):
    os.makedirs("data/reports", exist_ok=True)
    filename_txt = "data/reports/security_report.txt"
    filename_json = "data/reports/security_report.json"

    with open(filename_txt, "w", encoding="utf-8") as f:
        f.write("==== Windows Security Check Report ====\n")
        f.write(f"Generated at: {datetime.now()}\n\n")
        f.write(f"Firewall: {results['firewall']}\n")
        f.write(f"Antivirus: {results['antivirus']}\n")
        f.write(f"Suspicious processes: {results['processes']}\n")
        f.write(f"Open ports: {results['ports']}\n")

    with open(filename_json, "w", encoding="utf-8") as f:
        json.dump({"generated_at": str(datetime.now()), **results}, f, indent=2, ensure_ascii=False)
