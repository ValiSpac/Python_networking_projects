import paramiko
import os.path
import time
import sys
import re

#check for the user file path
user_file = input("\n Enter the user file path: ")
if os.path.isfile(user_file) == True:
    print("\nUser path valid!\n")
else:
    print("\nUser path is not valid!\n")
    sys.exit()

#check for the command line file path
cmd_file = input("\n Enter the command line file path: ")
if os.path.isfile(cmd_file) == True:
    print("\nCommand line file path valid!\n")
else:
    print("\Command line file path is not valid!\n")
    sys.exit()

def ssh_connection(ip):
    global user_file
    global cmd_file
    try:
        #open the user_file and get the username and password
        selected_user_file = open(user_file, 'r')
        selected_user_file.seek(0)
        username = selected_user_file.readline().split(',')[0].rstrip('\n')
        selected_user_file.seek(0)
        password = selected_user_file.readline().split(',')[1].rstrip('\n')

        #initialize the ssh connection
        session = paramiko.SSHClient()
        #for testing purposes, this allows auto-accepting unknown host keys
        #do not use in production! The default would be rejectpolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #establish the ssh connection using the ssh param
        session.connect(ip.rstrip('\n'), username=username, password=password)
        #start an interactive shell in the router
        connection = session.invoke_shell()

        #open the command line file to get all the commands
        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)
        #for each command line we will send it to the shell in the router
        for each_line in selected_cmd_file:
            connection.send(each_line + '\n')
            time.sleep(1)

        selected_cmd_file.close()
        selected_user_file.close()

        #checking command output for ios syntax errors
        router_output = connection.recv(65535)
        if re.search(b'% Invalid input', router_output):
            print(f"There was at least one IOS syntax error for {ip}, check the command line file")
        else:
            print(f"Done for device[]: {ip}\n")
        #searching for the cpu pattern after running the command "show processes top once"
        cpu = re.search(b"%Cpu\(s\):(\s)+(.+?)(\s)* us,", router_output)
        #extracting the second group from our cpu utilization output and decoding the byte output in utf-8 format
        utilization = cpu.group(2).decode("utf-8")
        #open and append the cpu utilization in a target file
        with open(f"{ip}_cpu", "a") as f:
            f.write(utilization + "\n")
        #close session so you don't create new connection for every thread
        session.close()

    except paramiko.AuthenticationException:
        print("Invalid username or password!(Please check the username and password for the device configuration)")
        sys.exit()
