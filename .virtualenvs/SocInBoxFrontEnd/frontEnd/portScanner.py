import socket, threading, time

class portScanner:

	def __init__(self, host):
		socket.setdefaulttimeout(2)
		self.f = open("portscandata.txt", "w")
		self.host = host

	def TCP_connect(self, ip, port_number, delay, output):
		TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		TCPsock.settimeout(delay)
		try:
			TCPsock.connect((ip, port_number))
			output[port_number] = TCPsock.recv(1024)
		except:
			output[port_number] = ''

	def scan_ports(self):
		
		threads = []        # To run TCP_connect concurrently
		output = {}         # For printing purposes
		data = ""
			# Spawning threads to scan ports
		for i in range(1048):
			t = threading.Thread(target=self.TCP_connect, args=(self.host, i, 2, output))
			time.sleep(.05)
			print(i)
			threads.append(t)

			# Starting threads
		for i in range(1048):
			threads[i].start()

			# Locking the main thread until all threads complete
		for i in range(1048):
			threads[i].join()

			# Printing listening ports from small to large
		for i in range(1048):
			if output[i] == '':
				#print("no data found for " + str(i))
				continue
			else:
				data += (str(i) + ': ' + str(output[i])) + '\n'
		return data

	def random(self):
		print (scan_ports(host, 2))
		f.write(scan_ports(host, 2))
		f.close()


