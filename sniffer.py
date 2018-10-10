from scapy.all import *

def read_packet(packet):
    if packet[TCP].payload and packet[TCP].dport==80:
            print("\nHTTP Capture: \nRequest from: "+packet[IP].src+":"+str(packet[IP].dport)
                +"\nServer at: "+packet[IP].dst+":"+str(packet[IP].dport)
                +"\nContent: "+str(bytes(packet[TCP].payload)))
                

sniff(iface='enp7s0', filter='tcp', prn=read_packet, store=0)