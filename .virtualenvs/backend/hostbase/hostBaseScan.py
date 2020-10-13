import subprocess, sys, re, os
scannedDir = 0
scannedFiles = 0
InfectedFiles = 0

#def hostBaseScan(dir):
print("running hostbase scan")
#this command works for jeff's machine, which is Windows. Need to test if it works for other windows machine too
#WinCommand = "cd C:\Users\Jessi\Downloads\clamav-0.102.1-win-x64-portable"
#WinCommand2 = ".\clamscan > portscandata.txt"
#change which command variable to run depending on which OS you are using
dir = "C:\ClamAVSupport"
command = f'cmd /c "cd {dir} & .\clamscan > C:\\Users\\Jessi\\SocInBox\\.virtualenvs\\backend\\hostbase\\clamAVresults.txt"'
os.system('cmd /c ')
#os.system('cmd /c ".\clamscan > portscandata.txt"')
#change path to reflect user's instead of hardcoding it

with open ("clamAVresults.txt", "r") as r:
    while True:
        line = r.readline()
        if not line: break
        scannedDir = re.findall(r'Scanned files: (\d{1,})', r.readline()) 
print(scannedDir)


print("finished scan")
