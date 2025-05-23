#10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;

# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

from queue_ import Queue_
from stack_ import Stack

#Carga de notificaciones: (hora, app, mensaje)
notificaciones = [
    ("11:30", "Facebook", "Hola!"),
    ("12:00", "Twitter", "Aprende Python con nosotros"),
    ("13:15", "Instagram", "Nueva foto"),
    ("14:00", "Twitter", "Python es genial"),
    ("15:50", "Facebook", "Evento hoy"),
    ("16:10", "Twitter", "Hola mundo"),
    ("12:30", "Twitter", "Python y datos"),
]

cola = Queue_()
for notif in notificaciones: #cargamos la cola 
    cola.arrive(notif)

# a. Eliminar todas las notificaciones de Facebook
def eliminar_facebook(cola):
    aux = Queue_()
    while cola.size() > 0: # miestras que al pila no este vacia 
        notif = cola.attention()
        if notif[1] != "Facebook": #guarda en una pila, todas las que no son 'facebook'
            aux.arrive(notif)
    #con while siguiente, vuelve a cargar la pila         
    while aux.size() > 0:
        cola.arrive(aux.attention())

# b. Mostrar notificaciones de Twitter con 'Python' sin perder datos
def mostrar_twitter_python(cola):
    aux = Queue_()
   
    while cola.size() > 0: 
        notif = cola.attention()
        if notif[1] == "Twitter" and "Python" in notif[2]:
            print(notif)
        aux.arrive(notif)
    while aux.size() > 0:
        cola.arrive(aux.attention())

# c. Pila para notificaciones entre 11:43 y 15:57, y contarlas
pila = Stack() #la necesito para guardar la determianr cuantas son .
def notificaciones_en_rango(cola, pila):
    aux = Queue_()
   
    def en_rango(hora): #hacemos una funcion para tener el valor de las horas que nos piden 
        #trabajamos directamente con la funcion 
        return "11:43" <= hora <= "15:57"
    while cola.size() > 0:
        notif = cola.attention()
        if en_rango(notif[0]):#es la pos en la que se ubican los horarios
            pila.push(notif)
        aux.arrive(notif) #para no perder el dato, los cargamos a la cola

    while aux.size() > 0:
        cola.arrive(aux.attention())
    

#Cada función usa una cola auxiliar para no perder datos

print("elimina las notificaciones de facebook")
eliminar_facebook(cola)
print("--------------------------------------------")

print("Muestra las notificaciones que contienen la palabra 'python': ")
mostrar_twitter_python(cola)
print("--------------------------------------------")

print("muestra la cantidad de notificaciones entre una hora determinada")
notificaciones_en_rango(cola, pila)
print(f"Cantidad de notificaciones entre 11:43 y 15:57: {pila.size()}")