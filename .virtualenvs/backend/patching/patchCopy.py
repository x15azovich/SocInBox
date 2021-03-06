import re, os

myDirectory = os.path.expanduser("~/SocInBox/scanning/portscandata.txt")
f = open(myDirectory, "r")

while True:
	#reading each line of the file
	line = f.readline()
	line = line.replace("\\r", "").replace("\\n", "").replace("220","")
	#break if no more line
	if not line: break

	#using regex to grab port number and banner 	
	x = re.findall(r'([\d]+): b[\'\"](.*)[\'\"]', line)[0]
	port = x[0]
	banner = x[1]
	strippedBanner = re.sub('[(){}\[\]\\\<> :#\-,*_]', '', banner)
	print (port + ": " + strippedBanner)
