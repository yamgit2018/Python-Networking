
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

#frutas=("Manzana", "Pera", "Durazno","Manzana")

"""fruta1,fruta2,fruta3=frutas
print(fruta1)
print(fruta2)
print(fruta3)"""
"""frutas=tuple(sorted(frutas)) #Ordenacion
for fruta in frutas:
    print(fruta)

print(type(frutas))"""


#Sets
""""mi_set={"Yam", "Guerra", "@yamfgr2018","42"}
print(mi_set)
for datos in mi_set:
    print(datos)"""

"""mi_set.add("yamfgr2018@gmail.com") #Insercion
mi_set.remove("42")#Eliminacion
mi_set=sorted(mi_set)
print(mi_set)

papa_set:set={"Carlos","Guerra","62"}
print(papa_set)"""

#Diccionario
""""mi_dicc={"Nombres":"Maia Vasquez Guerra",
         "Edad":"8","Lugar de Nacimiento":"Pisco"}
mi_dicc["Nombres"]="Yam Francis Guerra Reyes"#Actualizacion
mi_dicc["Profesion"]="Ingeniero Informatico"#Agregacion
mi_dicc["Edad"]="42"#Actualizacion
del mi_dicc["Lugar de Nacimiento"] #Eliminacion
print(mi_dicc)
print(type(mi_dicc))



for clave, valor in mi_dicc.items():
   print (f"{clave}: {valor}")

mi_dicc= sorted(mi_dicc.items())
print(mi_dicc)"""


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
"""agenda=[
[{"Nombre":"Yam Guerra", "Celular":935378556},{"Nombre":"Ana Cespedes", "Celular":123456789},{"Nombre":"Carlos Guerra", "Celular":987654321}]
]

for fila in agenda:
    for celda in fila:
        print(celda,end=" ")"""


print("Agenda")

numero_ingresos=int(input("Ingresa el numero de contactos a ingresar:"))


for cuenta in range():
    nombre=input("Ingresa tus nombres: ")
    celular=int(input("Ingresa tu numero celular: "))
    mi_agenda= {"Nombres:":nombre,"Celular:":celular}

for clave , dato in mi_agenda.items():
    print(f"{clave} {dato}")





