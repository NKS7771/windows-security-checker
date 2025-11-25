import socket

def check_open_ports():
    ports_to_check = [21, 22, 23, 80, 443, 3389]
    open_ports = []
    for port in ports_to_check:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex(("127.0.0.1", port))
            if result == 0:
                open_ports.append(port)
    return {"open_ports": open_ports}
