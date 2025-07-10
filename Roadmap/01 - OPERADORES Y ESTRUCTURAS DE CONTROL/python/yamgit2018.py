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
"""def is_ip_publica(ip_publica):
    try:
        ip=ipaddress.IPv4Address(ip_publica)
        return not ip.is_private
    except ValueError:
        return False

if __name__ == "__main__":
ip_input=input("Ingresa una ip publica: ")
if is_ip_publica(ip_input):
  print(f"Es una ip publica {ip_input}")
else: 
  print(f"No es una ip publica")
"""

""" - `+=` : Suma y asigna
   - `-=` : Resta y asigna
   - `*=` : Multiplica y asigna
   - `/=` : Divide y asigna (aunque en redes no es común, lo adaptaremos)
   - `//=`: División entera y asigna
   - `%=` : Módulo y asigna"""


"""ip=ip_net.broadcast_address
print(f"Red: {ip_net}")
print(f"\nEsta es la ip  de la red 192.168.10.0/30: {ip}")"""
"""
ip_net=ipaddress.IPv4Network("192.168.10.0/29")
for i in range (1, ip_net.num_addresses-1):
    ip=ipaddress.IPv4Address(ip_net.network_address+i)
    print(f"Host {i}: {ip}")"""

#Operadores de identidad
"""ip1=ipaddress.IPv4Address(input("Ingresa la ip1: "))
ip2=ipaddress.IPv4Address(input("Ingresa la ip2: "))

print(ip1 is ip2)
print(ip1 == ip2)"""

#Operadores de pertenencia
"""red=ipaddress.IPv4Network("192.168.1.0/24")
ip1=ipaddress.IPv4Address("192.168.10.1")
ip2=ipaddress.IPv4Address("192.168.1.10")

if ip1 in red:
    print(f"{ip1} si pertenece a la red {red}")
else:
    print(f"No pertenece esta ip {ip1} a la red {red}\n")

if ip2 in red:
    print(f"Esta ip {ip2} si pertenece a la red {red}")
else:
    print(f"No pertenece esta {ip2} a la red {red}")
"""


def filtrar_ip_publicas(pull_ip):
    pool_redes_privadas=[ipaddress.IPv4Network("10.0.0.0/8"),ipaddress.IPv4Network("172.16.0.0/12"),ipaddress.IPv4Network("192.168.0.0/16")]

    pool_ip_publicas=[]

    for ip_publica_validada in pull_ip:
        ip_publica=ipaddress.IPv4Address(ip_publica_validada)
        if all(ip_publica not in red for red in pool_redes_privadas) and not ip_publica.is_private:
            pool_ip_publicas.append(ip_publica)
    return pool_ip_publicas

lista_ip_publicas=["192.168.1.1", "8.8.8.8", "10.0.0.5", "172.16.0.1", "142.250.184.238"]
print("IPs Publicas: ",filtrar_ip_publicas(lista_ip_publicas))




#Operadorez de bit















