import psutil

SUSPICIOUS = ["keylogger", "rat", "trojan", "backdoor"]

def check_suspicious_processes():
    found = []
    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info.get('name', '').lower()
            for s in SUSPICIOUS:
                if s in name:
                    found.append(name)
        except Exception:
            pass
    return {"suspicious_processes": list(set(found))}
