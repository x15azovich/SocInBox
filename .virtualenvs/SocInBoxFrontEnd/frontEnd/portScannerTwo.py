import socket, threading
socket.setdefaulttimeout(2)
f = open("portscandata.txt", "w")
host = input("ip:")

def main():
    scan_ports('8.8.8.8', 2)

def TCP_connect(ip, port_number, delay, output):
	TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	TCPsock.settimeout(delay)
	try:
		TCPsock.connect((ip, port_number))
		output[port_number] = TCPsock.recv(1024)
	except:
		output[port_number] = ''

def scan_ports(host_ip, delay):
	
	threads = []        # To run TCP_connect concurrently
	output = {}         # For printing purposes
	data = ""
    # Spawning threads to scan ports
	for i in range(10000):
		t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
		threads.append(t)

    # Starting threads
	for i in range(10000):
		threads[i].start()

    # Locking the main thread until all threads complete
	for i in range(10000):
		threads[i].join()

    # Printing listening ports from small to large
	for i in range(10000):
		if output[i] == '':
			#print("no data found for " + str(i))
			continue
		else:
			data += (str(i) + ': ' + str(output[i])) + '\n'
	return data

print (scan_ports(host, 2))
f.write(scan_ports(host, 2))
f.close()

if __name__ == "__main__":
    main()
