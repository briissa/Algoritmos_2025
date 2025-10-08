# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:

# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

#--> hay una tabla en el archivo de este ejercicio 
from typing import Counter
from arbol import BinaryTree
from random import choice

criaturas = [
    
    {"Criatura": "Tifón", "Derrotado_por": "Zeus", "Capturada": "Teseo"},
    {"Criatura": "Enio", "Derrotado_por": "Heracles","Capturada": "Zeus"},
    {"Criatura": "Escila", "Derrotado_por": None,"Capturada": "Heracles"},
    {"Criatura": "Euríale", "Derrotado_por": None,"Capturada": "Teseo"},
    {"Criatura": "Ladón", "Derrotado_por": "Heracles","Capturada": "Zeus"},
    {"Criatura": "Hidra de Lerna", "Derrotado_por": "Heracles", "Capturada": "Teseo"},
    {"Criatura": "León de Nemea", "Derrotado_por": "Heracles", "Capturada": "Heracles"},
    {"Criatura": "Cerbero", "Derrotado_por": None,"Capturada": None},
    {"Criatura": "Cerda de Cromión", "Derrotado_por": "Teseo","Capturada": None},
    {"Criatura": "Ortro", "Derrotado_por": "Heracles","Capturada": "Teseo"},
    {"Criatura": "Toro de Creta", "Derrotado_por": "Teseo","Capturada": "Zeus"},
    {"Criatura": "Gerión", "Derrotado_por": "Teseo","Capturada": "Zeus"},
    {"Criatura": "Cloto", "Derrotado_por": None,"Capturada": None},
    {"Criatura": "Láquesis", "Derrotado_por": None,"Capturada": "Teseo"},
    {"Criatura": "Aves del Estínfalo", "Derrotado_por": "Zeus","Capturada": None},
    {"Criatura": "Talos", "Derrotado_por": "Medea","Capturada": "Heracles"},
    {"Criatura": "Sirenas", "Derrotado_por": None,"Capturada": "Teseo"},
    {"Criatura": "Cierva de Cerinea", "Derrotado_por": None,"Capturada": "Zeus"},
    {"Criatura": "Basilisco", "Derrotado_por": None,"Capturada": "Teseo"},
    {"Criatura": "Jabalí de Erimanto", "Derrotado_por": None,"Capturada": "Heracles"}
]

descripciones = [
    "Criatura marina de las profundidades.",
    "Monstruo gigante de múltiples cabezas.",
    "Ser mitad mujer, mitad serpiente.",
    "Gorgona capaz de petrificar con la mirada.",
    "Bestia con varias cabezas de serpiente.",
    "Monstruo con cuerpo de cabra, cabeza de león y cola de serpiente.",
]

arbol__ = BinaryTree()


#cargamos el arbol 
for cri in criaturas:
    info = {
        "Derrotado_por": cri ["Derrotado_por"],
        "Descripcion": choice(descripciones) #elige al alzar 'choice'
    }
    #el nombre se inserta aca como el valor del nodo
    arbol__.insert(cri["Criatura"], info)


#a. listado inorden de las criaturas y quienes la derrotaron;
print("listado ordenado por criaturas: ")
arbol__.in_order() 
# este no me convence como quedo 

# c. mostrar toda la información de la criatura Talos;
pos = arbol__.search("Talos")
if pos is not None:
    print(f'la info de {pos.value} es {pos.other_values}')
print()


# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
contador = Counter() #cuenta cuantas veces aparece cada elemento en una lista

for criatura in criaturas:
    derrotado_por = criatura["Derrotado_por"]
    if derrotado_por:  # solo contamos si no es None
        contador[derrotado_por] += 1

# Ordenar por cantidad descendente y tomar los 3 primeros
top_3 = contador.most_common(3) #obtiene los elementos mas frecuentes dentro de ese contador

print("Los 3 héroes o dioses que derrotaron más criaturas son:")
for nombre, cantidad in top_3:
    print(f"{nombre}: {cantidad} criaturas")




# e. listar las criaturas derrotadas por Heracles;
print("Criaturas derrotadas por Heracles:")
for criatura in criaturas:
    if criatura["Derrotado_por"] is not None: #no puede ser None porque no es iterable 
        if "Heracles" in  criatura["Derrotado_por"]:
            print(criatura["Criatura"])


print()
# f. listar las criaturas que no han sido derrotadas;
print("Criaturas que no han sido derrotadas:")
for criatura in criaturas:
    if criatura["Derrotado_por"] is None:
        print(criatura["Criatura"])
print()

# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
#00> ya esta hecho 


# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó; 

list_criaturas = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
#creo la lista para no hacer uno por uno 
for nombre_criatura in list_criaturas: #corremos sobre la lista
    
    pos = arbol__.search(nombre_criatura)
    if pos is not None: #verifica si fue encontrada
        pos.other_values["Derrotado_por"] = 'Heracles'
    else:
        print(f"No se encontro '{nombre_criatura}' en el arbol.")

#verifico
#arbol__.in_order()

# i. se debe permitir búsquedas por coincidencia; 

#A QUE SE REFIERE CON BUSQUEDAS POR COINCIDENCIA ??

# j. eliminar al Basilisco y a las Sirenas;
value = arbol__.delete('Sirenas')
print(f'se borro del arbol {value}')

value1 = arbol__.delete('Basilisco')
print(f'se borro del arbol {value1}')
#arbol__.in_order() 


#k.modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
pos = arbol__.search('Aves del Estínfalo')
if pos is not None: 
    pos.other_values['Derrotado_por'] = 'Heracles'



# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
value, other_values = arbol__.delete('Ladón') #el delete devuelve los datos, cambiamos 'value' y mantenemos other_values
if value is not None:
    new_value = 'Dragón Ladón'
    arbol__.insert (new_value, other_values)
#arbol__.in_order()


# m. realizar un listado por nivel del árbol;
print("Listado por nivel del arbol :")
arbol__.by_level()



#n. muestre las criaturas capturadas por Heracles.
print("muestra solo los capturados por (Heracles):")
arbol__.in_order_her()