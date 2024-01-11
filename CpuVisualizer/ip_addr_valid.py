import sys

def ip_addr_valid(iplist):
    for ip in iplist:
        ip = ip.rstrip("\n")
        octet_list = ip.split('.')
        #just checking if the ip address is valid
        if (len(octet_list) == 4 and (1 <= int(octet_list[0]) <= 253) and
            (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169) and
            int(octet_list[1]) != 254 and (0 <= int(octet_list[1]) <= 255)
            and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3])
            <= 255):
            print(ip)
            continue
        else:
            print(f"There is an invalid ip address in the file: {ip}\n")
            sys.exit()
