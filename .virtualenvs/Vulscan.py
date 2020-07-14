import os, re

def scan(ip):
    print("running scan")
    #this command works for jeff's machine, which is Windows. Need to test if it works for other windows machine too
    WinCommand = "nmap -sV --script=vulscan/vulscan.nse "+str(ip)+" > portscandata.txt"
    
    #this command works for Jessica's kali, also need to test for compatibility
    KaliCommand = "nmap --script nmap-vulners -sV "+str(ip)+" > portscandata.txt"
    
    #change which command variable to run depending on which OS you are using
    os.system(WinCommand)
    
    print("finished scan")
