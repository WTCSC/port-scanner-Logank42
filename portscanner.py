import sys
import time
import subprocess
import platform
import socket
import ipaddress


port = sys.argv[1] # First input
pnumber = sys.argv[2] # Second input
ip_add = sys.argv[3] # Third input


def main():
    if port == "-p":
        try:
            network = ipaddress.ip_network(ip_add, strict=False) # Converts into a IPv4 network

            for ip in network.hosts(): # For each ip, it will go through the check function
                input_check(ip, pnumber)

        except ValueError as e: # If the ip address isn't correctly formated, prints error message
            print(f"Invalid format: {e}")
            sys.exit(1)
    
    else: # Error message
        print("Error: -p argument required")


def input_check(ip, pnumber):
    input = sys.argv[2] # Takes port/s
    if "-" in input:
        start, end = map(int, input.split('-')) # Splits the range Ex: (1-100) 1 and 100 by the -
        pnumber = list(range(start, end + 1)) # Creates a list from given numbers Ex: 1-100 1, 2, 3, 4...
        scanning(ip, pnumber)

    else:
        pnumber = input.split(",") # Splits by commas
        scanning(ip, pnumber)
    return pnumber


def scanning(ip, pnumber):
    flag = "-n" if platform.system().lower() == "windows" else "-c" # Checks os
    pinging = ['ping', flag, '1', str(ip)] # Pinging commands, making the subprocess easier to read
    try:
        start_time = time.time() # Starts timer
        final = subprocess.run(pinging, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=.75) # Ping command, stops errors from being printed and times out if the ping takes longer than 5 seconds
        end_time = time.time() # Ends timer
        total_time = (end_time - start_time) * 1000 # Converts to ms

        if final.returncode == 0:
            print(f"{ip} - UP ({total_time:.2f}ms)") # Prints ip number, status and time
            port_check(ip, pnumber)

    except subprocess.TimeoutExpired:
        print (f"{ip} - TIMEOUT") # Timeout message


def port_check(ip, pnumber):
    for x in pnumber:
        portnumber = int(x) # Makes numbers into int
        ips = str(ip) # Makes numbers into string
        port = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Checks port
        port.settimeout(.1) # Timeout after 0.1 seconds
        result = port.connect_ex((ips, portnumber)) # Return code
        port.close()

        if result == 0:
            print(f"    Port {portnumber} - OPEN") # Prints if port is open

if __name__ == "__main__":
    # Printing messages, formating
    print(f"Scanning network {ip_add}, port(s) {pnumber}")
    time.sleep(1)
    print("...")
    time.sleep(1)
    main()
    print("...")
    time.sleep(1)
    print("Scan complete.")