import subprocess, ctypes, os, sys
from subprocess import Popen, DEVNULL

def check_admin():
	""" Force to start application with admin rights """
	try:
		isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
	except AttributeError:
		isAdmin = False
	if not isAdmin:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def add_rule(rule_name, ip_address):
	""" Add rule to Windows Firewall """
	subprocess.call(
		f"netsh advfirewall firewall add rule name={rule_name} dir=in interface=any action=block remoteip={ip_address}", 
		shell=True, 
 		stdout=DEVNULL, 
		stderr=DEVNULL
	)
	print(f"Rule {rule_name} for {file_path} added")

def modify_rule(rule_name, state):
    #""" Enable/Disable specific rule, 0 = Disable / 1 = Enable """
	state, message = ("yes", "Enabled") if state else ("no", "Disabled")
	subprocess.call(
		f"netsh advfirewall firewall set rule name={rule_name} new enable={state}", 
		shell=True, 
		stdout=DEVNULL, 
		stderr=DEVNULL
	)
	print(f"Rule {rule_name} {message}")

def delete_rule(rule_name, ip_address):
	""" Enable/Disable specific rule, 0 = Disable / 1 = Enable """
	subprocess.call(
		f"netsh advfirewall firewall delete rule name={rule_name} dir=in interface=any action=allow remoteip={ip_address}", 
		shell=True, 
 		stdout=DEVNULL, 
		stderr=DEVNULL
	)
	print(f"Rule {rule_name} for {file_path} added")


if __name__ == '__main__':
	check_admin()
	add_rule("RULE_NAME", "IP_ADDRESS")
	modify_rule("RULE_NAME", 1)
	delete_rule("RULE_NAME" "IP_ADDRESS")



#netsh advfirewall firewall add rule name="IP Block" ^
#dir=in interface=any action=block remoteip=198.51.100.108/32
#netsh advfirewall firewall show rule name="IP Block"
#netsh advfirewall firewall delete rule name="IP Block" remoteip=198.51.100.108/32`

