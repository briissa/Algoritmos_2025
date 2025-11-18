# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
# cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;

# 1.hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;

# 2.determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;

# 3.cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;

# 4.calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;

# 5.indicar qué personajes aparecieron en los nueve episodios de la saga.


from graph import Graph

#lista de los personajes 
starw = ["Luke Skywalker","Darth Vader","Yoda","Boba Fett","C-3PO","Leia","Rey","Kylo Ren",
    "Chewbacca","Han Solo","R2-D2","BB-8"
]

#defno el grafo 
grafo = Graph(is_directed=True)

#los cargo de la lista al grafo (vertices)
for personaje in starw:
    grafo.insert_vertex(personaje)


# aristas  
grafo.insert_edge("C-3PO","R2-D2",9)
grafo.insert_edge("Luke Skywalker","Leia",6)
grafo.insert_edge("Luke Skywalker","Darth Vader",3)
grafo.insert_edge("Han Solo","Chewbacca",5)
grafo.insert_edge("Rey","BB-8",3)
grafo.insert_edge("Leia","C-3PO",6)
grafo.insert_edge("Darth Vader","C-3PO",2)
grafo.insert_edge("Yoda","Luke Skywalker",3)
grafo.insert_edge("Boba Fett","Han Solo",1)
grafo.insert_edge("Kylo Ren","Rey",2)



# 1.hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
print("arbol-expansion desde C-3PO:")
print(grafo.kruskal("C-3PO"))

print()
print("arbol-expansion desde Yoda:")
print(grafo.kruskal("Yoda"))

print()
print("arbol-expansion desde Leia:")
print(grafo.kruskal("Leia"))


print()
# 2. maximo de episodios
max_ep = 0
pares_max = []
for vertex in grafo:
    for edge in vertex.edges:
        if edge.weight > max_ep:
            max_ep = edge.weight
            pares_max = [(vertex.value, edge.value)]
        elif edge.weight == max_ep:
            pares_max.append((vertex.value, edge.value))

print("max de episodios compartidos:", max_ep)
print("Pares de personajes:")
for par in pares_max:
    print(par)


print()
# 4. Caminos mas cortos
print("Camino mas corto de C-3PO a R2-D2:")

path = grafo.dijkstra("C-3PO")
destination = "R2-D2"
peso_total = None
camino = []

while path.size() > 0:
    value = path.pop()
    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]
        camino.append(value[0])
        destination = value[2]

camino.reverse()
print(f'el camino mas corto es: {"-".join(camino)} con un costo de {peso_total}')

#segundo camino mas corto 
print()
print("Camino mas corto de Yoda a Darth Vader :")

path = grafo.dijkstra("Yoda")
destination = "Darth Vader"
peso_total = None
camino = []

while path.size() > 0:
    value = path.pop()
    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]
        camino.append(value[0])
        destination = value[2]
camino.reverse()
print(f'el camino mas corto es: {"-".join(camino)} con un costo de {peso_total}')

print()
# 5. Personajes que aparecieron en los 9 episodios
aparecen_9 = set() #evita repetir personajes
for vertex in grafo:
    for edge in vertex.edges:
        if edge.weight == 9:
            aparecen_9.add(vertex.value)
            aparecen_9.add(edge.value)

print("Personajes que aparecieron en los 9 episodios:")
for p in aparecen_9:
    print(p)
