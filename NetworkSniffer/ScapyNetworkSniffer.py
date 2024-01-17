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
    net_iface = input("Please enter the interface on wich to run the sniffer(ex. 'enp0s8') : ")

#   PRMOISC mode is a mode for a wired NIC (network interface controer) or WNIC (wireless NIC) that causes the controler to pass all the trafic
#through the CPU rather then passing only the frames that the controler is intended to receive

    try:
        subprocess.call(["ifconfig", net_iface, "promisc"], stdout=False, stderr=False, shell=False)
    except:
        print("Failed to configure interface as promiscous.\n")
    else:
        print(f"Interface {net_iface} was set to PROMISC mode.\n")

    pkt_to_sniff = input("Enter the number of packets to capture(0 no limit)")

    if int(pkt_to_sniff) != 0:
        print(f"The program will capture {pkt_to_sniff} packets.\n")

    elif int(pkt_to_sniff) == 0:
        print("The program will capture packets until the timeout expires.\n")

    time_to_sniff = input("Enter the number of second to run the capture : ")

    if int(time_to_sniff) != 0:
        print(f"The capture will run for {time_to_sniff} seconds.\n")

    protocol_filter = input("Enter the protocol filter for the packets that you want to capture:")
