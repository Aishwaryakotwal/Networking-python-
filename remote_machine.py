import socket
def print_machine_info():
	
	hostname="www.python.org"	
	print "The remote hostname is %s"%socket.gethostbyname(hostname)
if __name__=='__main__':
	print_machine_info()
