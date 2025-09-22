# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:


# a. eliminar el nodo que contiene la información de Groot;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra w, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.


from list_ import List
from super_heroesTP6 import superheroes6 #esto nos sirve para usar la list de supeprheroes que tenemos..


#lista Principal
class Superhero:
    
    def __init__(self, name, house_comic, short_bio, first_appearance, is_villain):
        self.name = name
        self.house_comic = house_comic
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

     
    #Lo que nos va a mostrar en consola es lo siguiente: (cuando hagamos un print)
    #        - le podemos poner lo que nosotros queramos 
    def __str__(self):
        return f"{self.name} -- {self.house_comic}"
    #solo lo que vamos a mostrar porque a algunas solo las vamos a usar sin necesariamente mostrarlas.



list_superhero = List() #creamos una lista


def order_by_name(item):  #necestamos de esta funcion para poder borrar por medio de (name)
    return item.name

def order_by_year(item):  #ordenamos y despues buscamos.
    return item.year

def order_by_is_villain (item):
    return item.is_villan


list_superhero.add_criterion('name', order_by_name) #aca le asignamos la key 'name' y la funcion que va a usar.
list_superhero.add_criterion('first_appearance', order_by_year)
list_superhero.add_criterion('is_villain', order_by_is_villain)


#vamos a cargar toda la data en nuestra lista:
for superhero in superheroes6:#recorremos la lista de diccionarios que tenemos en super_heoresTP6
    hero = Superhero(  #crea una clase ?                    //¿porque lo transformamos a clase?
        #le pasamos cada uno de sus atributos:            //porque nosotros armamos la estructura de la clase lista 
        name=superhero["name"],
        house_comic= superhero["house_comic"],                       # // para trabajar con los objetos.. Y esta es la forma general que se debe de hacer.
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    list_superhero.append(hero) #cargamos todo a la lista con un append y llamando a la clase 'Superhero'.
print("--------")



#A- eliminar a Groot 
list_superhero.delete_value('Groot', 'name') #delete_value ('que es lo que quiero a eliminar', 'el atributo mediante el cual lo voy a eliminar')
print("se elimino a Groot:")
print()
list_superhero.show()



print("---- Punto b -----")
#B- mostrar año aparicion wolverine
pos = list_superhero.search('Wolverine', 'name') #para el momento de la busqueda es cunado lo va a ordenar la lista en relacion a los nombres con def order_by_name

if pos is not None:
    print(f'Wolverin aparecio en: {list_superhero[pos].first_appearance}')
else: 
    print('el superheroe no esta en la lista')



print()
print("-----Punto c ----")
#C- modificar Dr strage de villano a heroe
pos = list_superhero.search('Dr. Strange', 'name')

if pos is not None:
    print(f'{list_superhero[pos].name} es : {list_superhero[pos].is_villain} (villano)') #muestro antes
    list_superhero[pos].is_villain = False #al asignarle falso, al villano lo cambiamos a heroe
    print(f'{list_superhero[pos].name} ahora es: {list_superhero[pos].is_villain} (heroe)') #muestro despues 
else:
    print('el superheroe no esta en la lista')



print()
#D-mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura” (el profe los puso en ingles)
print("----Punto d-----")
print('--> superheroes con traje o armadura: ')
for superhero in list_superhero: #recorremos la lista de superheroes
    if 'armor' in superhero.short_bio or 'suit' in superhero.short_bio:
        print(superhero.name) #muestro solo el nombre



print()
print("-------Punto e-------")
#E. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
print(" --> Los Superheroes con aparicion anterior a 1963:")
for hero in list_superhero:
    if hero.first_appearance < 1963:
        print(f"{hero.name}, aparicion en :{hero.first_appearance}")
print('--------------------')



print()
print("-------Punto f------")
#f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print ("Casa de Capitana Marvel y Mujer Maravilla: ")
for hero in list_superhero:
    if hero.name in ['Capitana Marvel', 'Mujer Maravilla']:
        print(f'{hero.name}- casa : {hero.house_comic}')



print()
print("-------Punto g------")
#g. mostrar toda la información de Flash y Star-Lord;
for hero in list_superhero:
    if hero.name in ['Flash', 'Star-Lord']:
        print (f'Toda la informacion de {hero.name}:')
        print (vars(hero))
        print('---------')





print()
#H. listar los superhéroes que comienzan con la letra w, M y S;
print("------Punto h----")
print("lista de superheroes que comienzan con W, M y S:")
for superhero in list_superhero: #recorremos la lista de superheroes
    if superhero.name.lower().startswith(('w', 'm', 's')): # lower para que no importe si es mayuscula o minuscula 
        print(superhero.name)                              # startswith para que busque cual es la letra con ls que empieza la cadena




print("------Punto i ------")
# i. determinar cuántos superhéroes hay de cada casa de comic.
casa_marvel = 0 
casa_DC = 0 
for hero in list_superhero:
    if hero.house_comic == 'Marvel':
        casa_marvel += 1
    elif hero.house_comic == 'DC':
        casa_DC += 1

print(f'cantidad de superheroes de Marvel: {casa_marvel}')
print(f'cantidad de superheroes de DC: {casa_DC}')



    

    
