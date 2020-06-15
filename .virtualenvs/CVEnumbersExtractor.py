import re, os
#CHANGE FILE PATH TO NOT HARD CODING 
#myDirectory = os.path.expanduser("~/SocInBox/.virtualenvs/backend/scanning/portscandata.txt")
#f = open(myDirectory, "r")
f = open("portscandata.txt", "r")
w = open("CVEnumbers.txt", "w")
x = []
while True:
    line = f.readline()
    if not line: break
    x += re.findall(r'(CVE-\d{0,4}-\d{0,})', line) 
    
for i in x:
    result = re.sub("[(),']", '', str(i))
    w.write(result + '\n')

f.close()
w.close()