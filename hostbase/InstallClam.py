#!/usr/bin/python
import os

def operatingSystem(OS, path):
	if OS=="Windows":
		path = "~/SocInBox/hostbase/windows7"
		execute(path)
	if OS=="mac":
                path = "~/SocInBox/hostbase/mac"
                execute(path)
	if OS=="Linux":
                path = "~/SocInBox/hostbase/Linux"
                execute(path)


		
def execute(path):
	execute = path + "ClamAV-0.102.1.exe"
	os.system(execute)
	print("Seccessfully executed " + execute)
	

def main():
	operating=input("Enter your operating system : ")
	print ("main ran" + operating)
	path= "~/SocInBox/hostbase/Linux"
	operatingSystem(operating, path)
if __name__ == "__main__":
	main()
