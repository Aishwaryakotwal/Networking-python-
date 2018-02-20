#inet_aton() and inet_ntoa() 
import socket
from binascii import hexlify
def convert_address():
	for ipadr in ['127.0.0.1','192.168.0.1']:
        	packed_ip_address=socket.inet_aton(ipadr)
		unpacked_ip_address=socket.inet_ntoa(packed_ip_address)
		print "IP address is %s, packed %s and unpacked %s "%(ipadr,hexlify(packed_ip_address),unpacked_ip_address)
      
if __name__=='__main__':
	convert_address()
