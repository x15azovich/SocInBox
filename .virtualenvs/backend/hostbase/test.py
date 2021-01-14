import hostBaseScan
userDir = "C:\\Users\\jeffr\\Desktop\\SocInBox"
print("scan result: " + hostBaseScan.scan(userDir))
print("all quarantined files: " + hostBaseScan.listQuarantine(userDir))
print("all past detections: " + hostBaseScan.getPastDetections(userDir))
print("restore: ")
hostBaseScan.restore("ndfn")