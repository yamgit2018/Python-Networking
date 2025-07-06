import ipaddress
#Operadores
#IPv4
"""ip=ipaddress.IPv4Address("192.168.10.100")
print (f"Esta es la ip: {ip}")
print (f"Suma +5: {ip+5}")
print (f"Resta -10: {ip-10}")"""

#IPv6
"""ipv6=ipaddress.IPv6Address("2001:db8::a")
print (f"\nEsta es la IPv6: {ipv6}")
print (f"Sumamnos +10: {ipv6+10}")
print (f"Restamos -10: {ipv6-10}")

pool_ip=ipaddress.IPv4Address("10.0.1.100")
print("\n Agregamos 5 ips del pool 10.0.1.100")
for ip in  range (1,10):
    print (f"IP {ip} - {pool_ip+ip}")"""

#Operadores de comparacion
"""ip1=ipaddress.ip_address("192.168.20.5")
ip2=ipaddress.ip_address("192.168.10.100")

print(ip1==ip2)
print(ip1!=ip2)
print(ip1<ip2)
print(ip1>ip2)
"""
#Operadores Logicos
#AND
"""def es_ip_valida(ip):
    try:
        ip_validada=ipaddress.ip_address(ip)
        return(ip_validada.version==4 and ip_validada.is_private and ip_validada!=ipaddress.IPv4Address("192.168.1.1")) 
    except ValueError:
        return False
       
   
ip=ipaddress.ip_address(input("Ingresa una ip privada: ") )
print(ip)"""

#OR 

"""def ip_is_special(ip):
    try:
        ip_validada=ipaddress.ip_address(ip)
        return(
            ip_validada.is_loopback or
            ip_validada.is_multicast or
            ip_validada.is_reserved
        )
    except ValueError:
        return False

print("========== Vamos a validar una ip especiales =============")   
print(ip_is_special(input("Ingresa una ip especial: ")))"""

#not
def is_ip_publica(ip_publica):
    try:
        ip=ipaddress.IPv4Address(ip_publica)
        return not ip.is_private
    except ValueError:
        return False
    
"""if __name__ == "__main__":"""
ip_input=input("Ingresa una ip publica: ")
if is_ip_publica(ip_input):
  print(f"Es una ip publica {ip_input}")
else: 
  print(f"No es una ip publica")










