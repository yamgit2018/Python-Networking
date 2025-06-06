import ipaddress
#Estructura de Datos:
#Lista
"""subred_planta1= ["172.17.0.0/24", "172.17.10.0/24","172.17.20.0/24"]

print(subred_planta1)
print("\n")
for red in subred_planta1:
    print(red)"""


hop=10
numero_subnet=5

subnet=[ipaddress.IPv4Network(f"172.17.{indice}.0/24") for indice in range (0,numero_subnet*hop,hop)]
print("\n")
for red in subnet:
    print(red)




