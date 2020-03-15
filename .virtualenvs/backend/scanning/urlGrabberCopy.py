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
    x += re.findall(r'(\d*\/(tcp|udp).*)open(.*)', line)
    x += re.findall(r'https:\/\/(.*)', line) 
    
#for i in x:
#    result = re.sub("[(),']", '', str(i))
#    w.write(result + '\n')
for i in range(1,len(x)-1):
    result = re.sub("[(),']", '', str(x[i]))
    w.write(result + '\n')
f.close()
w.close()
