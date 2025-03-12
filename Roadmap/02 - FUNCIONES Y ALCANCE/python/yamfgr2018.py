"""/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */"""

#Funciones definida por el usuario
"""def hola():
    print("Hola Mundo Python")

hola()

#Funcion con retorno
def retorno_saludo():
    return "Hola Yam, vamos por ese CCNA"

saludo=retorno_saludo()
print(saludo)

print(retorno_saludo())"""

#Argumentos en la funcion
"""def saludo_arg(nombre):
    return (f"Mis nombres son {nombre}")

print(saludo_arg("Yam Francis Guerra Reyes"))

def saludo_persona(saludo,nombre):
    return (f"{saludo} {nombre}")

print(saludo_persona("Hola que tal","Yam Francis Guerra Reyes"))"""

"""def saludo_default(nombre="Python"):
    return (f"Hola que tal {nombre}")

print(saludo_default()) 
print(saludo_default("Maia Vasquez")) """

"""def saludo_default(saludo="Hola",nombre="Python"):
    return (f"{saludo} {nombre}")

print(saludo_default())
print(saludo_default(nombre="Yam Guerra"))
print(saludo_default(nombre="Maia Vasquez", saludo="Nos vemos pronto"))
print(saludo_default("Que hubo amor","Ana Cespedes"))
"""
#Retorno de varios valores 
"""def multiple_retorno():
    return "Dios ", "Danos fuerza por favor"

frase1, frase2=multiple_retorno()
print(f"{frase2} {frase1}")"""

#Argumentos Infinitos
"""def greet_coding(*lenguajes):
   for lenguaje in lenguajes:
     print(f"Hola {lenguaje}!")

greet_coding("Pyton","Java","Javascript")    """ 

# Argumentos de palabras 
"""def coding_key(**lenguajes):
   for clave  , lenguaje in lenguajes.items():
        print (f"{clave} : {lenguaje}")

coding_key(Lenguaje="Python", Tipo="Automatizacion", Variables=10)
coding_key(Lenguaje="Javascript", Tipo="Lenguaje Web")
coding_key(Lenguaje="Java")"""

#Funciones dentro de otras funciones
"""def funcion_externa():
    def funcion_interna():
        print("Funcion Interna, hola Python")
    funcion_interna()    

funcion_externa()"""

#Funcion del Lenguaje
"""print(len("Yam Francis Guerra Reyes"))
print(type(25))
print(type("Hola que tal "))
print(type(True))
print("yam".upper())"""

#Variables Locales y Globales
"""g_variable="Vamos con todo DevNet"
print(g_variable)"""

"""def hola_devnet():
    global_var="Let´s DevNet"
    local_var="Hola que tal,"
    print(local_var,global_var)

hola_devnet()"""
"""for contador in range (1,101,1):
    print(contador)"""

"""Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos."""

primer_parametro=input("Ingresa el primer dato:" )
segundo_parametro=input("Ingresa el segundo dato:")

def imprimiendo_parametros(primer, segundo) -> int:
    contador=0 #No es Multiplo ni de 3 y 5
    for numero_imp in range (1,101):
        if ((numero_imp%3==0) and (numero_imp%5==0)):
            print(f"{primer} {segundo}")
        elif (numero_imp%3==0):
            print(f"{primer}")
        elif (numero_imp%5==0) :
            print(f"{segundo}")
        else:
            contador+=1
            print(f"{numero_imp}")
    return  contador  


contador_numerico=imprimiendo_parametros(primer_parametro,segundo_parametro)
print(f"Número de veces que se ha impreso el número: {contador_numerico}")


