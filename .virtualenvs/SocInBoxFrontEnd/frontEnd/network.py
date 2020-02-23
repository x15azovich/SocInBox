import os

class myNetwork:
    def callPrint(myArgs):
        print(myArgs)
    def outDirCall():
        for name in os.listdir("C:\\Users\\Smith Gaddy\\Desktop\\"):
            if name.endswith(".txt"):
                print(name)