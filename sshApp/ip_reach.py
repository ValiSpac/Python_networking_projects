import sys
import subprocess

def ip_reach(list):
    for ip in list:
        ip = ip.rstrip("\n")
        ping_reply = subprocess.call('ping %s -c 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

        if ping_reply == 0:
            print(f"\n {ip} is reacheacble\n")
            continue
        else:
            print(f"\n {ip} is not reacheacble(Cheack conectivity and try again)\n")
            sys.exit()
