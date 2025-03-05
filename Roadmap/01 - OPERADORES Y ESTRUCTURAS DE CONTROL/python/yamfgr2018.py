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
######################################################################################
#Operadores de comparación
"""""print(f"Igualdad de 3 = 3: {3==3}")
print(f"Desigualdad de 10 != 3: {10!=3}")
print(f"Mayor de 10 > 3: {10>3}")
print(f"Menor de 3 < 15: {3<10}")
print(f"Mayor igual de 40 >= 15: {40>=15}")
print(f"Menor igual de 3 <= 3: {3<=3}")

#Operadores Logicos
print(f"AND &&: 10+3==13 and 5-2==4 es {10+3==13 and 5-2==4}")
print(f"OR |: 10+3==13 OR 5-2==4 es {10+3==13 or 5-2==4}")
print(f"NOT !: 5*5==15  es {not (5*5==15)}")

#Operadores de asignacion
cell_phone=935375856
print(f"Mi numero celular es: {cell_phone}")

contador=8 #Asignacion
print(f"El numero contador es: {contador}")
contador+=0.5 #Suma
print(f"El numero contador es: {contador}")
contador**=0.5 #Exponente
print(f"El numero contador es: {contador}")
contador//=0.5 #Division Entera
print(f"El numero contador es: {contador}")
contador-=0.5 #Resta
print(f"El numero contador es: {contador}")
contador*=0.5 #Multiplicacion
print(f"El numero contador es: {contador}")
contador/=0.5 #Division
print(f"El numero contador es: {contador}")
contador%=0.5 #Modulo
print(f"El numero contador es: {contador}")


#Operadores de identidadpwd
entero_1=int(5000)
entero_2=int(5000)
print(f"entero_1 is entero_2 {entero_1 is entero_2}")
print(f"entero_1 is not entero_2 {entero_1 is not entero_2}")

#Operadores de pertenencia 
print(f"La letra a esta en Yam: {"a" in "Yam"}")
print(f"La letra z no  esta en Yam: {"z" not in "Yam"}")

#Operadores de bit
valor1=10 #1010
valor2=3 #0011
print(f"AND:10&3: {10 & 3}") #0010
print(f"OR:10&3: {10 | 3}") #1011
print(f"XOR:103: {10 ^ 3}") #1001   
print(f"NOT ~ calc: {~10}")#1010 not 0101
print(f"Desplazamiento a la derecha {10>>2}")#1010 >> 0010
print(f"Desplazamiento a la izquierda {10<<2}")#1010 >> 101000"""""


#Estructura de Control
#Condicional
"""nombreCompleto="Maia Vasquez"
if nombreCompleto=="Yam Guerra":
    print(f"El es {nombreCompleto}")
elif nombreCompleto=="Ana Cespedes":
    print(f"Ella es {nombreCompleto}")
else:
    print(f"Esta persona no es Yam Guerra ni Ana Cespedes, es {nombreCompleto}")"""

#Iterativa

"""for iteracion in range(1,limite,1):
    if (iteracion%2==0):
        print(iteracion)"""
"""limite=50
iteracion=1
while(iteracion<=limite):
    if(iteracion%2==0):
        print(iteracion)
    iteracion+=1
"""

#Excepciones
"""valor_ingresado=float(input("Ingrese el numero a dividir 10/"))
try:
    resultado=10/valor_ingresado
except ZeroDivisionError:
     print(f"Error en el servicio")
else:
    print (f"Resultado es : {resultado}")
finally:
    print("Finalizo el servicio")
"""
#Ejercicio 
 # Crea un programa que imprima por consola todos los números comprendidos
 # entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

valor_numerico_final=55
for valor_impreso in range(10,valor_numerico_final+1):
    if((valor_impreso%2==0) and (valor_impreso!=16) and (valor_impreso%3!=0)):
        print(valor_impreso)



        



