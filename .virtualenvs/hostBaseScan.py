#returns (in the same order listed here): fileScanned, dirScanned, filesInfected, userDir
#userDir is the user's entered directory for scanning, use this information to access the clamAVresults.txt like this: {userDir}/clamAVresults.txt

import subprocess, sys, re, os
scannedDir = 0
scannedFiles = 0
InfectedFiles = 0

def hostBaseScan(userDir):
    print("running hostbase scan")

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

    with open (filePath, "r") as r:
        while True:
            line = r.readline()
            if not line: break
            scannedfiles += re.findall(r'Scanned files: (\d{0,})', line)
            scannedDir += re.findall(r'Scanned directories: (\d{0,})', line)
            infected += re.findall(r'Infected files: (\d{0,})', line)

    fileScanned = scannedfiles[0]
    dirScanned = scannedDir[0]
    filesInfected = infected[0]

    print(fileScanned)
    print(dirScanned)
    print(filesInfected)


    print("finished scan")
    return fileScanned, dirScanned, filesInfected, userDir, filePath
