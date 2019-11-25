import socket
socket.setdefaulttimeout(2)

host = input("ip:")

def portscanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if not(s.connect_ex((host,port))):
        print ("port", port, "is open!!!!!!")
    s.close()

for port in range (20,26):
    portscanner(port)

