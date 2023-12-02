import random
import sys

def subnet_calc():
#Checking for ip address
    while True:
        ip_address = input("Enter and IP address: ")
        octet_list = ip_address.split('.')
        if (len(octet_list) == 4 and (1 <= int(octet_list[0]) <= 253) and
            (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169) and
            int(octet_list[1]) != 254 and (0 <= int(octet_list[1]) <= 255)
            and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3])
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
    for octet in mask_octests:
        binary_octet = bin(int(octet)).lstrip('0b')
        mask_octet_binary.append(binary_octet.zfill(8))
    binary_mask = "".join(mask_octet_binary)
    #Count the numbers of 1 and 0 in the mask bin
    no_of_zeros = binary_mask.count('0')
    no_of_ones = 32 - no_of_zeros
    #Formula for getting the number of hosts/subnet
    #abs() because in the case of the /32 mask the no_of_zero = 0
    no_of_hosts = abs(2 ** no_of_zeros - 2)
    print(f"host = {no_of_hosts}")

    wildcard_octets = []
    for octet in mask_octests:
        wild_octet = 255 - int(octet)
        wildcard_octets.append(str(wild_octet))

    wildcard_mask = '.'.join(wildcard_octets)
    print(wildcard_mask)

