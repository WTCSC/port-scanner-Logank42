import sys
import time
import subprocess
import platform
import socket
import ipaddress


def scanner(ip, pnumber):
    input = sys.argv[2]
    if "-" in input:
        pass

    else:
        pnumber = input.split(",")
        flag = "-n" if platform.system().lower() == "windows" else "-c" # Checks os
        pinging = ['ping', flag, '1', str(ip)] # Pinging commands, making the subprocess easier to read

        try:
            start_time = time.time() # Starts timer
            final = subprocess.run(pinging, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5) # Ping command, stops errors from being printed and times out if the ping takes longer than 5 seconds
            end_time = time.time() # Ends timer
            total_time = (end_time - start_time) * 1000 # Converts to ms

            if final.returncode == 0:
                print(f"{ip} - UP ({total_time:.2f}ms)")
                port_check(ip, pnumber)

        except subprocess.TimeoutExpired:
            pass

def port_check(ip, pnumber):
    for x in pnumber:
                portnumber = int(x)
                ips = str(ip)
                port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                port.settimeout(2)
                result = port.connect_ex((ips, portnumber))
                port.close()

                if result == 0:
                    print(f"    Port {portnumber} - OPEN")
                    
                else:
                    return False

def main():
    port = sys.argv[1]
    pnumber = sys.argv[2]
    ip_add = sys.argv[3]

    try:
        network = ipaddress.ip_network(ip_add, strict=False) # Converts into a IPv4 network

        for ip in network.hosts(): # For each ip, it will go through the scanner function
            scanner(ip, pnumber)

    except ValueError as e: # If the ip address isn't correctly formated, prints error message
        print(f"Invalid format: {e}")
        sys.exit(1)


if __name__ == "__main__":
    port = sys.argv[1]
    pnumber = sys.argv[2]
    ip_add = sys.argv[3]
    print(f"Scanning network {ip_add}, port(s) {pnumber}")
    print("...")
    main()
    print("...")
    print("Scan complete.")