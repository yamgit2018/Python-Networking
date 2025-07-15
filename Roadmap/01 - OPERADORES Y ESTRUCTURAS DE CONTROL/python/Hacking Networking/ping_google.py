from scapy.all import *
packet = Ether()/IP(dst="8.8.8.8")/ICMP()
packet.show()

