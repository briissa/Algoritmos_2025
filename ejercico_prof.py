# 15. Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas
# a un archivo que contiene personajes de la saga de Star Wars, de los cuales se sabe su nombre,
# altura y peso. Además deberá contemplar los siguientes requerimientos:

# a. en el árbol se almacenara solo el nombre del personaje, además de la posición en la que se encuentra en el archivo (nrr);
# b. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
# c. mostrar toda la información de Yoda y Boba Fett;
# d. mostrar un listado ordenado alfabéticamente de los personajes que miden más de 1 metro;
# e. mostrar un listado ordenado alfabéticamente de los personajes que pesan menos de 75 kilos;
# f. deberá utilizar el TDA archivo desarrollado en el capítulo V;

 

from arbol import BinaryTree
from random import randint
# nombre, altura y peso

# b. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo
# de baja;


star_wars_tree_name = BinaryTree() #el arbol donde se guarda el nombre
star_wars_tree_id = BinaryTree()#el arbol donde se guarda el ID

#lo que le agregamos ademas del nombre del superhheroe es el ID (que es el numero)
characters = [('Yoda', 1), ('Darth Vader', 2), ('Boba Fett', 3), ('Grogu', 4), ('Mando', 5), ('Han Solo', 6), ('Palpatine', 9), ('Mace Windu', 10)]
#cargamos alguno personajes porque los tenemos que cargar a mano


#cargamos toda la informacion en el arbol
for character in characters:
    info = {  #este es un diccionario uqe contiene el peso y la altura y los determina de forma aleatoria (porque es un dato que no sabemos)
        'weight': randint(10, 100),
        'height': randint(40, 190),
    }
    #esto deberia agregar el ID (qeu esta en la pos 1)al corespondiente super heroe
    info.update({'id': character[1]})
    #con character[0] indico que quiero el nombre que esta en la primer posicion 
    star_wars_tree_name.insert(character[0], info)

    #hace uan copia del diccionario info para no modificar el original 
    info2 = info.copy()
    info2.pop('id')
    info2.update({'name': character[0]})
    star_wars_tree_id.insert(character[1], info2)


star_wars_tree_name.in_order()
print()

# punto b
#como tenemos 2 arboles debemos de insertar en ambos el nuevo personaje (en uno lo llamaos  por nombre y en el otro por ID)
star_wars_tree_name.insert('R2-D2', {'weight': 100, 'height': 85, 'id': 15})
star_wars_tree_id.insert(15, {'weight': 100, 'height': 85, 'name': 'R2-D2'})

#busca el personaje por nombre y lo elimina, pero para eliminarlo de los 2 arboles, le pasa el other_value que contiene el ID 
#porque el segundo arbol se maneja por ID, se lo pasa y lo elimina 
value, other_value = star_wars_tree_name.delete('Palpatine')
star_wars_tree_id.delete(other_value['id'])






#lo que esta haciendo aca es buscandolo para luego modificarlo (justo hacemos el superheroe R2-D2 proque sabemmos sus medidas)
pos = star_wars_tree_name.search('R2-D2')
if pos is not None:
    #aca les asigna otro valor a peso y altura 
    pos.other_values['weight'] = 115
    pos.other_values['height'] = 71

value, other_values = star_wars_tree_name.delete('Mando')
if value is not None:
    new_value = 'Din Djarin'
    star_wars_tree_name.insert(new_value, other_values)
    #para cambiar el otro arbol, buscamos por id y cambiamos el nombre
    pos = star_wars_tree_id.search(other_values['id'])
    pos.other_values['name'] = new_value


# print('buscando', star_wars_tree_name.search('Din Djarin').value)





# punto C
pos = star_wars_tree_name.search('Yoda') #esta busqueda solo devuelve la posicion si lo encontro..
#por lo que aca hacemo un condicional para que si lo encontro (contiene una posicion) imprima la informacion 
if pos is not None: 
    print(f'search character {pos.value}, character info {pos.other_values}')

#aca hacemos lo mismo que el anterior pero para otro personaje 
pos = star_wars_tree_name.search('Boba Fett')
if pos is not None:#is not none, significa que lo encontro 
    print(f'search character {pos.value}, character info {pos.other_values}')

print()


# puntos d
star_wars_tree_name.in_order_height() #este barrido inorder esat en la clase arbol
print()

# punto e
star_wars_tree_name.in_order_weight() #tambien esta en la clase arbol 
# nombre_arbol.metodo()
print()

star_wars_tree_name.in_order()
print()


#en este barrdio primero muestra los id y despues los nombres 
star_wars_tree_id.in_order()
print('se cargo en el repo')