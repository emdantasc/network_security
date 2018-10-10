import socket

Host="192.168.0.66"
port_list=range(440,450)

for x in port_list:
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	port_open=sock.connect_ex((Host,x))
	if(port_open==0):
		print("Port "+str(x)+" is open on Host: "+Host)
	else:
		print("Port "+str(x)+" is closed on Host:"+Host)
