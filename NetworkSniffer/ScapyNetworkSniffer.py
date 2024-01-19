from datetime import datetime
import subprocess
import sys

try:
    from scapy.all import *
    from scapy.all import conf
except ImportError:
    print("Scapy is not installed on your system($:python3 pip install scapy)")
    sys.exit()



if __name__ == "__main__":
    net_iface = input("Please enter the interface on wich to run the sniffer(ex. 'enp0s8'): ")

#   PRMOISC mode is a mode for a wired NIC (network interface controer) or WNIC (wireless NIC) that causes the controler to pass all the trafic
#through the CPU rather then passing only the frames that the controler is intended to receive

    try:
        result = subprocess.call(["ifconfig"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=False)
        if result != 0:
            print(f"Failed to configure interface {net_iface} as promiscuous. The command exited with code {result}\n")
            sys.exit()
        else:
            print(f"Interface {net_iface} was set to PROMISC mode.\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")
        sys.exit()

    #packets to sniff
    while True:
        pkt_to_sniff = input("Enter the number of packets to capture (0 for no limit): ")
        try:
            pkt_to_sniff = int(pkt_to_sniff)
            if pkt_to_sniff >= 0:
                break
            else:
                print("Enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Enter a valid integer.")
    if pkt_to_sniff != 0:
        print(f"The program will capture {pkt_to_sniff} packets.\n")
    else:
        print("The program will capture packets until the timeout expires.\n")

    #time_to_sniff
    while True:
        try:
            time_to_sniff = input("Enter the number of second to run the capture: ")
            if int(time_to_sniff) > 0:
                print(f"The capture will run for {time_to_sniff} seconds.\n")
                break
            else:
                print(f"Enter a non-negative integer.")
        except ValueError as e:
            print("Invalid input. Enter a valid integer.")

    try:
        available_l3_protocols = set(conf.l3types)
    except KeyError:
        available_l3_protocols = set()

    #protocol filter
    while True:
        protocol_filter = input("Enter the protocol filter for the packets that you want to capture (0 for all):")
        if protocol_filter != "" and protocol_filter != '0':
            print(f"Searching for packets with the {protocol_filter} protocol filter.\n")
            break
        elif protocol_filter == '0':
            print(f"Searching for all protocols.\n")
            break
        else:
            print("Enter a protocol!\n")

    #log file
    while True:
        file_name = input("Give a name to the log file: ")
        if file_name:
            sniffer_log = open(file_name, "a")
            break

    #function wich will print the data in the log file
    def packet_log(packet):
        global packet_count
        now = datetime.now()
        print(f"\n{now}: Packet number {packet_count}\n")

    print("\nStarting the capture.....\n")
    packet_count = 0
    try:
        if protocol_filter == '0':
            sniff(iface = net_iface, count = int(pkt_to_sniff), timeout = int(time_to_sniff). prn = packet_log)
        elif:
            sniff(iface = net_iface, filter = protocol_filter, count = int(pkt_to_sniff), timeout = int(time_to_sniff). prn = packet_log)
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")
        sys.exit()
    print("\nFINISHED!\nBYE!")

