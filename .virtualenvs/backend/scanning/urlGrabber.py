import re, os
#CHANGE FILE PATH TO NOT HARD CODING 
#myDirectory = os.path.expanduser("~/SocInBox/.virtualenvs/backend/scanning/portscandata.txt")
#f = open(myDirectory, "r")
f = open("portscandata.txt", "r")
w = open("CVEurls.txt", "w")
x = []
while True:
    line = f.readline()
    if not line: break
    
    x += re.findall(r'https:\/\/(.*)', line)
      
for i in x:
    w.write(i + '\n')

f.close()
w.close()
