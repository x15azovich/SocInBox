import re
#pattern = re.compile("Scanned files: (\d{0,})")
def scanResultGetter():
    scannedfiles = []
    scannedDir = []
    infected = []
    with open ("clamAVresults.txt", "r") as r:
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

    return fileScanned, dirScanned, filesInfected
