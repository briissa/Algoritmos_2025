# 22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
# actividades enumeradas a continuación:

# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

from list_ import List 

jedi_data = [
    {
        "nombre" : "Yoda",
        "maestro": None,
        "color_sable": "amarillo",
        "especie": "humano"
    },
    {
        "nombre" : "Ahsoka Tano",
        "maestro": "Yoda",
        "color_sable": "azul y negro ",
        "especie": "humano"
    },
    {
       "nombre" : "Luke Skywalker",
        "maestro": "Qui-Gon Jin",
        "color_sable": "blanco y azul",
        "especie": "twi'lek" 
    },
    {
       "nombre" : "Kit Fisto",
        "maestro": "Luke Skywalker",
        "color_sable": "violeta",
        "especie": "twi'lek" 
    },
    {
       "nombre" : "Qui-Gon Jin",
        "maestro": None,
        "color_sable": "negro",
        "especie": "trelek" 
    },
    {
        "nombre" : "Mace Windu",
        "maestro": "Kit Fito",
        "color_sable": "amarillo",
        "especie": "humano"
    }
]

class jedis :
    def __init__(self, nombre, maestro, color_sable, especie):
        self.nombre = nombre
        self.maestro = maestro
        self.color_sable = color_sable
        self.especie = especie 

    def __str__(self):
        return f'{self.nombre}, su especie es:{self.especie}'
    #mostramos lo que queremos ver en pantalla (que nos sirva)

#creamos la lista 
list_jedi = List()

#cargamos la lista 
for jed in jedi_data: #saco los datos de la lista y los guardo en la clase que cree 
    jedi = jedis (
        nombre = jed ["nombre"],
        maestro = jed ["maestro"],
        color_sable = jed ["color_sable"],
        especie = jed ["especie"],
    )
    list_jedi.append(jedi)

print("---------------")


#lo defino para el punto a (ordeno por nombre)
def ordenar_nombre(item):
    return item.nombre

list_jedi.add_criterion("nombre", ordenar_nombre) #le paso el criterio a la funcion
list_jedi.sort_by_criterion("nombre")
list_jedi.show()

# print()
# #lo defino para el a (ordeno por especie)
# def ordenr_especie (item):
#     return item.especie 

# list_jedi.add_criterion('especie', ordenr_especie)
# list_jedi.sort_by_criterion("especie")
# list_jedi.show()







# b. mostrar toda la información de Ahsoka Tano y Kit Fisto
for nombre in ["Ahsoka Tano", "Kit Fisto"]: #recorre la lista que contiene esos nombres
    pos = list_jedi.search(nombre, "nombre") #dentro de la lista busca el nombre para luego pasar la pos donde esta toda la info.
    print("informacion de Ahsoka Tano y Kit Fisto:")
    if pos is not None:
        print(vars(list_jedi[pos]))  # 'vars()' Muestra todos los atributos del objeto



print("------Punto c-------")
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
for maestro in ["Yoda", "Luke Skywalker"]: #cree una tupla con los nombres de maestros 
    print(f'Padawans de {maestro}:')
    for jedi in list_jedi:
        if jedi.maestro == maestro: #jedi.atributo es igual al maestro que busco, entonces..
            print(jedi.nombre)



print("--------Punto d-------")
# d. mostrar los Jedi de especie humana y twi'lek;
for especie in ["humano", "twi'lek"]:
    print(f'jedi de especie->{especie}:')
    for jedi in list_jedi:
        if jedi.especie == especie:
            print(jedi.nombre) #elijo mostrar el nombre


print("-----Punto e-------")
# e. listar todos los Jedi que comienzan con A;
print("Lista de los Superheroes que comienzan con A -->")
for jedi in list_jedi:
    if jedi.nombre.startswith(("A")):
        print (jedi)



print("-------Punto f----")
# f. mostrar los Jedi que usaron sable de luz de más de un color;
for jedi in list_jedi:
    if len (jedi.color_sable.split())> 1: #split cuenta por palabras y si es mayor a 1, es xq tiene dos colores
        print(f' jedi con + de un color: {jedi.nombre}, los colores son: {jedi.color_sable}') 



print ("--------Punto g -----")
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
for jedi in list_jedi:
    if jedi.color_sable in ["amarillo", "violeta"]:
        print (f'jedi con sable de color: {jedi.color_sable}, es: {jedi.nombre}')



print("-------Punto h-----")
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
for maestro in ["Qui-Gon Jin" , "Mace Windu"]:
    print (f'padawans de {maestro}:')
    for jedi in list_jedi:
        if jedi.maestro == maestro:
            print(f' {jedi.nombre}')
else :
    print(f'{maestro}-no tuvo padawans')