# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como 
# posición uno la cima de la pila;

# b. determinar los personajes que participaron en más de 5 películas de la saga, 
# además indicar la cantidad de películas en la que aparece;

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.


from stack import Stack

lista_personajes = [
    {"nombre": "Tony Stark - Iron Man", "peliculas": 10},
    {"nombre": "Steve Rogers - Captain America", "peliculas": 9},
    {"nombre": "Thor", "peliculas": 8},
    {"nombre": "Natasha Romanoff - Black Widow", "peliculas": 8},
    {"nombre": "Bruce Banner - Hulk", "peliculas": 7},
    {"nombre": "Clint Barton - Hawkeye", "peliculas": 6},
    {"nombre": "Peter Parker - Spider-Man", "peliculas": 6},
    {"nombre": "Stephen Strange - Doctor Strange", "peliculas": 4},
    {"nombre": "T'Challa - Black Panther", "peliculas": 4},
    {"nombre": "Scott Lang - Ant-Man", "peliculas": 5},
    {"nombre": "Wanda Maximoff - Scarlet Witch", "peliculas": 6},
    {"nombre": "Vision", "peliculas": 4},
    {"nombre": "Sam Wilson - Falcon", "peliculas": 5},
    {"nombre": "Bucky Barnes - Winter Soldier", "peliculas": 5},
    {"nombre": "Loki", "peliculas": 6},
    {"nombre": "Rocket Raccoon", "peliculas": 5},
    {"nombre": "Groot", "peliculas": 5}
]

pila_personajes = Stack()

for personaje in lista_personajes:
    pila_personajes.push(personaje)

print("- Personajes de Marvel Cinematic Universe - ")
pila_personajes.show() # mostramos los elementos de la pila
print("-----------------------------------------")

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
personajes_buscados = ["Rocket Raccoon", "Groot"]
posicion = {nombre : None for nombre in personajes_buscados}  #crea un diccionario llamado posicion donde las claves son los nombres de los personajes que estás buscando ("Rocket Raccoon" y "Groot"), y el valor inicial para cada clave es None.
#Esto se usa para guardar la posición en la pila de cada personaje buscado. Cuando encuentres a uno de esos personajes, actualizarás el valor None por la posición correspondiente.
pos_actual = 1
pila_aux = Stack()

while pila_personajes.size() > 0:
    personaje = pila_personajes.pop()
    if personaje["nombre"] in personajes_buscados:
        posicion[personaje["nombre"]] = pos_actual
    pila_aux.push(personaje)
    pos_actual += 1


#cada que hacemos un ejercicio, volvemos a cargar la pila original
while pila_aux.size() > 0:
    pila_personajes.push(pila_aux.pop())

print("PUNTO A")
for nombre, posicion in posicion.items():
    if posicion is not None:
        print(f"[ {nombre} se encuentra en la posicion {posicion} ]")
    else:
        print(f"[ {nombre} no se encuentra en la pila ]")
print("-----------------------------------------")

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece; 
pila_aux_2 = Stack()
pila_personajes_5 = Stack()
cant_peliculas = 0

while pila_personajes.size() > 0:
    personaje = pila_personajes.pop()
    if personaje["peliculas"] > 5:
        pila_personajes_5.push(personaje)
        cant_peliculas += 1
    pila_aux_2.push(personaje)

while pila_aux_2.size() > 0:
    pila_personajes.push(pila_aux_2.pop())

print("PUNTO B")
print(f"[ Personajes que participaron en más de 5 peliculas: {cant_peliculas} ]")
print("Personajes:")
pila_personajes_5.show() # mostramos los elementos de la pila
print("-----------------------------------------")

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow); 
pila_aux_3 = Stack()
pila_blackw = Stack()

while pila_personajes.size() > 0:
    personaje = pila_personajes.pop()
    if personaje["nombre"] == "Natasha Romanoff - Black Widow":
        pila_blackw.push(personaje)
    pila_aux_3.push(personaje)

while pila_aux_3.size() > 0:
    pila_personajes.push(pila_aux_3.pop())

print("PUNTO C")
print("Personaje:")
pila_blackw.show() # mostramos los elementos de la pila
print("-----------------------------------------")

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
pila_aux_4 = Stack()
pila_personajes_cdg = Stack()

while pila_personajes.size() > 0:
    personaje = pila_personajes.pop()
    if personaje["nombre"].startswith(("C", "D", "G")): #es una función de las cadenas de texto (strings) en Python. Sirve para verificar si una cadena comienza con uno o varios caracteres específicos.
        pila_personajes_cdg.push(personaje)
    pila_aux_4.push(personaje)

while pila_aux_4.size() > 0:
    pila_personajes.push(pila_aux_4.pop())

print("PUNTO D")
print("Personajes:")
pila_personajes_cdg.show() # mostramos los elementos de la pila
print("-----------------------------------------")