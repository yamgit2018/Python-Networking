"""/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
"""
# Listas
"""mi_lista=["Yam","Any","Carlos","Janda"]
print(mi_lista)
mi_lista.append("Cattaleya") #Insercion
print(mi_lista)
mi_lista.remove("Cattaleya")#Eliminacion
print(mi_lista)
mi_lista[0]="Valeria" #Actualizacion
print(mi_lista)
mi_lista.sort()#Ordenacion
print(mi_lista)"""

#Tuplas
"""mi_tupla= ("Yam Francis", "Guerra Reyes", "Loco Sencillo",42)
for tupla in mi_tupla:
    print(tupla)"""

"""matriz=(
        (1,2,3),
        (4,5,6),
        (7,8,9)
    )

print(matriz[2][0])"""

frutas=("Manzana", "Pera", "Durazno")
"""fruta1,fruta2,fruta3=frutas
print(fruta1)
print(fruta2)
print(fruta3)"""
frutas=tuple(sorted(frutas)) #Ordenacion
for fruta in frutas:
    print(fruta)

print(type(frutas))

