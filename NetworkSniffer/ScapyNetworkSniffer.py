import logging
from datetime import datetime
import subprocess
import sys

try:
    from scapy.all import *
except ImportError:
    print("Scapy is not installed on your system($:python3 pip install scapy)")
    sys.exit()

if __name__ == "__main__":
    net_iface = input("Please enter the interface on wich to run the sniffer(ex. 'enp0s8'):")

    try:
        subprocess.call(["ifconfig", net_iface, "promisc"], stdout=False, stderr=False, shell=False)
    except:
        print("Failed to configure interface as promiscous.\n")
    else:
        print(f"Interface {net_iface} was set to PROMISC mode.\n")
