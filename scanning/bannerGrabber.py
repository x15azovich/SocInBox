import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("ip:")
port = input("port:")

s.connect((ip, int(port)))

print(s.recv(1024))
