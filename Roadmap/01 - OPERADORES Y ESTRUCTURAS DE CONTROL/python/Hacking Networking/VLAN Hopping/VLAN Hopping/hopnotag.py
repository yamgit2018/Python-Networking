#Import scapy
from scapy.all import *

#Craft packet with 802.1Q headers
packet = Ether(dst="ff:ff:ff:ff:ff:ff")/\
         IP(src="10.1.2.2",dst="10.1.2.3")/\
         ICMP()

#Show packet
packet.show()

#Sent packet
sendp(packet)