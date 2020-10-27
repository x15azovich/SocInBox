import subprocess, ctypes, os, sys
from subprocess import Popen, DEVNULL

def check_admin():
	""" Force to start application with admin rights """
	try:
		isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
		print("is admin")
	except AttributeError:
		isAdmin = False
		print("is not admin")
	if not isAdmin:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
		print("not admin")

def add_rule(rule_name, ip_address):
	""" Add rule to Windows Firewall """
	my_file = open("list_of_bad_ips.txt", "r")
	content_list = my_file.readlines()
	#print(content_list)
	content_list.append(ip_address)
	#print(content_list)
	#print(rule_name)
	#print(ip_address)
	for x in content_list:
		subprocess.call(
			f'netsh advfirewall firewall add rule name="{rule_name}" dir=in interface=any action=block remoteip={x}', 
			shell=True, 
			stdout=DEVNULL,
			stderr=DEVNULL
		)
	print(f"Rule {rule_name} for {ip_address} added")

'''
def modify_rule(rule_name, ip_address):
    #""" Enable/Disable specific rule, 0 = Disable / 1 = Enable """
	state, message = ("yes", "Enabled") if state else ("no", "Disabled")
	subprocess.call(
		f'netsh advfirewall firewall set rule name={rule_name} new remoteip={ip_address}', 
		shell=True, 
		stdout=DEVNULL, 
		stderr=DEVNULL
	)
	print(f"Rule {rule_name} {message}")
'''

def delete_rule(rule_name):
	""" Enable/Disable specific rule, 0 = Disable / 1 = Enable """
	subprocess.call(
		f'netsh advfirewall firewall delete rule name={rule_name}', 
		shell=True 
 		# stdout=DEVNULL, 
		# stderr=DEVNULL
	)

def delete_ip(rule_name, ip_address):
	my_file = open("list_of_bad_ips.txt", "r")
	content_list = my_file.readlines()
	#print(content_list)
	content_list.remove(ip_address)
	#print(content_list)
	""" Enable/Disable specific rule, 0 = Disable / 1 = Enable """
	for x in content_list:
		subprocess.call(
			f'netsh advfirewall firewall add rule name={rule_name} dir=in interface=any action=block remoteip={x}', 
			shell=True 
			# stdout=DEVNULL, 
			# stderr=DEVNULL
		)

#if __name__ == '__main__':
	#check_admin()
	#add_rule("RULE_NAME", "162.59.2.36")
	#modify_rule("RULE_NAME", 1)
	#delete_rule("RULE_NAME")



#netsh advfirewall firewall add rule name="IP Block" ^
#dir=in interface=any action=block remoteip=198.51.100.108/32
#netsh advfirewall firewall show rule name="IP Block"
#netsh advfirewall firewall delete rule name="IP Block" remoteip=198.51.100.108/32`

