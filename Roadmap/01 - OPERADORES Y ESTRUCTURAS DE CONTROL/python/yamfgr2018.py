"""
EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""
#####################################################################################
import binascii    # Conversiones binarias
import ipaddress   # Manejo de direcciones IP y redes
import socket      # Operaciones de red de bajo nivel
#Operadores Aritmeticos
"""prioridad_sw1=4096
prioridad_sw2=32768    
SW1_IP="192.168.10.100"
SW2_IP="192.168.11.200"
print(f"Suma para aumentar la prioridad de SW1 Brigde ID SW1: {prioridad_sw1+4096}")
print(f"Resta para convertir a SW2 en root bridge Root ID SW2: {prioridad_sw2-4096}" )

print(f"Multiplicacion ICMP de   a 192.168.11.200 x4:")
for contador_icmp in range(4):
    print(f"Ping de {SW1_IP} a {SW2_IP}")

print(f"Valor decimal de 8 bits es: {2**8} ")
print(f"Valores de 8 bits son: 0 a {2**8-1}")

#Operadores de comparacion
MAC_SW1="aa.04.23.45.56.36"
MAC_SW2="45.36.89.ff.ab.45"
if (MAC_SW2==MAC_SW1):
   print(f"Mac SW1 es igual Mac SW2")
else:
    print("No son iguales Mac SW1 con Mac SW2")

if (MAC_SW2!=MAC_SW1):
     print("No son iguales Mac SW1 con Mac SW2")
else:
     print(f"Mac SW1 es igual Mac SW2")    


if(prioridad_sw2>prioridad_sw1):
    print("Prioridad SW2  tiene mayor que SW1")
else:
    print("Prioridad SW1  tiene mayor que SW2")

    
#Operadores Logicos
#AND  TRUE TRUE los dos deben ser true
#OR   TRUE solo uno debe ser
#NOT  AL TRUE lo vuelve FALSE y FALSE lo vuelve TRUE

if((MAC_SW1>MAC_SW2) and (prioridad_sw1<prioridad_sw2)):
    print("TRUE")
else:
    print("FALSE")

#Operadores de asignacion
SVI_VLAN10="192.168.10.5"
print(f"IP INT VLAN10= {SVI_VLAN10}")

loop=0
while(loop<=10):
    print(loop)
    loop+=1

#Operadores de Identidad
#MAC_SW2=MAC_SW1
print(f"MAC_SW1 no es igual MAC_SW2: {MAC_SW1 is not MAC_SW2}")

#Operadores de pertenecia
print(f"'aa' pertenece a la MAC_SW1 {'aa' in MAC_SW1}")
print(f"'00' No pertenece a la MAC_SW1 {'00' not  in   MAC_SW1}")
"""
#Operadores de Bit
"""ip = ipaddress.IPv4Address('192.168.10.240')
ip +=5  
print(ip)

red=ipaddress.IPv4Network('192.168.10.0/24')
print(f"Esta es l mascara de red: {red.netmask}")
print(f"Esta es la ip de broadcast: {red.broadcast_address}")
print(f"Esta es la ip de red: {red.network_address}")
"""

"""ip=ipaddress.IPv4Address('192.168.10.10')
ip_int=int(ip)


#Obtenemos la IP de red:
mascara=0xFFFFFF00 #/24
red_resultante=ip_int & mascara
print(ipaddress.IPv4Address(red_resultante))"""
"""valorb1=0b1100
valorb2=0b1010
#Operador and
print(10 and 12)
print(10 & 12)

print(10 or 12)
print(10 | 12)"""
"""#Operadpr or
print(bin(valorb1 or valorb2))
#Operador xor
print(bin(valorb1 ^ valorb2)) 
#Opereador NOT
print(f"Valor negativo de 10  es {~ 10}")"""

"""#Desplazamiento izq der
print(f"Desplazamiento a al derecha 10>>2: {10>>2}")
#1010   >>  0010
print(f"Desplazamiento a al izquierda 10<<2: {10<<2}")
#1010 << 101000 
"""
#Estructura de Control

#Condicional if

#/26
"""if mascara==0xfffffe0:
    print("Es mascara /23")
