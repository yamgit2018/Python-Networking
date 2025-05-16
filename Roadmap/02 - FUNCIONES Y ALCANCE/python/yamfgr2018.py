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
def  insertIP(ip):
    print(f"Esta es la ip ingresada {ipaddress.IPv4Address(ip)}")

ip_nueva=input(f"Ingresa la ip:")
insertIP(ipaddress.IPv4Address(ip_nueva))



    



    