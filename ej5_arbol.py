# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;

# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
#               I. determinar cuántos nodos tiene cada árbol;
#               II. realizar un barrido ordenado alfabéticamente de cada árbol.



superheroes = [
    {"name": "Capitana Marvel", "is_villain": False},
    {"name": "Hulk","is_villain": False},
    {"name": "Groot","is_villain": True},
    {"name": "Iron Man","is_villain": True},
    {"name": "Dr. Strange","is_villain": True},
    { "name": "Wolverine", "is_villain": False},
    {"name": "Flash","is_villain": True},
]    

from arbol import BinaryTree

arbol_super = BinaryTree()

#cargamos el arbol 
for hero in superheroes:
    arbol_super.insert(hero["name"], hero ["is_villain"]) #guardamos los dos datos(1.values y 2.other_values)
#para algunos ejercicos no necesito hacer ['is_villain'] poruqe no lo estoy cargando como un diccionario, ademas es el unico valor de other_values 

print('---punto b-----' )
#Ordeno los villanos alfabeticamente (esta modificado en la clase base)
arbol_super.is_villain_in_order()

print()
print("-----punto c----")
#muestro superheroe con 'c' 
arbol_super.super_in_order()


print()
print("-----punto d----")
total = arbol_super.contar_heroes()
print(f"la cantidad de heroes es: {total}")

print()  
#Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre; 
print("----punto e----")

# Buscamos por prefijo 'Dr' (proximidad)
pos = arbol_super.proximity_busqueda('Dr')
if pos is not None:
    print('Encontrado (por proximidad):', pos.value)

    # eliminamos el nodo encontrado y reinsertamos con el nombre corregido
    deleted_value, deleted_other = arbol_super.delete(pos.value)
    
    if deleted_value is not None:
        # Asumimos que other_values fue guardado como booleano (is_villain)
        arbol_super.insert('Doctor Strange', deleted_other)
        print('Nombre corregido a: Doctor Strange')
    else:
        print('No se pudo eliminar el nodo encontrado')


print()
print("----punto f ----")
#ordenamos de manera descendiente los superheroes
arbol_super.in_order_des()


print()
print("--punto g---")
arbol_h = BinaryTree()# un arbol para superheroes
arbol_v = BinaryTree() #  un arbol para villanos 

arbol_super.divide_arbol(arbol_h, arbol_v) 
print("arbol de heroes:")
arbol_h.in_order()
print()
print("arbol de villanos:")
arbol_v.in_order()
print()

#  II. realizar un barrido ordenado alfabéticamente de cada árbol.
print("heroes ordenados alfabeticamente:")
arbol_v.in_order()
print()
print("villanos ordenados alfabeticamente:")
arbol_v.in_order()
print()

#I. determinar cuántos nodos tiene cada árbol;
print("determinar cuantos nodos hay en cada arbol")

hero = arbol_h.contar_heroes()
print(f"cantidad dde heroes: {hero}")
print()

villan = arbol_v.contar_villain()
print(f'cantidad de villanos: {villan}')