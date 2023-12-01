import paramiko
import os.path
import time
import sys
import re

user_file = input("\n Enter the user file path: ")
if os.path.isfile(user_file) == True:
    print("\nUser path valid!\n")
else:
    print("\nUser path is not valid!\n")
    sys.exit()

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
        selected_user_file = open(user_file, 'r')
        selected_user_file.seek(0)
        username = selected_user_file.readline().split(',')[0].rstrip('\n')
        selected_user_file.seek(0)
        password = selected_user_file.readline().split(',')[1].rstrip('\n')

        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip('\n'), username=username, password=password)
        connection = session.invoke_shell()

        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)
        for each_line in selected_cmd_file:
            connection.send(each_line + '\n')
            time.sleep(1)
        selected_cmd_file.close()
        selected_user_file.close()

        router_output = connection.recv(65535)
        if re.search(b'% Invalid input', router_output):
            print(f"There was at least one IOS syntax error for {ip}, check the command line file")
        else:
            print(f"Done for device[]: {ip}")
        output_strings = re.split(r'\r\n|\r\r|\n|\r', router_output.decode())
        for line in output_strings:
            print(line)
        session.close()

    except paramiko.AuthenticationException:
        print("Invalid username or password!(Please check the username and password for the device configuration)")
        sys.exit()
