import os.path
import sys

#check for ip_file path
def ip_file_valid():
    ip_file = input("\n Give path to the ip file: ")
    if os.path.isfile(ip_file) == True:
        print("\nIP path is valid!\n")
    else:
        print("IP path is not valid ".format(ip_file))
        sys.exit()
    selectet_ip_f = open(ip_file, 'r')
    selectet_ip_f.seek(0)
    ip_list = selectet_ip_f.readlines()
    selectet_ip_f.close()
    return ip_list
