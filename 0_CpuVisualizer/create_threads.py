import threading

def create_threads(list, function):
    threads = []
    #initialize threads and set the ssh_connection function as the target
    for ip in list:
        th = threading.Thread(target=function, args=(ip,))
        th.start()
        threads.append(th)
    #join the threads so they can run at the same time
    for th in threads:
        th.join()
