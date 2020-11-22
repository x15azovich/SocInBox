#returns (in the same order listed here): fileScanned, dirScanned, filesInfected, userDir
#userDir is the user's entered directory for scanning, use this information to access the clamAVresults.txt like this: {userDir}/clamAVresults.txt

import subprocess, sys, re, os

def hostBaseScan(userDir):
    print("running hostbase scan")
<<<<<<< HEAD:.virtualenvs/backend/hostbase/hostBaseScan.py
    #userDir = "C:\\Users\\Jessi\Desktop\\ScanTest" #example directory for testing purposes
    filePath = f"{userDir}\\hostbaseScanResults.txt"
    command = f'cmd /c "cd %ProgramFiles%\Windows Defender & .\MpCmdRun.exe -Scan -ScanType 3 -File {userDir} > {filePath}"'
    os.system(command)
    result = []
=======

    #this command works for jeff's machine, which is Windows. Need to test if it works for other windows machine too
    print(userDir)
    userDir = userDir.replace("/","\\")
    
    #userDir = "C:\ClamAVSupport" #example directory for testing purposes
    command = f'cmd /c "D:\Jeff\ClamAV\clamscan.exe --recursive {userDir} > D:\Jeff\ClamAV\clamAVresults.txt"' 
    #command = f'cmd /c "cd {userDir} & D:\Jeff\ClamAV\clamscan.exe > D:\Jeff\ClamAV\clamAVresults.txt"' 
    os.system(command)

    scannedfiles = []
    scannedDir = []
    infected = []

    filePath = "D:\Jeff\ClamAV\clamAVresults.txt"

>>>>>>> 142ba62860bd542ff84f15764d66d22cc168b8c6:.virtualenvs/hostBaseScan.py
    with open (filePath, "r") as r:
        while True:
            line = r.readline()
            if not line: break
            result += re.findall(r'found (.*) threats', line)
    print("finished scan")
    return "Found " + result[0] + " threat(s)"
