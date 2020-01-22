f = open("/root/SocInBox/scanning/portscandata.txt", "r")

while True:
	x = f.readline()
	if not x: break
	print (x)
