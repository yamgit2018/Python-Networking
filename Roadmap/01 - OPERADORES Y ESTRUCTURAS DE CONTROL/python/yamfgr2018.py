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
print(f"Igualdad de 3 = 3: {3==3}")
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


