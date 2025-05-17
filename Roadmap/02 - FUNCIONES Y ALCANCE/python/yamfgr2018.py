import ipaddress
#Funciones definida por el usuario
#Funcion Simple
"""def bannerSwitchL2():
    print("ADVERTENCIA! Acceso restringido a personal autorizado.")

bannerSwitchL2()
"""

#Funcion con retorno
"""def bannerLogin():
    return "Ingrese sus credenciales para acceder al sistema"

login=bannerLogin()
print (login) 
print(bannerLogin())"""

#Funcion con argumento
"""def  insertIP(ip):
    print(f"Esta es la ip ingresada {ipaddress.IPv4Address(ip)}")

ip_nueva=input(f"Ingresa la ip:")
insertIP(ipaddress.IPv4Address(ip_nueva))"""

#Funcion con mas de un argumento
def impresion_net_mascara(ip, mascara):
   interfaz=ipaddress.ip_interface(f"{ip}/{mascara}")

   print(f"Esta es la ip net: {interfaz.ip}")
   print(f"Esta es la mascara: {interfaz.netmask}")
   print(f"Esta es direcccion de red:{interfaz.network.network_address}")
   print(f"Esta la direccion de Broadcast: {interfaz.network.broadcast_address}")

         
    
ip=input("Ingresa direccion ip (ejm 192.168.10.0):")
mascara=input("Ingrese la mascara (ejm 24 / 255.255.255.0):")
impresion_net_mascara(ip,mascara)











    



    