import re, os

myDirectory = os.path.expanduser("~/SocInBox/scanning/portscandata.txt")
f = open(myDirectory, "r")

while True:
	#reading each line of the file
	line = f.readline()

	#break if no more line
	if not line: break

	#using regex to grab port number and banner 	
	x = re.findall(r'([\d]+): b[\'\"](.*)[\'\"]', line)[0]
	print (x[0] + " " + x[1])
