import os, re

class nmapVulScanner:

    def __init__(self, ip):
        self.ip = ip
 #   host = input("ip:")
    def scan(self):
        command = "nmap --script nmap-vulners -sV "+str(self.ip)+" > portscandata.txt"
        os.system(command)

        pattern = "https://(.*?)\|"

        with open("portscandata.txt", "r") as file:
            for line in file:
                substring = re.search(pattern, line)[0]
                print(substring)
        