# 5.Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios
#   para resolver las tareas, listadas a continuación:

# para saber:
# La clase UTILIZADA agrega arista inversa solo cuando is_directed=True.
# Por eso, para tener GRAFO NO DIRIGIDO:

from graph import Graph

g = Graph(is_directed=True)

nodos = [
    'Router 1','Router 2','Router 3',
    'Switch 1','Switch 2',
    'Red Hat','Debian','Arch',
    'Manjaro','Parrot','Ubuntu','Mint','Fedora',
    'Guarani','MongoDB','Impresora'
]

#agrega cada vertice en el grafo 
for var in nodos:
    g.insert_vertex(var)     


# Cada nodo debe almacenar su tipo:
# pc, notebook, servidor, router, switch, impresora
# Esto se guarda en v.other_values 

for v in g:
    if v.value in ['Red Hat','Debian','Arch']:
        v.other_values = 'notebook'
    elif v.value in ['Manjaro','Parrot','Ubuntu','Mint','Fedora']:
        v.other_values = 'pc'
    elif v.value in ['Guarani','MongoDB']:
        v.other_values = 'servidor'
    elif v.value in ['Router 1','Router 2','Router 3']:
        v.other_values = 'router'
    elif v.value in ['Switch 1','Switch 2']:
        v.other_values = 'switch'
    elif v.value == 'Impresora':
        v.other_values = 'impresora'

# Rutas entre routers y servidores/notebooks
g.insert_edge('Router 1','Router 2',37)
g.insert_edge('Router 1','Router 3',43)
g.insert_edge('Router 2','Router 3',50)
g.insert_edge('Router 2','Red Hat',25)
g.insert_edge('Router 2','Guarani',9)

# Red del Switch 2
g.insert_edge('Router 3','Switch 2',61)
g.insert_edge('Switch 2','Manjaro',40)
g.insert_edge('Switch 2','Parrot',12)
g.insert_edge('Switch 2','MongoDB',5)
g.insert_edge('Switch 2','Arch',56)
g.insert_edge('Switch 2','Fedora',3)

# Red del Switch 1
g.insert_edge('Switch 1','Debian',17)
g.insert_edge('Switch 1','Ubuntu',18)
g.insert_edge('Switch 1','Impresora',22)
g.insert_edge('Switch 1','Mint',80)
g.insert_edge('Switch 1','Router 1',29)


# a. mostrar tipos de nodos 
print("- A) Tipos de nodos ")
for var in g:
    print(var.value, "-", var.other_values)


# b.barridos 
# Red Hat, Debian, Arch

inicios = ['Red Hat','Debian','Arch']

for start in inicios:
    print("- B) DFS desde", start)
    g.deep_sweep(start)       # recorrido en profundidad 

    print("- B) BFS desde", start)
    g.amplitude_sweep(start)  # recorrido en amplitud 


#c. camino corto asi la impresora
# desde: Manjaro, Red Hat, Fedora
# Utiliza dijkstra() 

print(" Camino minimo hacia Impresora: ")
fuentes = ['Manjaro', 'Red Hat', 'Fedora']

for orig in fuentes:

    # dijkstra devuelve un stack con tu formato: [nodo, distancia, predecesor]
    stack = g.dijkstra(orig)
    dist = {}

    # Pasar el stack a dict
    while stack.size() > 0:
        nodo, d, prev = stack.pop()
        dist[nodo] = (d, prev)

    # Si impresora no está alcanzable
    if 'Impresora' not in dist or dist['Impresora'][0] == float('inf'):
        print("No hay camino desde", orig)
        continue

    # reconstruccion manual del camino mas corto
    camino = []
    actual = 'Impresora'
    while actual is not None:
        camino.append(actual)
        if actual == orig:
            break
        actual = dist[actual][1]

    camino.reverse()

    print(f"{orig} -> Impresora: costo {dist['Impresora'][0]}, camino {camino}")


# d. arbol de expansion minima
# usando kruskal() ya implementado en tu clase

print("- D) Arbol de expansion minima (Kruskal)")
print(g.kruskal('Router 1'))   #siempre tenemos que indicar un vertice inicial


# e. PC más cercana al servidor Guarani
# (solo PCs, no notebooks)

print(" PC mas cercana a Guarania:")

mejor_pc = None
mejor_dist = float('inf')
mejor_camino = None

for v in g:
    if v.other_values == 'pc':   # solo PCs
        origen = v.value

        # correr Dijkstra desde esa PC
        stk = g.dijkstra(origen)
        dist = {}
        while stk.size() > 0:
            n, d, p = stk.pop()
            dist[n] = (d, p)

        # ¿mejor distancia actual?
        if 'Guarani' in dist and dist['Guarani'][0] < mejor_dist:
            mejor_dist = dist['Guarani'][0]

            # reconstruir camino
            actual = 'Guarani'
            camino = []
            while actual is not None:
                camino.append(actual)
                if actual == origen:
                    break
                actual = dist[actual][1]
            camino.reverse()

            mejor_camino = camino
            mejor_pc = origen

print("PC con camino más corto:", mejor_pc)
print("Distancia:", mejor_dist)
print("Camino:", mejor_camino)


# f. Computadora (pc o notebook) conectada al Switch 1
# con camino más corto hacia MongoDB.

print("- F) Equipo conectado a Switch 1 mas cercano a MongoDB")

# buscamos vecinos de Switch 1
pos_s1 = g.search('Switch 1','value')
equipos_s1 = []

# recorrer las aristas del switch
for ar in g[pos_s1].edges:
    posv = g.search(ar.value,'value')
    tipo = g[posv].other_values
    if tipo in ['pc','notebook']:
        equipos_s1.append(ar.value)

mej = None
mej_dist = float('inf')
mej_camino = None

# calcular distancia desde cada uno
for eq in equipos_s1:

    stk = g.dijkstra(eq)
    dist = {}

    while stk.size() > 0:
        n, d, p = stk.pop()
        dist[n] = (d, p)

    if 'MongoDB' in dist and dist['MongoDB'][0] < mej_dist:
        mej_dist = dist['MongoDB'][0]

        # reconstruir camino
        actual = 'MongoDB'
        camino = []
        while actual is not None:
            camino.append(actual)
            if actual == eq:
                break
            actual = dist[actual][1]
        camino.reverse()

        mej = eq
        mej_camino = camino

print("Equipo:", mej)
print("Distancia:", mej_dist)
print("Camino:", mej_camino)


# g. Cambiar la impresora al Router 2 y repetir DFS/BFS

print("- G) Mover impresora a Router 2 y repetir recorridos ")

# borrar conexión actual
g.delete_edge('Switch 1','Impresora','value')

# nueva conexión
g.insert_edge('Router 2','Impresora',22)

# repetir recorridos
for start in inicios:
    print("\n--- DFS desde", start, "(impresora movida) ---")
    g.deep_sweep(start)

    print("\n--- BFS desde", start, "(impresora movida) ---")
    g.amplitude_sweep(start)

