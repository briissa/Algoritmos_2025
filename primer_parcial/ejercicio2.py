"""Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
    1.Listado ordenado de manera ascendente por nombre de los personajes.
    2.Determinar en que posicion esta The Thing y Rocket Raccoon.
    3.Listar todos los villanos de la lista.
    4.Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
    5.Listar los superheores que comienzan con  Bl, G, My, y W.
    6.Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
    7.Listado de superheroes ordenados por fecha de aparación.
    8.Modificar el nombre real de Ant Man a Scott Lang.
    9.Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
    10.Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
"""
from list_ import List
from super_heroes_data import superheroes
from queue_  import Queue_

class Superhero :
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain
    
    def __str__ (self):
        return f"{self.name}, su nombre real es: {self.real_name}"
    #solo mostramos lo que necesitamos.

#creamos la lista
list_superhero = List()
#creamos la cola para el punto 4 
mi_cola = Queue_()

#cargamos la lista 
for super in superheroes:
    heroe = Superhero (
        name = super ["name"],
        alias = super ["alias"],
        real_name = super ["real_name"],
        short_bio = super ["short_bio"],
        first_appearance = super ["first_appearance"],
        is_villain = super ["is_villain"],
    )
    list_superhero.append(heroe)


#la uso para el punto 1
def ordenar_por_nombre(item):
    return item.name

list_superhero.add_criterion("name", ordenar_por_nombre)


#la uso para el punto 6.
def ordenar_por_nombreReal(item):
    return item.real_name

list_superhero.add_criterion("real_name", ordenar_por_nombreReal)

#la uso par el punto 7
def ordenar_por_fecha(item):
    return item.first_appearance

list_superhero.add_criterion("first_appearance", ordenar_por_fecha)



#1.Listado ordenado de manera ascendente por nombre de los personajes.
list_superhero.sort_by_criterion("name")
print("Listado ordenado por nombre de los personajes:")
list_superhero.show()  
print("-----------")



#2.Determinar en que posicion esta The Thing y Rocket Raccoon.
pos_thing = list_superhero.search("The Thing", "name")
if pos_thing is not None:
    print(f"The Thing se encuentra en la posicion: {pos_thing}")
print("------")

pos_roc = list_superhero.search("Rocket Raccoon", "name")
if pos_roc is not None:
    print(f"Rocket Raccoon se encuentra en la posicion: {pos_roc}")
print("------")


#3.Listar todos los villanos de la lista.
print("Listado de todos los villanos:")
for super in list_superhero:
    if super.is_villain == True :
        print(super)
        mi_cola.arrive(super)
print("------")
print("La cola con los villanos:")
mi_cola.show()
print("------")


# 4.Poner todos los villanos en una cola para determinar luego 
# cuales aparecieron antes de 1980.

cola_aux = Queue_()

while mi_cola.size() > 0:
    villano = mi_cola.attention()
    if villano.first_appearance < 1980:
        cola_aux.arrive(villano)       
print("los villanos que aparecieron antes de 1980:")
cola_aux.show()
print("---------")


# 5.Listar los superheores que comienzan con  Bl, G, My, y W.
print("Lista de los Superheroes que comienzan con: ( Bl, G, My, W)-->")
for super in list_superhero:
    if super.name.startswith(("Bl", "G", "My", "W")):
        print (super)
print("--------")



#6.Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
list_superhero.sort_by_criterion("real_name")
print("Listado ordenado por nombre real de los personajes:")
list_superhero.show()
print("-----------")



#7.Listado de superheroes ordenados por fecha de aparación.
list_superhero.sort_by_criterion("first_appearance")
print("Listado ordenado por fecha de aparicion de los personajes:")
list_superhero.show()
print("-----------")


# 8.Modificar el nombre real de Ant Man a Scott Lang.
pos = list_superhero.search("Ant Man", "name") #lo buscamos por name y luego cambiamos por real_name
if pos is not None:
    print(list_superhero[pos])
    print("su nombre real fue cambiado:")
    hero = list_superhero[pos]
    hero.real_name = "Scott Lang"
    print(list_superhero[pos])
print("----------------")





#9.Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
print("super que incluyen en su biografia la palabra time-traveling o suit: ")
encontro = False
for super in list_superhero: #recorremos la lista de superheroes
    if 'trime-traveling' in super.short_bio or 'suit' in super.short_bio: #si la palabra esta incluida en la bio
        print(f"{super}")
        encontro = True
if not encontro:
    print("Ningun personaje contiene en su Bio esa palabras")


# 10.Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
eliminado_electro = list_superhero.delete_value('Electro', 'name')
if eliminado_electro is not None:
    print(f"Se elimino a: {eliminado_electro}")
else:
    print("Electro no estaba en la lista.")

eliminado_zemo = list_superhero.delete_value('Baron Zemo', 'name')
if eliminado_zemo is not None:
    print(f"Se elimino a: {eliminado_zemo}")
else:
    print("Baron Zemo no estaba en la lista.")



