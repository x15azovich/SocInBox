import subprocess, sys, re, os

#takes in userDir, which is the desired folder path to be scanned
#returns scan and cleanning result if applicable
def scan(userDir):
    print("running hostbase scan")
    #userDir = "C:\\Users\\Jessi\Desktop\\ScanTest" #example directory for testing purposes
    filePath = f"{userDir}\\hostbaseScanResults"
    command = f'cmd /c "cd %ProgramFiles%\Windows Defender & .\MpCmdRun.exe -Scan -ScanType 3 -File {userDir} > {filePath + ".txt"}"'
    os.system(command)
    result = []
    with open (filePath + ".txt", "r") as r:
        while True:
            line = r.readline()
            if not line: break
            result += re.findall(r'found (.*) threats', line)
    print("finished scan")
    return "Found " + result[0] + " threat(s)"

#takes in OutputfilePath, which is the desired path to store the quarantined file path results, which will be a file called quarantinedFiles.txt
#returns quarantined file names in string format
def listQuarantine(OutputfilePath):
    #command to list all quarantined file
    command2 = f'cmd /c "cd %ProgramFiles%\Windows Defender & .\MpCmdRun.exe -Restore -ListAll > {OutputfilePath + "quarantinedFiles.txt"}"'
    print(os.system(command2))
    
    result = ""
    with open (OutputfilePath + "quarantinedFiles.txt", "r") as r:
        while True:
            line = r.readline()
            if not line: break
            result += line
    return result
#takes in OutputfilePath, which is the desired path to store the past detection results, in a file called pastDetections.txt
#returns all detected file paths (include ones that has been deleted as well) in a csv formatted string
def getPastDetections(OutputfilePath):
    subprocess.call(f'%SystemRoot%/system32/WindowsPowerShell/v1.0/powershell.exe Get-MpThreatDetection > {OutputfilePath + "pastDetections.txt"}', shell=True)
    result = ""
    pattern = re.compile(r'file:_(.*)[,|}][\n| ]')
    with open (OutputfilePath + "pastDetections.txt", "r") as r:
        while True:
            line = r.readline()
            if not line: break
            mo = pattern.search(line)
            if mo is not None:
                result += (mo.group(1)) + ", "
    return result