import os, re

ip="192.168.1.153"
def scan(ip):
    command = "nmap -sV --script=vulscan/vulscan.nse "+str(ip)+" > portscandata2.txt"
    os.system(command)

    pattern = "https://(.*?)\|"

    with open("portscandata2.txt", "r") as file:
        for line in file:
            substring = re.search(pattern, line)[0]
            print(substring)