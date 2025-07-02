#Modulo ipaddress
import ipaddress
"""ip=ipaddress.IPv4Address("10.0.0.240")
print(f"\nEsta en la IP de la interface {ip}")"""
#print(type(ip))

# Pagina de Python: https://www.python.org/
"""Pagina de Libreria de pyton ipaddress: https://docs.python.org/3/library/ipaddress.html"""

"""ip_net=ipaddress.IPv4Network("192.168.10.0/30")
print(f"\nEsta es la red 192.168.10.0/30: {ip_net}")"""

#Constantes
#Clase IPv4Address
"""NETMASK_24=ipaddress.IPv4Address("255.255.255.0")
NETMASK_16=ipaddress.IPv4Address("255.255.0.0")
NETMASK_8=ipaddress.IPv4Address("255.0.0.0")

def calcular_red(ip,mask):
    interface=ipaddress.IPv4Interface(f"{ip}/{mask}")
    return interface.network

ip=input("Inserta una ip y su mascara ejm:192.168.10.5: ")
mask=input("Ingresa la mascara: ejm:/24 o /16 o /8: ")
 
if (mask == "/24"):
    print(calcular_red(ip,NETMASK_24))
elif(mask == "/16"):
    print(calcular_red(ip,NETMASK_16))
else:
    print(calcular_red(ip,NETMASK_8))"""

ip_vlan10=ipaddress.IPv4Network("192.168.10.0/24")
print(ip_vlan10)
