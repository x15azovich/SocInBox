#!/usr/bin/python
import os

def operatingSystem(OS, path):
	if OS=="Windows":
		path = "~/SocInBox/hostbase/windows7/ClaimAV-0.1.2.1.exe"
		executeWindows(path)
	if OS=="mac":
                path = "~/SocInBox/hostbase/mac/clamav-0.102.2.tar.gz"
                executeLinux(path)
	if OS=="Linux":
                path = "~/SocInBox/hostbase/Linux/clamav-0.102.2.tar.gz"
                executeLinux(path)


		
def executeLinux(path):
#system commands to unpack and install on linux/mac
	execute = path
	os.system(execute)
	
def executeWindows(path):
	execute = path
	os.system(execute)
	
def main():
	operating=input("Enter your operating system : ")
	print ("main ran" + operating)
	path= "~/SocInBox/hostbase/Linux"
	operatingSystem(operating, path)
if __name__ == "__main__":
	main()
