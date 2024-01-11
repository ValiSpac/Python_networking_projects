from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads
from graph import show_graph
import sys
import time
import threading

def main_program(ip_list):
    cycle = 0
    #in here we create threads for each ip that will create the simultaneous ssh connection
    while True:
        create_threads(ip_list, ssh_connection)
        time.sleep(5)
        if (cycle == 0):
            cycle = 1
            #creating a thread for the graph so it can update live
            #!!!very unstable to run a matplotlib giu outside of main thread!!!!
            graph_thread = threading.Thread(target=show_graph, args=(ip_list,))
            graph_thread.start()

if __name__ == "__main__":
    ip_list = ip_file_valid()

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

    main_thread = threading.Thread(target=main_program, args=(ip_list,))
    main_thread.start()
    main_thread.join()
