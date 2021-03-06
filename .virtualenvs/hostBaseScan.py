#returns (in the same order listed here): fileScanned, dirScanned, filesInfected, userDir
#userDir is the user's entered directory for scanning, use this information to access the clamAVresults.txt like this: {userDir}/clamAVresults.txt

import subprocess, sys, re, os

def hostBaseScan(userDir):
    print("running hostbase scan")
    #userDir = "C:\\Users\\Jessi\Desktop\\ScanTest" #example directory for testing purposes
    filePath = f"{userDir}\\hostbaseScanResults.txt"
    command = f'cmd /c "cd %ProgramFiles%\Windows Defender & .\MpCmdRun.exe -Scan -ScanType 3 -File {userDir} > {filePath}"'
    os.system(command)
    result = []
    with open (filePath, "r") as r:
        while True:
            line = r.readline()
            if not line: break
            result += re.findall(r'found (.*) threats', line)
    print("finished scan")
    filesInfected = result[0]
    return filesInfected, userDir, filePath