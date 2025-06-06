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

# Con un numero variable de argumentos
"""def imprimir_ips(*ips): 
    for ip in ips:
        print(f"Esta es la ip: {ip}")

imprimir_ips("192.168.10.100",1,2.4)"""

#keyword arguments como argumento, clave - valor
"""def imprimir_valores_ospf(**valores_preterminado_ospf):
  #  print(type(valores_preterminado_ospf))
  
    for parametro,valor in valores_preterminado_ospf.items():
        print(f"{parametro}: {valor}")


imprimir_valores_ospf(Hello=10,Dead=4,Prioridad=1)
"""
#Funciones Anidadas:
"""def validar_verificar_ip():
    def es_ip_en_subnet(ip,subnet):
        try:
            ip_validacion=ipaddress.IPv4Address(ip)
            subnet=ipaddress.IPv4Network(subnet)
            return ip_validacion in subnet
        except ValueError as e:
            return f"!Error {e} no es una ip"
    

    ip=input("Ingresa una ip para la validacion ejm 192.168.10.1:")
    subnet="192.168.10.0/24"
    resultado=es_ip_en_subnet(ip,subnet)

    if isinstance(resultado, bool):
        if resultado:
            print(f"Esta ip {ip} esta en red {subnet}")
        else:       
            print(f"Esta ip {ip} no esta en la red {subnet}")
    else:
        print (resultado)  
validar_verificar_ip()      """

#Funiones Python
"""subnet=ipaddress.IPv4Network("192.168.10.0/30")
print(f"La IP red es: {subnet.network_address}")
print(f"La ip de broadcast: {subnet.broadcast_address}")
print(f"La mascara de red: {subnet.netmask}")
print("\n")
print("IPs de hosts en la red 192.168.10.0/30")
for ip in subnet.hosts():
    print(ip)"""

#Variables Locales y Globakes
#Ambito de las variables
"""OSPF_DEFAULT_AREA="0.0.0.0"
MTU=1500

activeRouters=0
routerA=1
active_routers=routerA

def add_router(routerB=3):
    global activeRouters
   # active_routers=routerB
    activeRouters=routerB

add_router()
print(f"Routers activos {activeRouters}")
print(f"MTU: {MTU}")"""

#Extra
"""* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
print("Bienvenido Contador del 1 al 100 de multiplos de 3 y 5 \n")
primer_texto=input("Ingresa el primer texto: ")
segundo_texto=input("Ingresa el segundo texto: ")
cantidad_3=0
cantidad_5=0
no_cantidad_3_5=0

for valor_numerico in range (1,101):
    if((valor_numerico%3==0)and(valor_numerico%5==0)):
        print(f"Es multiplo de 3 y 5: {valor_numerico} {primer_texto} {segundo_texto}")
        cantidad_3+=1
    elif(valor_numerico%3==0):
        print(f"Es mutiplo de 3: {valor_numerico} {primer_texto}")
        cantidad_5+=1
    elif(valor_numerico%5==0):
        print(f"Es multiplo de 5: {valor_numerico} {segundo_texto}")
    else:
        print(f"No es multiplo ni de 3 y 5: {valor_numerico}")
        no_cantidad_3_5+=1
print("\n")
print(f"Cantidad de multiplos de 3: {cantidad_3}")
print(f"Cantidad de multiplos de 5: {cantidad_5}")
print(f"Cantidad de no multiplos de 3 y 5: {no_cantidad_3_5}")













         












    



    