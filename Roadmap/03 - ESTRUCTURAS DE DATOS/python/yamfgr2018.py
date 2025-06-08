import ipaddress
#Estructura de Datos:
#Lista []
"""subred_planta1= ["172.17.0.0/24", "172.17.10.0/24","172.17.20.0/24"]

print(subred_planta1)
print("\n")
for red in subred_planta1:
    print(red)"""


hop=10
numero_subnet=5
subnet=[ipaddress.IPv4Network(f"172.17.{indice}.0/24") for indice in range (0,numero_subnet*hop,hop)]
print("\n")
print(subnet)
print("\n")
for red in subnet:
    print(red)
print(type(subnet))
print("\n")
"""print("\n")
print("Ingresmos una lista de subnets Planta 1")
for red in subnet:
    print(red)
""""""
#Insercion de una dato a la lista:
subnet.append(ipaddress.IPv4Network("172.17.50.0/24"))
print("\n")
print("Ingresamos una subnet 172.17.50.0/24")
for red in subnet:
    print(red)

# Borrado de un item a la lista
subnet.remove(ipaddress.IPv4Network("172.17.0.0/24"))
print("\n")
print("Eliminamos  una subnet 172.17.0.0/24")
for red in subnet:
    print(red)
"""
#Actualizacion de la lista subnet
#Cambiamos la subnet 172.17.50.0 x 172.17.60.0
"""subnet_reemplazar=ipaddress.IPv4Network(input("Ingresa la subnet a remplazar:"))
subnet_nueva=ipaddress.IPv4Network(input("Ingresa la nueva subnet:"))

if subnet_reemplazar in subnet:
    index=subnet.index(subnet_reemplazar)
    subnet[index]=subnet_nueva
    print("\n Subnet ingresada exitosamente")
else:
    print("\n Esta subnet no se encuentra en lista")
    

print("\nLista Actualizada")
for red in subnet:
    print(red)"""

#Ordenacion de los datos
"""subnet.sort(reverse=True)
print("\n")
for red  in subnet:
    print(red)"""

#Tuplas ()
tupla_subnet=("172.17.0.0/24", "172.17.10.0/24","172.17.20.0/24")
print(tupla_subnet)
print(type(tupla_subnet))
