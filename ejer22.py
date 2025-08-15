#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c. Utilizar un vector para representar la mochila.

def ordenar_burbuja(mochila): #antes de usar la busqueda, tenemos que ordenar (alfabeticamente)
    n = len(mochila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if mochila[j] > mochila[j + 1]:
                mochila[j], mochila[j + 1] = mochila[j + 1], mochila[j]


def usar_la_fuerza(mochila, buscado, inicio, fin, contador=0):
    if inicio > fin:
        return False, contador
    medio = (inicio + fin) // 2
    contador += 1
    if mochila[medio] == buscado:
        return True, contador
    elif mochila[medio] > buscado:
        return usar_la_fuerza(mochila, buscado, inicio, medio - 1, contador)
    else:
        return usar_la_fuerza(mochila, buscado, medio + 1, fin, contador)


#en este caso, la mochila es un vector de string
mochila = [ "agua", "gorra", "casa", "abrigo", "comida", "sable de luz"]
buscado = "sable de luz"

#llamamos para ordenar la mochila, antes de la busqueda
ordenar_burbuja(mochila)

# Llamada a la función de búsqueda binaria
encontrado, comparaciones = usar_la_fuerza(mochila, buscado, 0, len(mochila) - 1)
#la busqueda solo devuelve un booleano que se lo asigna a 'encontrado' y un contador que se lo asigna a'comparaciones'


#mostramos fuera de la funcion
print("Mochila ordenada:", mochila)
if encontrado:
    print(f"El sable de luz fue encontrado después de {comparaciones} comparaciones.")
else:
    print("El sable de luz no está en la mochila.")