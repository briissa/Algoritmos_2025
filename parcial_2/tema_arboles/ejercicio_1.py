# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) 
# de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool)
# para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:



# 1.los índices de cada uno de los árboles deben ser nombre, número y tipo;

# 2.mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, 
# es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;

# 3.mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;

# 4.realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;

# 5.mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;

# 6.mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;

# 7.determinar cuantos Pokémons tienen megaevolucion.

# 8.determinar cuantos Pokémons tiene forma gigamax.

from arbol import BinaryTree

pokemones = [
    {'nombre': 'Jolteon', 'numero': 135, 'tipo': ['electrico', 'fuego'], 'debilidad': ['agua'], 'megaevolucion': False, 'gigamax': True},
    {'nombre': 'Lycanroc', 'numero': 13, 'tipo': ['electrico', 'acero'], 'debilidad': ['tierra'], 'megaevolucion': False, 'gigamax': False},
    {'nombre': 'Tyrantrum', 'numero': 103, 'tipo': ['acero'], 'debilidad': ['tierra'], 'megaevolucion': True, 'gigamax': False},
    {'nombre': 'Tyran', 'numero': 193, 'tipo': ['fantasma'], 'debilidad': ['hielo'], 'megaevolucion': False, 'gigamax': True},
    {'nombre': 'Tylon', 'numero': 93, 'tipo': ['fantasma'], 'debilidad': ['hielo'], 'megaevolucion': False, 'gigamax': True},
    {'nombre': 'Pikachu', 'numero': 25, 'tipo': ['electrico'], 'debilidad': ['tierra'], 'megaevolucion': True, 'gigamax': False},
]
# del arbol se conoce su nombre, numero, tipo o tipos, debilidad frente a tipo/tipos, megaevolucion=true/false , gigamax= true/false  


by_nombre = BinaryTree() #el value de cada arbol es el que tiene como nombre y el resto de la info es other_value 
by_numero = BinaryTree()
by_tipo = BinaryTree()

#cargo cada uno de los arboles (value y other_values(no necesita especificar creo))
for poke in pokemones: 
    by_nombre.insert(poke['nombre'], poke)
    by_numero.insert(poke['numero'], poke)
    for tipo in poke ["tipo"]:
        by_tipo.insert(tipo, poke)


#by_nombre.in_order()

# 2.mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, 
# es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
print ('mostrar los datos del pokemon numero: 93')
pos = by_numero.search(93)
if pos is not None: 
    print(pos.other_values)


print()
print('mostrar los datos del pokemon con nombre: TY') #deberia de mostrar: tyran, tylon y tyrantum 
pos = by_nombre.proximity_search('Ty')
if pos is not None:
    print(pos.other_values)



print()
# 3.mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
print("pokemones de tipo fantasma: ")
by_tipo.tipo_in_order() 



print()
# 4.realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
print('listado por numero (ascendente):' )
by_numero.in_order_simple()

print()
print(' listado por nombre:')
by_nombre.in_order_simp()


print()
print('listado -por nivel- de nombres:')
by_nombre.by_level()



print()
# 5.mostrar todos los tipos??? que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
print("debilidades frente a jolteron, lycanroc y tyrantrum:")
by_nombre.in_order_tipo()




print()
# 6. Mostrar todos los tipos de Pokémons y cuántos hay de cada tipo

# Mostrar todos los tipos
print(" Todos los tipos de Pokémon:")
tipos_lista = by_tipo.mostrar_tipos()
for tipo in tipos_lista:
    print(tipo)

print()
# Contar cuántos hay de cada tipo
print(" Cantidad de Pokemon por tipo:")
tipos_cantidad = by_tipo.contar_tipos()
for tipo, cant in sorted(tipos_cantidad.items()):
    print(f"  {tipo}: {cant}")



print()
# 7.determinar cuantos Pokémons tienen megaevolucion.
print("los poke con megaevolucion son:" , by_nombre.megaevolucion())

print()
# 8.determinar cuantos Pokémons tiene forma gigamax.
print("los pokemones con gigamax son : ", by_nombre.gigamax())