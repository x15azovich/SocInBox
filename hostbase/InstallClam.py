#!/usr/bin/python
import os

def operatingSystem(operatingSystem, path):
	if operatingSystem=="Windows 7":
		path = "~/SocInBox/hostbase/windows7"
		execute(path)
		
def execute(path):
	execute = path + "ClamAV-0.102.1.exe"
	os.system(execute)
	print("Seccessfully executed " + execute)
	

def main():
	operating=input("Enter your operating system : ")
	print ("main ran" + operating)
	path= "~/SocInBox/hostbase/Linux"
	operaingSystem(operating, path)
if __name__ == "__main__":
	main()
