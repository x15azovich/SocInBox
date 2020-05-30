import os, re

def scan(ip):
    command = "nmap --script nmap-vulners -sV "+str(ip)+" > portscandata.txt"
    os.system(command)

    pattern = "https://(.*?)\|"

    with open("portscandata.txt", "r") as file:
        for line in file:
            substring = re.search(pattern, line)[0]
            print(substring)
        