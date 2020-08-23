# -*- coding: iso-8859-1 -*-
import subprocess, sys

p = subprocess.Popen(["powershell.exe", 
               "cd C:/Users/Jessi/Downloads/clamav-0.102.1-win-x64-portable;.\clamscan"], 
              stdout=sys.stdout)
p.communicate()

'''
import os, re

print("running hostbase scan")
#this command works for jeff's machine, which is Windows. Need to test if it works for other windows machine too
WinCommand = "cd C:\Users\Jessi\Downloads\clamav-0.102.1-win-x64-portable"
WinCommand2 = ".\clamscan > portscandata.txt"

#change which command variable to run depending on which OS you are using
os.system(WinCommand)
os.system(WinCommand2)

print("finished scan")
'''