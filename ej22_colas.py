# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, 
# etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

from queue_ import Queue_


#(nombre-personaje, nombre-superheroe, genero) (genero M o F)
personajes = [
    ("Tony Stark", "Iron Man", "M"),
    ("Steve Rogers", "Capitán América", "M"),
    ("Natasha Romanoff", "Black Widow", "F"),
    ("Carola Ducter", "Capitana Marvel", "F"),
    ("Joules", "Dakar", "M"),
    ("Scott Lang", "Hombre Hormiga", "M"),
]

mi_cola =  Queue_()

for persona in personajes: #cargo la cola
    mi_cola.arrive(persona)

cola_aux = Queue_() #cola aux
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
while mi_cola.size() > 0:
    nombre = mi_cola.attention()
    cola_aux.arrive(nombre)
    if nombre[1] == "Capitana Marvel":
        print(f"el nombre de CAapitana Marvel es {nombre[0]}") #a la variable nombre no necesito definirla antes, solo la uso ahi mismo

#volver a cargar la pila 
while cola_aux.size() > 0:
    mi_cola.arrive(cola_aux.attention())

# b. mostrar los nombre de los superhéroes femeninos.
cola_femeninos = Queue_()
while mi_cola.size() > 0:
    nombre = mi_cola.attention()
    cola_aux.arrive(nombre)
    if nombre[2] == "F":
        cola_femeninos.arrive(nombre)
print("------------------")
print("superheroes femeninos:")
cola_femeninos.show()

#volver a cargar la pila 
while cola_aux.size() > 0:
    mi_cola.arrive(cola_aux.attention())


        
# b. mostrar los nombre de los superhéroes masculinos.
cola_masculinos = Queue_()
while mi_cola.size() > 0:
    nombre = mi_cola.attention()
    cola_aux.arrive(nombre)
    if nombre[2] == "M":
        cola_masculinos.arrive(nombre)
print("------------------")
print("superheroes masculinos:")
cola_masculinos.show()
print("------------------")

#volver a cargar la pila 
while cola_aux.size() > 0:
    mi_cola.arrive(cola_aux.attention())
    
# d. determinar el nombre del superhéroe del personaje Scott Lang.
while mi_cola.size() > 0:
    nombre = mi_cola.attention()
    cola_aux.arrive(nombre)
    if nombre[0] == "Scott Lang":
        print(f"el nombre de CAapitana Marvel es {nombre[1]}")
print("------------------")
#volver a cargar la pila 
while cola_aux.size() > 0:
    mi_cola.arrive(cola_aux.attention())



#e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;

while mi_cola.size() > 0:
    nombre = mi_cola.attention()
    cola_aux.arrive(nombre)
    # nombre[0] es el nombre del personaje, nombre[1] es el nombre del superhéroe
    if nombre[0].startswith("S") or nombre[1].startswith("S"): # .startswith() verifica si una cadena comienza con un texto específico.
        print(f"Datos de personas con S: {nombre}") #no indicamos la psicion, porque queremos mostrar todo

# Volver a cargar la cola original
while cola_aux.size() > 0:
    mi_cola.arrive(cola_aux.attention())

    

# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
encontrado = False
while mi_cola.size() > 0:
    nombre = mi_cola.attention()
    cola_aux.arrive(nombre)
    if nombre[0] == "Carol Danvers":
        print(f"Carol Danvers está en la cola y su nombre de superhéroe es: {nombre[1]}")
        encontrado = True

if not encontrado:
    print("Carol Danvers no se encuentra en la cola.")

