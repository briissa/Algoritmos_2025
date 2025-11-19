# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
# es la distancia entre los ambientes, se debe cargar en metros;

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

from graph import Graph

#creamos la lista de ambientes que luego vamos a cargar en el grafo (aristas) 
ambientes = [
    "Cocina", "Comedor", "Cochera", "Quincho",
    "Baño 1", "Baño 2", "Habitacion 1", "Habitacion 2",
    "Sala de estar", "Terraza", "Patio"
]

grafo = Graph(is_directed=True) #para que sea no dirigido 

#cargamos el grafo 
for var in ambientes:
    grafo.insert_vertex(var)


#creamos las aristas (inicio, final, peso) 
"""puedo empezar por cualquier vertice (cocina, comedor, etc ), lo importante es que haya 3 conexiones distintas (aristas)"""
grafo.insert_edge("Cocina", "Comedor", 2)
grafo.insert_edge("Cocina", "Sala de estar", 4)
grafo.insert_edge("Cocina", "Patio", 6)
grafo.insert_edge("Cocina", "Terraza", 5)
grafo.insert_edge("Cocina", "Baño 1", 3)       # Cocina: 5
grafo.insert_edge("Comedor", "Cochera", 3)
grafo.insert_edge("Comedor", "Quincho", 3)    # Comedor: 4
grafo.insert_edge("Quincho", "Terraza", 6)
grafo.insert_edge("Quincho", "Patio", 3)               #patio: 4
grafo.insert_edge("Quincho", "Sala de estar", 7)
grafo.insert_edge("Quincho", "Cochera", 7)           # Quincho: 5
grafo.insert_edge("Patio", "Cochera", 4)            # Cochera: 3
grafo.insert_edge("Sala de estar", "Habitacion 1", 2)
grafo.insert_edge("Baño 1", "Sala de estar", 4)      # Baño 1: 3
grafo.insert_edge("Baño 2", "Habitacion 2", 2)
grafo.insert_edge("Baño 2", "Sala de estar", 5)    #sala de estar:7 
grafo.insert_edge("Baño 2", "Baño 1", 3)             # Baño 2: 3
grafo.insert_edge("Habitacion 1", "Sala de estar", 3)
grafo.insert_edge("Habitacion 1", "Habitacion 2", 4) # Hab. 1: 3
grafo.insert_edge("Habitacion 2", "Sala de estar", 4)      # Hab. 2: 4
grafo.insert_edge("Terraza", "Patio", 2)             # Terraza: 4
grafo.insert_edge("Baño 1", "Habitacion 1", 2)


# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;

print("arbol de expansion minima: ")
expansion_tree = grafo.kruskal("Cocina") #usamos cualquier vertice como origen 
#este retorna un solo valor 

total_peso = 0 
for edge in expansion_tree.split(';'):   # split separa 
    if edge.count('-') == 2 : #verifica qeu la arista tenga origen, destino y peso (osea que tenga 2 guiones-->  "origen-destino-peso")
        origen , destino, peso = edge.split('-')
        print(f"{origen} - {destino}: {peso}")
        total_peso += int(peso)
print(f"Total metros de cable necesarios: {total_peso}")



# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

print("Camino mas corto de Hab. 1 hasta la Sala de estar:")

path = grafo.dijkstra("Habitacion 1")  #stack con resultadps
# path contiene: 
# [["Habitacion 1", 0, None], ["Sala de estar", 3, "Habitacion 1"], ...]

destination = "Sala de estar"
peso_total = None
camino = []

while path.size() > 0:
    value = path.pop()
    if value[0] == destination: # si el nodo actual es el destino 
        if peso_total is None:
            peso_total = value[1]
        camino.append(value[0])
        destination = value[2]
camino.reverse()
print(f'el camino mas corto es: {"-".join(camino)} - la cantidad de metros de cable necesarios es {peso_total}') 
#join contruye todo a un unico string 



# Dijkstra calcula el camino más corto desde un origen hacia TODOS los nodos y guarda esa información en el stack.
# despues hacemos: 
# Desapilar (pop) todos los elementos.
# Buscar el nodo destino.
# Reconstruir el camino usando el campo nodo_previo.