from typing import Any, Optional
from queue_ import Queue_
from stack import Stack 
from heap import HeapMin
from list_ import List #tiene que estar en la carpeta de grafos  (importamos para reutilizar todo lo que ya teniamos)

class Graph(List):

    class __nodeVertex:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List() #aristas 
            self.edges.add_criterion('value', Graph._order_by_value) #estos son los criterios que agregamos 
            self.edges.add_criterion('weight', Graph._order_by_weight) #este tambien 
            self.other_values = other_values
            self.visited = False #el vertice es quien debe de llevar la marca de que no fue visitado=false
        
        def __str__(self):
            return str(self.value) #IMPORTANTE; le agrege srt() para que convierta todo a texto porque no puedo mostrar numeros sino 
    
    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values # no esta en uso aun
        
        def __str__(self):
            return f'Destination: {self.value} with weight --> {self.weight}'
    
    def __init__(self, is_directed=False):
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed


    ##### estos son dos criterios que creamos par ordenar/buscar ###### --> los tenemos que agregar en DEF  _init__ de la CLASS __nodeVertex
    def _order_by_value(item):
        return item.value

    def _order_by_weight(item):
        return item.weight
    #(a estas funciones las puedo crear en el codigo de prectica, donde esta cada ejercicio)


    def show(
        self
    ) -> None:
        for vertex in self:
            print(f"Vertex: {vertex}")
            vertex.edges.show()  # hace un show de las aristas 

    def insert_vertex( #insertar vertice 
        self,
        value: Any,
        other_values: Any = None  # parametro opcional  
    ) -> None:
        node_vertex = Graph.__nodeVertex(value, other_values=other_values)
        self.append(node_vertex)


    #conexiones/aristas/arcos/flechas (las conexines son listas o una lista )
    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None: 
        origin = self.search(origin_vertex, 'value') #origen (debemos de encontrar el origen y destino antes de insertar una conexion )
        destination = self.search(destination_vertex, 'value') #destino 

        if origin is not None and destination is not None: #chequeamos que ambos existan!!
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)

            if self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print('no se puede insertar falta uno de los vertices')

    def delete_edge(
        self,
        origin,
        destination,
        key_value: str = None,
    ) -> Optional[Any]:
        pos_origin = self.search(origin, key_value)
        if pos_origin is not None:
            edge = self[pos_origin].edges.delete_value(destination, key_value)
            if self.is_directed and edge is not None: #si es un ida y vuelta (grafo dirigido), debe de eliminar el otro vertice tambien. 
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(origin, key_value)
            return edge

    def delete_vertex(
        self,
        value,
        key_value_vertex: str = None,
        key_value_edges: str = 'value',
    ) -> Optional[Any]:
        delete_value = self.delete_value(value, key_value_vertex) # IMPORTANTE: cambie g.detele_value por self.delete_value porq g es el grafo definido abajo para mostrar el funcionamiento y no es generico si siguen con g 
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(vertex.value, value, key_value_edges)
        return delete_value

    def mark_as_unvisited(self) -> None: # este sirve para que no entre en un bucle cuando recorra
        for vertex in self: # barrer 1 a  1con el for 
            vertex.visited = False # le asignamos a cada uno el 'false' para saber que ya pasamos.

    # cada vez que hacemos un barrido debemos marcar todos los vertices como no visitados, para asegurarnos de que tenemos que pasar 
    # por todos los vertices y no pasar mas de una vez . --> esto tienen que estar cada vez que haga un BARRIDO 



    def exist_path(self, origin, destination):
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.search(edge.value, 'value')
                            if not graph[destination_edge_pos].visited:
                                result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result
        
        self.mark_as_unvisited()
        result = __exist_path(self, origin, destination)
        return result

    def deep_sweep(self, value) -> None: # barrido en profundidad  (el usuario dice desde que vertice quiere arrancar el barrido)
        # son dos barridos: 1 por vertice y 2 por su adyacente 
        def __deep_sweep(graph, value):
            vertex_pos = graph.search(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited: # si no paso por aca antes, entra
                    graph[vertex_pos].visited = True #cambio el valor de visitded
                    print(graph[vertex_pos])
                    for edge in graph[vertex_pos].edges: #necesitamos los adyacentes 'edges'(representacion de la conexion el 'edge')
                        destination_edge_pos = graph.search(edge.value, 'value')
                        if not graph[destination_edge_pos].visited:
                            __deep_sweep(graph, graph[destination_edge_pos].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)

    def amplitude_sweep(self, value)-> None:
        queue_vertex = Queue_()
        self.mark_as_unvisited()
        vertex_pos = self.search(value, 'value')
        if vertex_pos is not None:
            if not self[vertex_pos].visited:
                self[vertex_pos].visited = True
                queue_vertex.arrive(self[vertex_pos])
                while queue_vertex.size() > 0:
                    vertex = queue_vertex.attention()
                    print(vertex.value)
                    for edge in vertex.edges:
                        destination_edge_pos = self.search(edge.value, 'value')
                        if destination_edge_pos is not None:
                            if not self[destination_edge_pos].visited:
                                self[destination_edge_pos].visited = True
                                queue_vertex.arrive(self[destination_edge_pos])


    def dijkstra(self, origin):
        from math import inf
        no_visited = HeapMin()
        path = Stack()
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            no_visited.arrive([vertex.value, vertex, None], distance)
        while no_visited.size() > 0:
            value = no_visited.attention()
            costo_nodo_actual = value[0]
            path.push([value[1][0], costo_nodo_actual, value[1][2]])
            edges = value[1][1].edges
            for edge in edges:
                pos = no_visited.search(edge.value)
                if pos is not None:
                    if pos is not None:
                        if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                            no_visited.elements[pos][1][2] = value[1][0]
                            no_visited.change_priority(pos, costo_nodo_actual + edge.weight)
        return path
    


    def kruskal(self, origin_vertex): #---> arbol de expansion minima 
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index
                
        forest = []  #creamos el bosque
        edges = HeapMin()
        for vertex in self:
            forest.append(vertex.value)
            for edge in vertex.edges:
                edges.arrive([vertex.value, edge.value], edge.weight)
       
        while len(forest) > 1 and edges.size() > 0: #mientras el tamanio del bosque sea mayor que 1, seguimos. Vemos que el tamanio de las edge sea recorridas 
            edge = edges.attention()
            origin = search_in_forest(forest, edge[1][0])
            destination = search_in_forest(forest, edge[1][1])
            if origin is not None and destination is not None:
                if origin != destination:
                    if origin > destination:
                        vertex_origin = forest.pop(origin)
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)    

                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';'+f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination+';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')
        
        from_vertex = search_in_forest(forest, origin_vertex)
        
        return forest[from_vertex] if from_vertex is not None else forest    
        


