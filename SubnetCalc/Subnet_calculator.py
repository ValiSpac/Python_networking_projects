import random
import sys

def subnet_calc():
#Checking for ip address
    while True:
        ip_address = input("Enter and IP address: ")
        ip_octets = ip_address.split('.')
        if (len(ip_octets) == 4 and (1 <= int(ip_octets[0]) <= 253) and
            (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169) and
            int(ip_octets[1]) != 254 and (0 <= int(ip_octets[1]) <= 255)
            and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3])
            <= 255):
            break
        else:
            print(f"The ip address is invalid {ip_address}\n")
            continue

#Checking for subnet mask
    masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
    while True:
        mask = input("Enter the subnet mask: ")
        mask_octets = mask.split('.')
        if ((len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and
            (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks)
            and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >=
            int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3]))):
            break
        else:
            print(f"The subnet mask is invalid {mask}\n")
            continue

    #Format the mask binary
    mask_octet_binary = []
    for octet in mask_octets:
        binary_octet = bin(int(octet)).lstrip('0b')
        mask_octet_binary.append(binary_octet.zfill(8))
    binary_mask = "".join(mask_octet_binary)
    #Count the numbers of 1 and 0 in the mask bin
    no_of_zeros = binary_mask.count('0')
    no_of_ones = 32 - no_of_zeros
    #Formula for getting the number of hosts/subnet
    #abs() because in the case of the /32 mask the no_of_zero = 0
    no_of_hosts = abs(2 ** no_of_zeros - 2)

    #Get wildcard mask from octets
    wildcard_octets = []
    for octet in mask_octets:
        wild_octet = 255 - int(octet)
        wildcard_octets.append(str(wild_octet))

    wildcard_mask = '.'.join(wildcard_octets)
    #print(wildcard_mask)

    #Extract each octet in the ip and put it into a string
    ip_octets_binary = []
    for octet in ip_octets:
        binary_octet = bin(int(octet)).lstrip('0b')
        ip_octets_binary.append(binary_octet.zfill(8))

    binary_ip = "".join(ip_octets_binary)
    #print(binary_ip)

    network_address_bin = binary_ip[:(no_of_ones )] + '0' * no_of_zeros
    brodcasat_addres_bin = binary_ip[:(no_of_ones)] + '1' * no_of_zeros

    #Get each octet from the network binary
    net_ip_octets = []
    for binn in range(0, 32, 8):
        net_ip_octet = network_address_bin[binn : binn + 8]
        net_ip_octets.append(net_ip_octet)

    #Transform from binary to int the network address and join it to a string
    net_ip_addresss = []
    for each_octet in net_ip_octets:
        net_ip_addresss.append(str(int(each_octet, 2)))

    network_address = ".".join(net_ip_addresss)

    #Get each octet from the brodcast address binary
    bst_ip_octets = []
    for binn in range(0, 32, 8):
        bst_ip_octet = brodcasat_addres_bin[binn : binn + 8]
        bst_ip_octets.append(bst_ip_octet)

    #Transform from binary to int the brodcast address and join it to a string
    bst_ip_address = []
    for each_octet in bst_ip_octets:
        bst_ip_address.append(str(int(each_octet, 2)))

    broadcast_address = ".".join(bst_ip_address)
    
    print("\n")
    print("Network address is: %s" % network_address)
    print("Broadcast address is: %s" % broadcast_address)
    print("Number of valid hosts per subnet: %s" % no_of_hosts)
    print("Wildcard mask: %s" % wildcard_mask)
    print("Mask bits: %s" % no_of_ones)
    print("\n")
    
subnet_calc()
