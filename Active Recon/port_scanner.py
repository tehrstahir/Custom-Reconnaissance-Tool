import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                return port
    except Exception:
        return None
    return None

def socket_scan(host):
    open_ports = []
    with ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(scan_port, host, port) for port in range(1, 65536)]
        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)
    return open_ports
