
#Operadores
        #Artimetico
"""
print(f"Suma= {13+8}")
print(f"Resta= {15-7}")
print(f"Multiplicacion= {30*3}")
print(f"Division= {32/3}")
print(f"Modulo= {29%3}")
print(f"Exponente= {2**3}")
print(f"Division Entera= {29//3}")
"""

#Operadores de comparacion
"""
print(f"Igualdad 3==3 {3==3}")
print(f"Desigualdad 5!=3 {5!=3}")
print(f"Mayor que 5>3 {5>3}")
print(f"Menor que 2<3 {2<3}")
print(f"Mayor e igual que 5>=3 {5>=3}")
print(f"Menor e igual que 2<=3 {2<=3}")
"""

#Operadores Logicos
"""print(f"and && 23+5==28 AND 23-3==20 {23+5==28 and  23-3==20}")
print(f"or || 23+5==28 AND 23-3==20 {23+5==28 or -3==20}")
print(f"not !  10+3==12 {not 10+3==12}")"""


#Operadores de asignacion
#mi_numero_1=7
"""
print(mi_numero)
mi_numero=+9
print(mi_numero)
mi_numero-=3
print(mi_numero)
mi_numero*=9
print(mi_numero)
mi_numero/=3
print(mi_numero)
mi_numero%=2
print(mi_numero)
mi_numero**=5
print(mi_numero)
mi_numero//=3
print(mi_numero)
"""
#Operadores de identidad
"""mi_numero_2=mi_numero_1

print(f"mi numero 1:{mi_numero_1}")
print(f"mi numero 2: {mi_numero_2}")
print(f"mi numero es mi nuevo numero {mi_numero_1 is mi_numero_2}")
print(f"mi numero es no mi nuevo numero {mi_numero_1 is not mi_numero_2}")"""

#Operadores de pertenencia
"""print (f"La letra m tiene el nombre Yam {'m' in "Yam"}")
print (f"La letra m no tiene el nombre Yam {'m' not in  "Yam"}")"""

#Operadores de bits
"""bit1=15
bit2=9
print(f"Operador & de 10 & 3: {bit1 & bit2}")
print(f"Operador | de 10 | 3: {bit1 | bit2}")
print(f"Operador  XOR ^ de 3 ^ 3: {bit1 ^ bit2}")
print(f"Operador not ~ de 3: { ~bit1}")
print(f"Desplazamiento a la derecha 10>>2 {10>>2}")
print(f"Desplazamiento a la derecha 10<<2 {10<<2}")"""

#Operadores
"""soyyo="Francis"
if soyyo=="Yam":
        print("Es Yam, vamos con todo")
elif soyyo=="Francis":
        print("soy Francis lets do it")
else:
        print("No es Yam ni Francis")"""

#for
"""for iteracion in range(10):
        print(iteracion)

iteracion1=0
while iteracion1<=10:
        print (iteracion1)
        iteracion1+=1"""
        
#Excepciones 
"""try:
        pruebaError=10/2
except:
          print("Error de ejecucion")
else:
        print(f"Division Correcta:{pruebaError}")
finally:
        print("Proceso Finalizado")"""

 #DIFICULTAD EXTRA (opcional):
 # Crea un programa que imprima por consola todos los números comprendidos
 # entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

"""if ((pruebaM3%3)==0):
        print (f"El resultado es multiplo de 3  no va")
else:
        print(f"No es multiplo de 3 este numero {pruebaM3}") 

if (pruebaM3==16):
        print("Si es numero 16")
else: 
         print(f"No es 16, es {pruebaM3}")"""


for numero in range(10, 56):
        if(((numero%3)!=0)and (numero!=16) and ((numero%2)==0)):
                print(numero)
        numero+=1
