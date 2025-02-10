[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18031290)
# IP port scanner
This is a simple port scanner. When you input the IP and the ports you want to check, you will get an output of either open or no response. If it says open, then the port is open, and if theres no response, the port is closed. You can do a single port, a couple of ports with a comma inbetween (setup like this: 20,80) or a range (1-100). This can scan either one IP or multipul using CIDR notation
## Setup:
Before you can do anything, you need to know the IP address and the ports you want to scan. To run the scanner, you need to type `python3 portscanner.py -p [Port(s)] [IP address]`. Once you enter the command, you will see it printed in this format:

    Scanning network 164.90.247.135/30, port(s) 1-81
    ...
    164.90.247.133 - UP (44.34ms)
        Port 22 - OPEN
        Port 80 - OPEN
    164.90.247.134 - TIMEOUT
    ...
    Scan complete.