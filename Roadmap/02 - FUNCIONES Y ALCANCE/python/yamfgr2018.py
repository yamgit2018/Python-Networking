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
"""def impresion_net_mascara(ip, mascara):
   interfaz=ipaddress.ip_interface(f"{ip}/{mascara}")

   print(f"Esta es la ip net: {interfaz.ip}")
   print(f"Esta es la mascara: {interfaz.netmask}")
   print(f"Esta es direcccion de red:{interfaz.network.network_address}")
   print(f"Esta la direccion de Broadcast: {interfaz.network.broadcast_address}")"""

    
"""ip=input("Ingresa direccion ip (ejm 192.168.10.0):")
mascara=input("Ingrese la mascara (ejm 24 / 255.255.255.0):")
impresion_net_mascara(ip,mascara)"""

"""def timers_stp(hello_time=2, forward_delay_listening=15,forwar_delay_learning=15,max_age=20):
   print(f"Hello Time: {hello_time}")
   print(f"Litening: {forward_delay_listening}")
   print(f"Learning:{forwar_delay_learning}")
   print(f"Max Age:{max_age}")"""


#timers_stp()
"""timers_stp(20,30,30,0)
timers_stp()
timers_stp(hello_time=5,forwar_delay_learning=5,forward_delay_listening=12)"""


#Funcion argumentos y retorno

"""def subnet_completa(ip,mascara):
    subnet_1=ipaddress.ip_interface(f"{ip}/{mascara}")
    return subnet_1


ip=input("Ingresa la ip de la red ejm(172.16.10.40): ")
mascara=input("Ingresa la mascara ejm(24 / 255.255.255.0): ")

red=subnet_completa(ip,mascara)
print(f"Esta es la ip: {red.ip}")
print(f"Esta es la mascara: {red.netmask}")
print(f"Esta es la ip red: {red.network.network_address}")
print(f"Esta es la ip broadcast:  {red.network.broadcast_address}")
"""
#Retorno multiple

"""def ingreso_ip_mascara():
    ip=input("Ingresa una ip(ejm 192.168.10.5): ")
    mascara=input("Ingresa la mascara(ejm 255.255.255.0/24): ")
    net=ipaddress.ip_interface(f"{ip}/{mascara}")
    return net.ip, net.netmask


ip_nueva, mascara_nueva=ingreso_ip_mascara()
print(f"IP: {ip_nueva}")
print(f"Mascara: {mascara_nueva}")"""

#









         












    



    