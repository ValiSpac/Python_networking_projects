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

    try:
        for ip in ip_list:
            with open(f"{ip}_cpu", "w") as f:
                pass
        while True:
            create_threads(ip_list, ssh_connection)
            if (cycle == 0):
                cycle = 1
                # creating a thread for the graph so it can update live
                graph_thread = threading.Thread(target=show_graph, args=(ip_list,))
                # seting the thread as a daemon so it can be automatically terminated when the main thread exits
                #!!!!this method doesn't allow for proper cleanup as it abruptly stops the thread
                graph_thread.daemon = True
                graph_thread.start()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nProgram aborted by user!\n")
        sys.exit()

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

    # start the main program in a separate thread
    main_thread = threading.Thread(target=main_program, args=(ip_list,))
    main_thread.daemon = True
    main_thread.start()

    try:
        # main_thread can continue with other tasks or just wait
        main_thread.join()
    except KeyboardInterrupt:
        print("\nProgram aborted by user!\n")
        sys.exit()
