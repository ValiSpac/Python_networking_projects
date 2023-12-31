from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads
import sys
import time
import os

ip_list = ip_file_valid()

# if os.path.exists ("/cpu.txt"):
#     cpu_information = open("cpu.txt", 'w')
#     cpu_information.close()
try:
    ip_addr_valid(ip_list)
except KeyboardInterrupt:
    print("\nProgram aborted by user!\n")
    sys.exit()

try:
    ip_reach(ip_list)
except KeyboardInterrupt:
    print("\nProgram aborted by user!\n")
    sys.exit()

#In here we create threads for each ip that will create the simultaneous ssh connection
while True:
    create_threads(ip_list, ssh_connection)
    time.sleep(5)
