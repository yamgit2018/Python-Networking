#Link:
# www.python.org
#Comentario en una linea 

"""
Comentario de comillas dobles
Comentario en bloque 
en varias linea
"""

'''
Sniffer de Red Básico (Usando Scapy)

Scapy es una potente librería de Python para manipulación y análisis de paquetes de red. Vamos a expandir el sniffer básico para hacerlo más útil en análisis de seguridad.

'''


packet="eth 00:00:00:00:00:00"
packet="eth 01:01:01:01:01:01:01"

PRIORIDAD_ID= 32768 #Convencion
PRIORIDAD_ID=4096
#print (f"Esta es la prioridad: {PRIORIDAD_ID}")
#print("Esta es mi mac principal:"+  packet)
#Ptyhon no tiene constantes

#Entero
cost= 4

#No existe decimales en Networking pero bueno ha practicar Python
pi=3.14

#Valores Booleanos
paquete_fragamentado=False
vlan_tagging=True


#Cadena de texto
trama="Es una trama de capa 2"
paquete='Es un paquete de capa 3'

mensaje_networking="Los paquetes no mienten"
print(trama)
print(paquete)
print("!!!"+mensaje_networking+'!!!')
print (f"!!!{mensaje_networking}!!!")





