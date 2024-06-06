import socket
from IPy import IP

def check_ip(ipaddress):
    try:
        IP(ipaddress)
        return ipaddress
    except:
        return socket.gethostbyname(ipaddress)
    

def get_banner(socket):
    return socket.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print(f"Port {port} is open on target {ipaddress} : {str(banner.decode())}")
        except:
            print(f"Port {port} is open on target {ipaddress}")
    except:
        pass

ipaddress = input("Enter ip address: ")
converted_ip = check_ip(ipaddress)

for port in range(1, 100):
    scan_port(converted_ip, port)