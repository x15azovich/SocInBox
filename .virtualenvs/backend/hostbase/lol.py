import subprocess, sys, re
scannedDir = 0
scannedFiles = 0
InfectedFiles = 0

#change path to reflect user's instead of hardcoding it
p = subprocess.Popen(["powershell.exe", 
               "cd C:\ClamAVSupport;.\clamscan > C:/Users/Jessi/SocInBox/.virtualenvs/backend/hostbase/clamAVresults.txt"], 
              stdout=sys.stdout)
p.communicate()

with open ("clamAVresults.txt", "r") as r:
    while True:
        line = r.readline()
        if not line: break
        scannedDir = re.findall(r'Scanned files: (\d{1,})', r.readline()) 
print(scannedDir)


