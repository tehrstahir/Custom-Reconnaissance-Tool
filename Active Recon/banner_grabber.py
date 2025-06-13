import socket
import ssl
import requests

def grab_banner(ip_or_domain, ports):
    results = {}
    for port in ports:
        try:
            if port in [80, 8080]:  # HTTP
                response = requests.get(f"http://{ip_or_domain}:{port}", timeout=5)
                server = response.headers.get("Server", "No Server Header")
                results[port] = f"HTTP Banner: {server}"
            elif port == 443:  # HTTPS
                response = requests.get(f"https://{ip_or_domain}", timeout=5, verify=False)
                server = response.headers.get("Server", "No Server Header")
                results[port] = f"HTTPS Banner: {server}"
            else:
                # Fallback to raw socket for other ports (FTP, SSH, etc.)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((ip_or_domain, port))
                banner = sock.recv(1024).decode(errors='ignore').strip()
                results[port] = banner if banner else "No banner received"
                sock.close()
        except requests.exceptions.RequestException as e:
            results[port] = f"HTTP/HTTPS Error: {str(e)}"
        except socket.timeout:
            results[port] = "Connection timed out"
        except Exception as e:
            results[port] = f"Error: {str(e)}"
    return results
