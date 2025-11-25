import subprocess

def check_antivirus():
    try:
        output = subprocess.check_output(
            'wmic /namespace:\\\\root\\SecurityCenter2 path AntiVirusProduct get displayName',
            shell=True
        ).decode(errors="ignore")
        lines = [l.strip() for l in output.splitlines() if l.strip()]
        # geralmente a primeira linha é header; pegamos os nomes únicos
        installed = lines[1:] if len(lines) > 1 else ["UNKNOWN"]
        return {"installed": installed}
    except Exception as e:
        return {"installed": ["UNKNOWN"], "error": str(e)}
