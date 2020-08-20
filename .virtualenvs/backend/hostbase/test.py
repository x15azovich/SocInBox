# -*- coding: iso-8859-1 -*-
import subprocess, sys

p = subprocess.Popen(["powershell.exe", 
               "cd C:\Users\Jessi\Downloads\clamav-0.102.1-win-x64-portable;.\clamscan"], 
              stdout=sys.stdout)
p.communicate()