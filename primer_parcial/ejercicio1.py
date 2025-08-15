#Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
#  -funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
#  -funcion recursiva para listar los superheroes de la lista.

superheroes = ["Spider-Man", "Iron Man", "Capitan America", "Thor, Hulk", "Viuda Negra", "Doctor Strange",
    "Black Panther", "Ant-Man", "Bruja Escarlata", "Vision", "Hawkeye", "Wolverine", "Deadpool",
    "Capitan Marvel",
] #con los nombres ya esta bien 




def bus_bin_rec(array, value, first, last):
    if first >= last:
        return -1
    
    middle = (first + last) // 2
    if array[middle] == value:
        return middle
    elif array[middle] > value:
        return bus_bin_rec(array, value,first, last -1)
    else:
        return bus_bin_rec(array, value, first+1, last)
#podemos ordenar son el metodo
superheroes.sort()  
print("lista ordenada:")
print(superheroes)

#llamamos a la funcion y le pasamos los parametros
pos = bus_bin_rec(superheroes, "Capitan America", 0, len(superheroes)-1)
if pos != -1:
    print (f"Capitan America esta en la lista, en la posicion: {pos}")
else:
    print("Capitan America NO esta en la lista")



#  -funcion recursiva para listar los superheroes de la lista.
def listar_superheroes(array, index=0):
    if index == len(array):
        return
    print(array[index])
    listar_superheroes(array, index + 1)

print("lista de los superheroes:")
listar_superheroes(superheroes)