# g = Graph()

# g.insert_vertex('A')
# g.insert_vertex('I')
# g.insert_vertex('B')
# g.insert_vertex('Z')
# g.insert_vertex('G')

# g.insert_edge('A', 'Z', 14)
# g.insert_edge('A', 'G', 4)
# g.insert_edge('I', 'A', 20)
# g.insert_edge('A', 'B', 7)
# g.insert_edge('B', 'Z', 144)
# g.insert_edge('B', 'A', 40)
# g.insert_edge('G', 'A', 24)
# # g.insert_edge('B', 'I', 11)

# g.show()
# print()

#  --> el eliminar queda funcionando bi-direccional  ///
#---> esta es la forma de eliminar correcta !!!
# vertex = g.delete_vertex('A', 'value')
# print(f'deleted vertex: {vertex}') // muestra el vertice eliminado 

# g.deep_sweep('A')

# print() --> aca solo mostro como hizo el barrido 
# for vertex in g:
#     print(vertex.value, vertex.visited)
# g.show()


# print('segundo barrido')
# g.deep_sweep('I')
#--> este segundo barrido no mostro nada. (por que porbo sin la funcion recursiva)


# es_adyacente(vértice, destino). Devuelve verdadero (true) si el destino es un nodo adyacente al vértice; (profe: devuelve true si un valor es adyacente o no)

# adyacentes(vértice). Realiza un barrido de los nodos adyacentes al vértice; (devuelve una lista con los adyacentes del obejto que le damos)

# existe _paso(grafo, vértice origen, vértice destino). Devuelve verdadero (true) si es posible ir des-
# de el vértice origen hasta el vértice destino, caso contrario retornará falso (false);

# barrido_profundidad(grafo, vértice inicio). Realiza un barrido en profundidad del grafo a par-
# tir del vértice de inicio;

# barrido_amplitud(grafo, vértice inicio). Realiza un barrido en amplitud del grafo a partir del
# vértice de inicio;




#### esto es lo copiado 
# g = Graph(is_directed=True)


# g.insert_vertex('A')
# g.insert_vertex('B')







# print(g.exist_path('T', 'Z'))

#==========================================NO SOLO CALCULO EL ARBOL DE EXPANCION, SINO QUE TENGO QEU PROCESAR LOS  DATOS 
# expansion_tree = g.kruskal('F')
# print(expansion_tree) --> esto solo me devuelve un string completo 
# como hago para separarlo ?? De la sig manera: 

# peso_total = 0  
# for edge in expansion_tree.split(';'): //split separa 
#     origin, destination, weight = edge.split('-')
#     print(f'origin {origin} destination {destination}')
#     peso_total += int(weight) 
# print(f'peso total: {peso_total}')
#===========================================




# ==========================================  DIJKSTRA - FUNCIONAMIENTO 
# path = g.dijkstra('T')  
# destination = 'Z'
# peso_total = None
# camino_completo = []

# while path.size() > 0:
#     value = path.pop()
#     if value[0] == destination:
#         if peso_total is None:
#             peso_total = value[1]
#         camino_completo.append(value[0])
#         destination = value[2]
# camino_completo.reverse()
# print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

#=============================================



# vertex = g.delete_vertex('A', 'value')
# print(f'deleted vertex: {vertex}')

# g.amplitude_sweep('A')

# --> hace la prueba mostrando que todos los vertices estan en false
# for vertex in g:
#     print(vertex.value, vertex.visited)
# g.show()
# print('segundo barrido')
# g.deep_sweep('I')

# ---> lo que hace es marcar a la 'a' que es la primera [0] como visitada.
# g[0].visited = true  === se muestra como ' A true '
# ---> pero si hace  g.mark_as_unvisited() ==== vuelven a aparecer coomo 'A false'




# es_adyacente(vértice, destino). Devuelve verdadero (true) si el destino es un nodo adyacente
# al vértice;
# adyacentes(vértice). Realiza un barrido de los nodos adyacentes al vértice;

# existe _paso(grafo, vértice origen, vértice destino). Devuelve verdadero (true) si es posible ir des-
# de el vértice origen hasta el vértice destino, caso contrario retornará falso (false);

# barrido_profundidad(grafo, vértice inicio). Realiza un barrido en profundidad del grafo a par-
# tir del vértice de inicio;

# barrido_amplitud(grafo, vértice inicio). Realiza un barrido en amplitud del grafo a partir del
# vértice de inicio;