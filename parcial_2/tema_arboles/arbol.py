from typing import Any, Optional
from queue_ import Queue_

class BinaryTree:

    class __nodeTree:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None
            self.height = 0

    def __init__(self):
        self.root = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                return BinaryTree.__nodeTree(value, other_values)
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)

            root = self.auto_balance(root)
            self.update_height(root)

            return root

        self.root = __insert(self.root, value, other_values)

    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                print(root.value, root.other_values, root.height)
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)

    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value, root.other_values)
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    #lo corrijo porque me tira error el chat 
    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.left)               
                __post_order(root.right)
                print(root.value)

        if self.root is not None:
            __post_order(self.root)

    def search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if root.value == value:
                    return root
                elif root.value > value:
                    return __search(root.left, value)
                else:
                    return __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux
    

    def proximity_search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                # elif root.value > value:
                __search(root.left, value)
                # else:
                __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

   
    def delete(self, value: Any):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            delete_value = None
            deleter_other_values = None
            if root is not None:
                if value < root.value:
                    root.left, delete_value, deleter_other_values = __delete(root.left, value)
                elif value > root.value:
                    root.right, delete_value, deleter_other_values = __delete(root.right, value)
                else:
                    delete_value = root.value
                    deleter_other_values = root.other_values
                    if root.left is None:
                        root = root.right
                    elif root.right is None:
                        root.right = root.left
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_values = replace_node.other_values

                root = self.auto_balance(root)
                self.update_height(root)
            return root, delete_value, deleter_other_values

        delete_value =  None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)
        
        return delete_value, deleter_other_values
    
    def by_level(self):
        tree_queue = Queue_()
        if self.root is not None:
            tree_queue.arrive(self.root)

            while tree_queue.size() > 0:
                node = tree_queue.attention()
                print(node.value)
                if node.left is not None:
                    tree_queue.arrive(node.left)
                if node.right is not None:
                    tree_queue.arrive(node.right)

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            alt_left = self.height(root.left)
            alt_right = self.height(root.right)
            root.height = max(alt_left, alt_right) + 1

    def simple_rotation(self, root, control):
        if control: # RS Right
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # RS Left
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control: # RD Right
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        
        return root

    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    # print("RS RIGHT")
                    root = self.simple_rotation(root, True)
                else:
                    # print("RD RIGHT")
                    root = self.double_rotation(root, True)
            if self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    # print("RS LEFT")
                    root = self.simple_rotation(root, False)
                else:
                    # print("RD LEFT")
                    root = self.double_rotation(root, False)
        return root
    

    #                           A PARTIR DE ACA SON FUNCIONES DE EJERCICIOS 
    #ejercicio 23 
    def in_order_der(self):
        def __in_order_der(root):
            if root is not None:
                __in_order_der(root.left)
                print(f'{root.value}- derrotada por :{root.other_values}')
                __in_order_der(root.right)

        if self.root is not None:
            __in_order_der(self.root)

    #ejercicio numero 10 
    def contar_nodos_en_nivel(self, nivel_objetivo):
        
        def __contar_nodos(root, nivel_actual):
            if root is None:
                return 0
            if nivel_actual == nivel_objetivo:
                return 1
            return (__contar_nodos(root.left, nivel_actual + 1) +
                    __contar_nodos(root.right, nivel_actual + 1))

        return __contar_nodos(self.root, 0)

    def nodos_maximos_en_nivel(self, nivel):
        
        return 2 ** nivel


    #ejercicio 8 
    def maximo(self):  
     
        def __maximo(root):
            if root is None:
                return None
            # si tiene hijo derecho, sigo bajando por la derecha (mayores)
            if root.right is not None:
                return __maximo(root.right)
            # cuando no tiene más derechos, este es el máximo
            return root

        if self.root is not None:
            return __maximo(self.root)
        else:
            return None


    def minimo(self):
        def __minimo(root):
            if root is None:
                return None
            # si tiene hijo izquierdo, sigo bajando por la izquierda (menores)
            if root.left is not None:
                return __minimo(root.left)
            # cuando no tiene más izquierdos, este es el mínimo
            return root

        if self.root is not None:
            return __minimo(self.root)
        else:
            return None


    #tp5-punto e
    def proximity_busqueda(self, value: Any) -> __nodeTree:
        def __search(root, value):
            # Busca recursivamente un nodo cuyo valor (string) empiece con el prefijo `value`.
            if root is None:
                return None

            try:
                if isinstance(root.value, str) and root.value.startswith(value):
                    return root
            except Exception:
                pass

            left_result = __search(root.left, value)
            if left_result is not None:
                return left_result

            return __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux
 
    #para ordenar de manera descendiente solo cambio left y right 
    def in_order_des(self):
        def __in_order_des(root):
            if root is not None:
                __in_order_des(root.right)#primero la derecha (mayores)
                if root.other_values is False: # is_villain = false o true
                    print(root.value)
                __in_order_des(root.left) #luego la izquiera (menores)

        if self.root is not None:
            __in_order_des(self.root)

    def in_order_her(self):
        def __in_order_her(root):
            if root is not None:
                __in_order_her(root.left)
                if root.other_values['Derrotado_por'] == 'Heracles':
                    print(root.value, root.other_values)
                __in_order_her(root.right)

        if self.root is not None:
            __in_order_her(self.root)


    def villain_in_order(self):
        def __villain_in_order(root):
            if root is not None:
                __villain_in_order(root.left)
                if root.other_values["is_villain"] is True:
                    print(root.value)
                __villain_in_order(root.right)

        if self.root is not None:
            __villain_in_order(self.root)

    #tp5 punto 'c'
    def super_in_order(self):
        def __super_in_order(root):
            if root is not None:
                __super_in_order(root.left)
                #que empiece con 'c' y que sea superheroe
                if root.value.startswith("C") and root.other_values is False:
                    print(root.value) #solo mostrmaos el nombre
                __super_in_order(root.right)

        if self.root is not None:
            __super_in_order(self.root)

    #ejercicio_1 = parcial  ============================================================   parcial ================================
    def tipo_in_order(self):
        def __tipo_in_order(root):
            if root is not None:
                __tipo_in_order(root.left)
                if root.value == "fantasma":  
                    print(root.other_values['nombre'])
                __tipo_in_order(root.right)

        if self.root is not None:
            __tipo_in_order(self.root)

  
    def in_order_simple(self):
        def __in_order_simple(root):
            if root is not None:
                __in_order_simple(root.left)
                print(f"{root.value} - {root.other_values['nombre']}")
                __in_order_simple(root.right)

        if self.root is not None:
            __in_order_simple(self.root)

    def in_order_tipo(self):
        def __in_order_tipo(root):
            if root is not None:
                __in_order_tipo(root.left)
                if root.value in ["Jolteon", "Lycanroc", "Tyrantrum"]:
                  print(f"{root.value} - {root.other_values['debilidad']}")
                __in_order_tipo(root.right)

        if self.root is not None:
            __in_order_tipo(self.root)

    def in_order_simp(self):
        def __in_order_simp(root):
            if root is not None:
                __in_order_simp(root.left)
                print(f"nombre: {root.value}")
                __in_order_simp(root.right)

        if self.root is not None:
            __in_order_simp(self.root)

   #cuenta cantidad de tipos fantasma 
    def contar_tipos(self):
        def __contar_tipos(root):
            count = 0
            if root is not None:
                if root.other_values["fantasma"]:
                    count += 1
                count += __contar_tipos(root.left)
                count += __contar_tipos(root.right)

            return count

        total = 0
        if self.root is not None:
            total = __contar_tipos(self.root)
        return total
    

    
  
    # Mostrar todos los tipos (sin repetir)
    def mostrar_tipos(self):
        tipos_unicos = set() #el set no admite duplicados 
        
        def __recolectar(root):
            if root is not None:
                __recolectar(root.left)
                tipos_unicos.add(root.value)
                __recolectar(root.right)
        
        if self.root is not None:
            __recolectar(self.root)
        
        return sorted(tipos_unicos)
    
    # Contar cantidad de cada tipo
    def contar_tipos(self):
        tipos_count = {}
        
        def __contar(root):
            if root is not None:
                __contar(root.left)
                tipo = root.value
                tipos_count[tipo] = tipos_count.get(tipo, 0) + 1
                __contar(root.right)
        
        if self.root is not None:
            __contar(self.root)
        
        return tipos_count
    
    def megaevolucion(self):
        def __megae(root):
            count = 0
            if root is not None:
                if root.other_values["megaevolucion"] is True:
                    count += 1
                count += __megae(root.left)
                count += __megae(root.right)

            return count

        total = 0
        if self.root is not None:
            total = __megae(self.root)
        return total
    

    def gigamax(self):
        def __gigamax(root):
            count = 0
            if root is not None:
                if root.other_values["gigamax"] is True:
                    count += 1
                count += __gigamax(root.left)
                count += __gigamax(root.right)

            return count

        total = 0
        if self.root is not None:
            total = __gigamax(self.root)
        return total






    
    def is_villain_in_order(self):
        def __is_villain_in_order(root):
            if root is not None:
                __is_villain_in_order(root.left)
                if root.other_values is True: #solo imprime los villanos 
                    print(root.value)
                __is_villain_in_order(root.right)

        if self.root is not None:
            __is_villain_in_order(self.root)
    
    def count_heroes(self):
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.other_values["is_villain"] is False:
                    count += 1
                count += __count_heroes(root.left)
                count += __count_heroes(root.right)

            return count

        total = 0
        if self.root is not None:
            total = __count_heroes(self.root)
        
        return total
    
    def contar_heroes(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is False: #todos los heroes 
                    count += 1
                count += __contar_heroes(root.left)#Llama recursivamente a la función para el hijo izquierdo.
                count += __contar_heroes(root.right)#Llama recursivamente a la función para el hijo derecho.

            return count

        total = 0 #inicializamos la variable total en 0
        if self.root is not None:#Revisamos si el árbol tiene al menos un nodo.
            total = __contar_heroes(self.root)#Llamamos a la función recursiva privada __contar_heroes, pasándole la raíz del árbol.
        
        return total #mandamos le total fuera de la funcion
    


    def contar_villain(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is True: #todos los heroes 
                    count += 1
                count += __contar_heroes(root.left)#Llama recursivamente a la función para el hijo izquierdo.
                count += __contar_heroes(root.right)#Llama recursivamente a la función para el hijo derecho.

            return count

        total = 0 #inicializamos la variable total en 0
        if self.root is not None:#Revisamos si el árbol tiene al menos un nodo.
            total = __contar_heroes(self.root)#Llamamos a la función recursiva privada __contar_heroes, pasándole la raíz del árbol.
        
        return total #mandamos le total fuera de la funcion
    
    #es del ej6 quiero que solo muestre el campo principal 
    def in_order_dato(self):
        def __in_order_dato(root):
            if root is not None:
                __in_order_dato(root.left)
                print(root.value) #borro el other_values 
                __in_order_dato(root.right)

        if self.root is not None:
            __in_order_dato(self.root) #le pongo 'dato para recordar que solo muestra el dato principal 

    def divide_tree(self, arbol_h, arbol_v):
        def __divide_tree(root, arbol_h, arbol_v):
            if root is not None:
                if root.other_values["is_villain"] is False:
                    arbol_h.insert(root.value, root.other_values)
                else:
                    arbol_v.insert(root.value, root.other_values)
                __divide_tree(root.left, arbol_h, arbol_v)
                __divide_tree(root.right, arbol_h, arbol_v)


        __divide_tree(self.root, arbol_h, arbol_v)
    

    #dividir en 2 abroles (villanos y super) Ej5
    def divide_arbol(self, arbol_her, arbol_vill):
        def __divide_arbol(root, arbol_her, arbol_vill):
            if root is not None:
                if root.other_values is False:
                    arbol_her.insert(root.value, root.other_values) #inserta ambos datos (name, is_villain)
                else:
                    arbol_vill.insert(root.value, root.other_values)#inserta ambos datos (name, is_villain)
                __divide_arbol(root.left, arbol_her, arbol_vill)
                __divide_arbol(root.right, arbol_her, arbol_vill)


        __divide_arbol(self.root, arbol_her, arbol_vill)


    def in_order_height(self):
        def __in_order_height(root):
            if root is not None:
                __in_order_height(root.left)
                if root.other_values['height'] > 100:
                    print(root.value, root.other_values['height'])
                __in_order_height(root.right)

        if self.root is not None:
            __in_order_height(self.root)
    
    def in_order_weight(self):
        def __in_order_weight(root):
            if root is not None:
                __in_order_weight(root.left)
                if root.other_values['weight'] < 75:
                    print(root.value, root.other_values['weight'])
                __in_order_weight(root.right)

        if self.root is not None:
            __in_order_weight(self.root)





# print()K
# arbol.update_hight(arbol.root.left.left)
# print()
# arbol.update_hight(arbol.root.left)
# print()
# arbol.update_hight(arbol.root)
# print()
# arbol.pre_order()

# arbol.insert('F', 'f')
# arbol.insert('B', 'b')
# arbol.insert('K', 'k')
# arbol.insert('H', 'h')
# arbol.insert('J', 'j')
# arbol.insert('E', 'e')
# arbol.insert('B')
# arbol.insert('V')
# arbol.pre_order()
# print()


# for i in range(1, 16):
#     arbol.insert(i)

# arbol.pre_order()

# if pos is not None:
#     arbol.delete('F')
#     arbol.insert('C', 'c')

# delete_value, deleter_other_values = arbol.delete('K')
# if delete_value is not None:
#     print(delete_value, deleter_other_values)


# arbol.in_order()
# # delete_value = arbol.delete('F')

# # if delete_value is not None:
# #     print(f'valor eliminado {delete_value}')
# # else:
# #     print('valor no encontrado')
# # print()
# arbol.by_level()


# # arbol.insert(11)

# # pos = arbol.search(19)
# # print(pos)
# arbol.in_order()

# from super_heroes_data import superheroes

# for super_hero in superheroes:
#     arbol.insert(super_hero['name'], super_hero)


# arbol.divide_tree(arbol_heroes, arbol_villanos)

# bosque = [arbol_heroes, arbol_villanos]

# for tree in bosque:
#     tree.in_order()
#     print()

# arbol.proximity_search('Dr')
# name = input('ingrese nombre para modificar: ')
# value, other_value = arbol.delete(name)

# if value is not None:
#     fix_name = input('ingrese el nuevo nombre: ')
#     other_value['name'] = fix_name
#     arbol.insert(fix_name, other_value) 

# print()
# arbol.proximity_search('Dr')
# print()
# pos = arbol.search('Dr Strange')
# if pos is not None:
#     print(pos.value, pos.other_values)

# print(arbol.count_heroes())

# arbol.villain_in_order()

# print()
# pos = arbol.search("Thanos")
# if pos is not None:
#     print(pos.value, pos.other_values)