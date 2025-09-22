# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria que resuelva las siguientes actividades:

# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.


from arbol import BinaryTree
from random import randint
from queue_ import Queue_

arbol= BinaryTree()
for num in range (10):
    arbol.insert(randint(0, 15))



# a. realizar los barridos

print("-- barrido in-order---")
arbol.in_order()
print("--------------")

print("-- barrido  pre-order---")
arbol.pre_order()
print("--------------")

print("-- barrido post-order---")
arbol.post_order()
print("--------------")

print("barrido por-nivel")
arbol.by_level()
print("-----------")



# b. determinar si un número está cargado en el árbol o no;
pos = arbol.search(10)
if pos is not None:
    print("el numero esta en el arbol")
else: 
    print ("el numero no esta en el arbol")
print("--------------")


# c. eliminar tres valores del árbol;
# eliminamos valores elegidos por nosotros 
arbol.delete(4) 
arbol.delete(7)
arbol.delete(11)
print("barrido in-order despues de eliminar 3 valores ")
arbol.in_order()
print("--------------")




# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
print('altura del arbol derecho:')
print(arbol.height(arbol.root.right))

print("altura del arbol izquierdo:")
print(arbol.height(arbol.root.left))#accede al hijo izquierdo del nodo raíz. 



# f. contar cuántos números pares e impares hay en el árbol.

def pares_impares_rec(root):
    if root is None:
        return 0, 0  # pares, impares

    # Contamos en subárbol izquierdo
    pares_izq, impares_izq = pares_impares_rec(root.left) #Llama a la función pares_impares_rec de forma recursiva sobre el subárbol izquierdo del nodo actual (root.left).
    # Contamos en subárbol derecho
    pares_der, impares_der = pares_impares_rec(root.right)

    # Contamos el nodo actual
    if root.value % 2 == 0:
        pares_actual = 1
        impares_actual = 0
    else:
        pares_actual = 0
        impares_actual = 1

    # Sumamos todo
    pares_tot = pares_izq + pares_der + pares_actual
    impares_tot = impares_izq + impares_der + impares_actual

    return pares_tot, impares_tot


pares, impares = pares_impares_rec(arbol.root)
print(f"Pares: {pares}, Impares: {impares}")           