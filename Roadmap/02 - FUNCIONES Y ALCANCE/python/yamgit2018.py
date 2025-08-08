import ipaddress
#Funciones definida por el usuario
#Smple
"""def ip_in_red(ip_in,red_in):
    ip=ipaddress.IPv4Address(ip_in)
    red=ipaddress.IPv4Network(red_in)
    return ip in red
 

ip=input("Ingresa la ip ejm:192.168.10.5: ")
red=input("Ingresa red y sy mascara ejm: 192.168.10.0/24: ") 
validacion_ip_red=ip_in_red(ip,red)

if validacion_ip_red:
    print(f"Esta ip {ip}  esta en esta red {red}")
else:
    print(f"Esta ip {ip} no se encuentra en la red {red}")"""


"""def clasifica_ips(ip_in):
    ip=ipaddress.ip_address(ip_in)

    if ip.is_loopback:
        return f"Esta  {ip} es Lookback"
    elif ip.is_private:
        return f"Esta {ip} es Privada"
    elif ip.is_multicast:
        return f"Esta {ip} es Multicast"
    elif ip.is_global:
        return f"Esta  {ip} es Publica"
    else:
        return f"Esta  {ip} es Reservada/Especial" 
    


ip=input("Ingresa la ip para verificar si es Privada/Loopback/Multicast: ")
salida_mensaje=clasifica_ips(ip)
print (salida_mensaje)
"""

"""red=ipaddress.ip_network(input("Ingresa la red y su mascara ejm 192.168.10.0/24: "),strict=False)
print(f"Esta es la red ingresa: {red}")
"""

"""def cantidad_hosts_red(red_ingresada,cantidad=3):
    red=ipaddress.IPv4Network(red_ingresada)
    return list(red.hosts())[:cantidad]

red=input("Ingresa la red y su mascara ejem: 192.168.1.0/29: ")
cantidad_hosts=int(input("Ingresa cantidad de hosts: "))
print(cantidad_hosts_red(red,cantidad_hosts))"""

"""red=ipaddress.ip_network(input("Ingresa la red ejm 192.168.10.0/24: "))
for ip in red.hosts():
    print(ip)"""

"""
def tabla_ip(red_str):
    red=ipaddress.ip_network(red_str, strict=False)

    print("\n Red:", red,"\n")
    print(f"{'Direccion IP':<18} {'Tipo':<10}")
    print("-"*24,"\n")
    
    for ip in red:
        if ip==red.network_address:
            tipo="Red"
        elif ip==red.broadcast_address:
            tipo="Broadcast"
        else:
            tipo="Host"
        print(f"{str(ip):<18}  {tipo:<10}")    

tabla_ip(input("Ingresa una ip y su mask ejm 192.168.10.0/24: "))"""

#Con un numero de variables como  argumentos

"""def mostrar_ips(*ips):
    for ip in ips:
        print(ip)

mostrar_ips("192.168.10.1","172.16.0.5","10.0.10.100")
"""
"""
def mostrando_redes(*redes):
    for red_str in redes:
        red=ipaddress.ip_network(red_str,strict=False)
        print(red)


mostrando_redes("192.168.10.255/24","172.16.10.0/16","10.0.0.5/8")"""

#Con un  numero de argumentos con palabra clave

def informacion_red(**datos_red):
    print("Informacion de la Red")
    for clave, valor in datos_red.items():
        print (f"{clave} : {valor} ")


#Ingresamos los datos de la red:
informacion_red(
    Direccion="192.168.10.5",
    Gateway="192.168.10.240",
    Mascara="255.255.255.0",
    Tipo="Privado"
    )






