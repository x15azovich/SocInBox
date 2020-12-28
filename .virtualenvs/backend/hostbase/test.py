import hostBaseScan
userDir = "C:\\Users\\Anthony\\Documents\\Jessi"
print("scan result: " + hostBaseScan.scan(userDir))
print("all quarantined files: " + hostBaseScan.listQuarantine(userDir))
print("all past detections: " + hostBaseScan.getPastDetections(userDir))
print("restore: ")
hostBaseScan.restore("ndfn")