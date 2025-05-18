#13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
# verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido)

#   resolver las siguientes actividades:
# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
# además mostrar el nombre de dichas películas; 

# b. mostrar los modelos que quedaron dañados, sin perder información de la pila.

# c. eliminar los modelos de los trajes destruidos mostrando su nombre;
# d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
# más de un modelo de traje, estos deben cargarse por separado; (no entendi esto)
# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
# repetidos en una misma película.
# f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
# “Capitan America: Civil War”.

from stack import Stack
 
#creamos la pila
mi_pila = Stack()


#cargamos la pila manualmente (modelo, pelicula, estado)
mi_pila.push(("Mark XLIV (Hulkbuster)", "Avengers: Age of Ultron", "dañado"))
mi_pila.push(("Mark III", "Iron Man", "impecable"))
mi_pila.push(("Mark XLII", "Iron Man 3", "destruido"))
mi_pila.push(("Mark XLIV (Hulkbuster)", "Avengers: Endgame", "dañado"))
mi_pila.push(("Mark L", "Avengers: Infinity War", "impecable"))
print("la pila original es:")
mi_pila.show()

pila_auxiliar = Stack()
while mi_pila.size() > 0: #en los siguiente ejercicios trabajo con la pila auxiliar (menos en el b)
    pila_auxiliar.push(mi_pila.pop())

# Buscar el modelo Mark XLIV (Hulkbuster)
peliculas_hulkbuster = [] #lo incializo como lista vacia

while pila_auxiliar.size() > 0:
    modelo = pila_auxiliar.pop()
    mi_pila.push(modelo) #uso la pila aux pero vuelvo a cargar la pila orginal xq me habia quedado vacia

    # Verificar si el modelo es Mark XLIV (Hulkbuster)
    if modelo[0] == "Mark XLIV (Hulkbuster)":
        peliculas_hulkbuster.append(modelo[1])  # Guardar el nombre de la película
        #tener en cuenta la sposiciones en las que estan lso datos en la lista

#mostrar las pelis en las que se uso el modelo
if len (peliculas_hulkbuster) > 0: #si la lista contiene un elemnto, se ejecuta el if, sino no se ejecuta
    print("El modelo (Hulkbuster) fue utilizado en las siguientes películas:")
    for pelicula in peliculas_hulkbuster:
        print(f"- {pelicula}") #con f' imprimimos un string, y con {pelicula} le indicamos que tiene que imprimir el valor de esa variable
else:
    print("El modelo (Hulkbuster) no fue utilizado en ninguna película.")



#b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
pila_aux = Stack() #para no perder datos y luego devolverlos a la original
modelos_dañados = [] #lista para guardar los modelos dañados

while mi_pila.size() > 0:
    modelo_da = mi_pila.pop()
    
    if modelo_da[2] == "dañado":
        # print(f"-Modelo dañado encontrado: {modelo_da[0]}")
        modelos_dañados.append(modelo_da[0])
    
    pila_aux.push(modelo_da)#los cargamos a la pila aux

if len (modelos_dañados) > 0:
    print("los modelos son:") ##lo ponemos si queremos
    for mostr_da in modelos_dañados: #En cada iteración, la variable modelo toma el valor de un elemento de la lista.
        #por que siempre se dede se sacar de a un elemento de la lista
        print(f"-modelo dañado encontrado: {mostr_da}")
else:
    print(" no hay modelos dañados")

#devolvemso los datos a la pila original 
while pila_aux.size ()> 0:
    mi_pila.push(pila_aux.pop())







# c. eliminar los modelos de los trajes destruidos mostrando su nombre.
pila_auxi = Stack() #para guardr lo que no tiene como estado 'destruido'

while mi_pila.size() > 0:
    peli = mi_pila.pop() # dentro de pelicula esta (mdelo, pelicula, estado)
    pila_auxi.push(peli) #vuelvo a cargar la pila original
    if peli [2] == "destruido":
        print(f'-el modelo eliminado por estar (destruido) es": {peli[0]}') #muestro el nombre del traje
    
    
# print("la pila con los 'destruidos' eliminados es:")
# pila_auxi.show()
while pila_auxi.size() > 0:
    mi_pila.push(pila_auxi.pop())
#caca debo devolver lo de la pila aux a la original


#HASTA ACA ANDA




#e. agregar el modelo Mark LXXXV a la pila, teniendo en cuenta que no se pueden cargar modelos repetidos en una misma película.

# Crear una pila auxiliar para verificar si el modelo ya existe en la película
pila_aux2 = Stack()
modelo_a_agregar = ("Mark LXXXV", "Avengers: Endgame", "Impecable")
modelo_ya_existe = False

# Verificar si el modelo ya existe en la misma película
while mi_pila.size() > 0:
    modelo_1 = mi_pila.pop()
    pila_aux2.push(modelo_1)  # Guardar en la pila auxiliar para no perder datos

    # Verificar si el modelo y la película coinciden
    if modelo_1[0] == modelo_a_agregar[0] and modelo_1[1] == modelo_a_agregar[1]:
        modelo_ya_existe = True

# Restaurar la pila original
while pila_aux2.size() > 0:
    mi_pila.push(pila_aux2.pop())

# Agregar el modelo si no existe
if not modelo_ya_existe:
    mi_pila.push(modelo_a_agregar) #aca agregamos el modelo 
    print(f"El modelo {modelo_a_agregar[0]} fue agregado a la pila.")
else:
    print(f"El modelo {modelo_a_agregar[0]} ya existe en la película {modelo_a_agregar[1]} y no se agregó.")

# Mostrar la pila actualizada
print("\nPila actualizada:")
mi_pila.show()




#f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
# “Capitan America: Civil War”.


# Crear una pila auxiliar para no perder los datos
pila_aux = Stack()

# Listas para guardar los nombres de los trajes utilizados en las películas específicas
trajes_spiderman = []
trajes_capitan_america = []

while mi_pila.size() > 0:
    traje = mi_pila.pop()
    pila_aux.push(traje)  # Guardar en la pila auxiliar para no perder datos

    # Verificar si el traje pertenece a las películas indicadas
    if traje[1] == "Spider-Man: Homecoming":
        trajes_spiderman.append(traje[0])
    elif traje[1] == "Capitan America: Civil War":
        trajes_capitan_america.append(traje[0])

# Restaurar la pila original
while pila_aux.size() > 0:
    mi_pila.push(pila_aux.pop())

# Mostrar los resultados
print("\nTrajes utilizados en 'Spider-Man: Homecoming':")
if trajes_spiderman:
    for traje in trajes_spiderman:
        print(f"- {traje}")
else:
    print("No se encontraron trajes utilizados en 'Spider-Man: Homecoming'.")

print("\nTrajes utilizados en 'Capitan America: Civil War':")
if trajes_capitan_america:
    for traje in trajes_capitan_america:
        print(f"- {traje}")
else:
    print("No se encontraron trajes utilizados en 'Capitan America: Civil War'.")





#DATOS IMPORTANTES:
#\n es un carácter especial en Python que representa un salto de línea

# ---muy importante---
#  de la pila_original le paso todo a la pila_aux (para hacer el punto con la pila aux)
#  Pero antes de perder los datos por completo de la pila_aux (o solo quedarme con los datos que pide el punto)
#  se los devuelvo a la pila_original