else:
    print("No es mascara /23")
"""
#Condicional Intermedia
"""if mascara==0xFFFFFe00:
    print("Es mascara /23")
elif mascara==0xffffff00:
    print("Es mascara /24")
else:
    print("No es ni mascara /23 y /24")"""

#Iterativas
"""ip=ipaddress.IPv4Address("192.168.100.1")
if(ip=="192.168.100.1"):
    print(f"Esta es la ip 192.168.100.1")
else:"""
  #  print("Esta no es la ip 192.168.100.1")
"""for ip in range(1,10):  #1-9
    print(f"Esta es la ip {ip}")"""
"""while(ip<"192.168.100.10"):
      print(f"Esta es la ip {ip}")
      ip+=1"""
#for ip in range(10):
"""ip_inicio=ipaddress.IPv4Address('192.168.100.1')
ip_final=ipaddress.IPv4Address('192.168.100.10')

for ip in range(int(ip_inicio),int (ip_final)):
    print(f"Esta es la IP: {ipaddress.IPv4Address(ip)}")"""

"""mascara_24=0xffffff00#/24
print(f"Esta es la mascara /24: {ipaddress.IPv4Address(mascara_24)}")
mascara_30=0xfffffffc#/30
print(f"Esta es la mascara /30: {ipaddress.IPv4Address(mascara_30)}")
mascara_29=0xfffffff8#/29
print(f"Esta es la mascara /29: {ipaddress.IPv4Address(mascara_29)}")

mascara=0xffffff00 #/24
if mascara==0xffffff00:
    print("Es mascara /24")
elif mascara==0xffffff00:
    print("Es mascara /23")
else:
    print("No es ni mascara /23 y /24")"""


"""ip_inicio=ipaddress.IPv4Address('192.168.100.1')
#ip_final=ipaddress.IPv4Address('192.168.100.6')
ip_inicio+=100
print(ip_inicio)
"""
#While
"""ip=ipaddress.IPv4Address('192.168.10.0')
ip_final=ipaddress.IPv4Address('192.168.10.10')
while (int(ip)<int(ip_final)):
    print(ip)
    ip+=1
"""
"""
ip=ipaddress.IPv4Address("192.168.10.15")
print(type(ip))"""

#while
"""ip1=ipaddress.IPv4Address("172.16.0.100")
ip_final=ipaddress.IPv4Address("172.16.0.110")
while(int(ip1)<=int(ip_final)):
    print(ip1)
    ip1+=1 

#For
ip_inicial2=ipaddress.IPv4Address('172.17.0.100')
ip_final2=ipaddress.IPv4Address('172.17.0.111')
for ip2 in range(int(ip_inicial2),int(ip_final2)):
    print(ipaddress.IPv4Address(ip2))"""

#Manejo de Excepciones 
"""try:
    
    dividiendo=int(input("Ingresa el dividiendo: "))
    divisor=int(input("Ingresa el divisor: "))
    cociente=dividiendo/divisor
except ZeroDivisionError:
    print("Error en la division")
else:
    print(f"La division es {cociente}")
finally:
    print("Finalizacion de la division")    """

"""* DIFICULTAD EXTRA (opcional):
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3"""

"""ip_inicio=ipaddress.IPv4Address("192.168.10.10")
ip_final=ipaddress.IPv4Address("192.168.10.56")

for ip_nueva in range(int(ip_inicio),int(ip_final)):
    if(((int(ip_nueva))%2) ==0 and ((int(ip_nueva))%16)!=0 and ((int(ip_nueva)%3)!=0)):
        print(ipaddress.IPv4Address(ip_nueva))
        print(ip_nueva)
"""
valor_inicial=10
valor_final=56
for valor in range (valor_inicial,valor_final):
    if ((valor%2==0) and (valor!=16) and ((valor%3)!=0)):
        print(f"Este valor es par: {valor}")