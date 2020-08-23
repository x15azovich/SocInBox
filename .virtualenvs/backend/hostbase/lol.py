import subprocess, sys

p = subprocess.Popen(["powershell.exe", 
               "cd C:/Users/Jessi/Downloads/clamav-0.102.1-win-x64-portable;.\clamscan > C:/Users/Jessi/SocInBox/.virtualenvs/backend/hostbase/clamAVresults.txt"], 
              stdout=sys.stdout)
p.communicate()