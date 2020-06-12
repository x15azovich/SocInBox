import os, re

ip="192.168.1.153"
def scan(ip):
    print("running scan")
    command = "nmap -sV --script=vulscan/vulscan.nse "+str(ip)+" > portscandata2.txt"
    os.system(command)
    print("finished scan")
    pattern = "https://(.*?)\|"

    with open("portscandata2.txt", "r") as file:
        print("getting regex")
        for line in file:
            print("substring:")
            substring = re.search(pattern, line)[0]
            print(substring)