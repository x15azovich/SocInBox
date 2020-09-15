import re
pattern = re.compile("Scanned files: (\d{1,})")


for i, line in enumerate(open('clamAVresults.txt')):
    line = "".join(line.split())
    for match in re.finditer(pattern, line):
        print ('Found on line %s: %s' % (i+1, match.group()))

'''
with open ('clamAVresults.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line: break
        linelol = "".join(line.split()).replace(" ", "")
        print(linelol)
        print(re.findall(r'Scanned\sfiles:\s(\d{1,})', linelol)) 



for i, line in enumerate(open('clamAVresults.txt')):
    print(line)
    for match in re.finditer(pattern, line):
        scannedDir = match.group()
        print(scannedDir)

     

file1 = open('clamAVresults.txt', 'r') 
Lines = file1.readlines() 
#print(Lines[1]) 
count = 0
# Strips the newline character 
for line in Lines:
   # line = line.rstrip()
    print("".join(line.split()))

file1.close()   '''