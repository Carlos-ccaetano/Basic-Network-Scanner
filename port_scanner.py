import socket
import json

def scan_port(host, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host, port))
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def scan_common_ports(host, common_ports=None):
    if common_ports is None:
        common_ports = {
            20: "FTP Data",
            21: "FTP Control",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            135: "MSRPC",
            139: "NetBIOS Session Service",
            143: "IMAP",
            443: "HTTPS",
            445: "SMB",
            3389: "RDP",
            8080: "HTTP Proxy"
        }

    open_ports = []
    print(f"Escaneando portas comuns em {host}...")
    for port, service in common_ports.items():
        if scan_port(host, port):
            print(f"  Porta {port} ({service}): Aberta")
            open_ports.append({"port": port, "service": service, "status": "Aberta"})
        else:
            print(f"  Porta {port} ({service}): Fechada")
            open_ports.append({"port": port, "service": service, "status": "Fechada"})
    return open_ports

def export_to_json(data, filename='scan_results.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Resultados exportados para {filename}")


if __name__ == "__main__":
    target_host = input("Digite o host a ser escaneado (ex: google.com, 192.168.1.1): ")
    if not target_host:
        print("Nenhum host fornecido. Saindo.")
    else:
        try:
            results = scan_common_ports(target_host)
            save_json = input("Exportar resultados para 'scan_results.json'? (s/n, padrão: s): ").lower() != 'n'
            if save_json:
                export_to_json(results)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
