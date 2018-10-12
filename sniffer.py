from scapy.all import *

def read_packet(packet):
    if packet[TCP].payload:
            print("\nHTTP Capture: \nRequest from: "+packet[IP].src+":"+str(packet[IP].sport)
                +"\nServer at: "+packet[IP].dst+":"+str(packet[IP].dport))
            

sniff(iface='enp7s0', filter='tcp port 80', prn=read_packet, store=0)