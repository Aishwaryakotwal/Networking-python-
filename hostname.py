import socket
hostname=socket.gethostname()
print "The hostname is %s"%hostname
hostname1=socket.gethostbyname(socket.gethostname())
print "The Address is %s"%socket.gethostbyname(hostname1)
