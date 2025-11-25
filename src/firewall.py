import subprocess

def check_firewall():
    try:
        output = subprocess.check_output(
            'netsh advfirewall show allprofiles', shell=True
        ).decode(errors="ignore")

        status = "ON" if "State ON" in output else "OFF"
        return {"status": status}
    except Exception as e:
        return {"status": "UNKNOWN", "error": str(e)}
