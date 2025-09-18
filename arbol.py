from typing import Any, Optional
from queue_ import Queue_   #corroborar esto, que sean los correctos


class BinaryTree:

    class __nodeTree:
        """ este es el nodo dentro del arbol binario"""
        def __init__(self, value: Any, other_values: Optional[Any]= None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None
            self.hight = 0

    """inicializamos la clase arbol"""
    def __init__(self):
        self.root = None




    """metodo insertar"""
    def insert(self, value: Any, other_values : Optional[Any]= None):
        print(f'insertar value {value}')

        """esta es una funcion recursiva, donde chequeaba si la raiz era vacia(inserta ahi),
          en caso de no serlo evaluaba si tenia que ir a la izq o derecha  (siempre inserta una hoja)""" 
        def __insert(root, value, other_values):
            if root is None:
                print('lugar libre insertar raiz')
                return BinaryTree.__nodeTree(value, other_values)
            elif value < root.value:
                print(f'vamos a la izquierda ->padre {root.value}')
                root.left = __insert(root.left, value, other_values)
            else:
                print(f'vamos a la derecha ->padre {root.value}')
                root.right = __insert(root.right, value, other_values)

            root = self.auto_balance(root) #veriifcar 
            self.update_hight(root)

            return root
        
        self.root = __insert(self.root, value, other_values)






    """los barridos que tenemos son: inorden (deberia devolverme los elementos en orden descendente), posorden (deberia devolverme los elementos ord de manera ascendente) y preorden"""

    def in_order(self):
        """recorrido inorden"""
        def __in_order(root):
            if root is not None:
                print("hoja no vacia")
                print("me voy a la izquierda")
                __in_order(root.left)
                print("nodo actual",root.value)
                print("me voy a la derecha")
                __in_order(root.right)
            else:
                print("hoja vacia")
        if self.root is not None:
            __in_order(self.root)


    """
    la logica del barrido es muy simple: me fijo si tengo valores en la raiz donde estoy parado actualmente,
    si tengo valor, me voy a la izq (con la llamada recursiva para que repita el proceso), muestra el valor y me voy a la derecha.

    """


    def post_order(self):  #el chat me dice que no esta bien hecha
        """recorrido posorden"""
        def __post_order(root):

            "este es el mismo arbol que el anterior, solo qeu en el primero me voy a ala derech y dsp a la izq"
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)
        if self.root is not None:
            __post_order(self.root)


    def pre_order(self):
        """recorrido preorden"""
        def __pre_order(root):
            if root is not None:
                print(root.value, root.other_values, root.hight)
                __pre_order(root.left)
                __pre_order(root.right)
        if self.root is not None:
            __pre_order(self.root)

    """ Este lo que hace el mostrar el valor, luego irse para la izquierda 
        y despues para la derecha.
    """



    "VAMOS A HACER LA BUSQUEDA"
    def search (self, value: Any) -> __nodeTree:
        def __search (root, value):
            if root is not None :
                if root.value == value:
                    "en esta parte hago lo que me pide el ejercicio"
                    print("valor encontrado")
                    return root
                elif root.value > value:
                    print("me voy a buscar a la izq")
                    return __search(root.left, value)
                else:
                    print("me voy a buscar a la derch")
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
                        root = root.left
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_values = replace_node.other_values

                root = self.auto_balance(root)
                self.update_hight(root)
            return root, delete_value, deleter_other_values

        delete_value =  None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)
        
        return delete_value, deleter_other_values  


    def by_level(self):
        tree_queue = Queue()
        if self.root is not None:
            tree_queue.arrive(self.root)

            while tree_queue.size() > 0:
                node = tree_queue.attention()
                print(node.value)
                if node.left is not None:
                    tree_queue.arrive(node.left)
                if node.right is not None:
                    tree_queue.arrive(node.right)  

    def hight(self, root):
        if root is None:
            return -1
        else:
            return root.hight

    def update_hight(self, root):
        if root is not None:
            alt_left = self.hight(root.left)
            alt_right = self.hight(root.right)
            root.hight = max(alt_left, alt_right) + 1

    def simple_rotation(self, root, control):
        if control: # RS Right
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # RS Left
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_hight(root)
        self.update_hight(aux)
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
            if self.hight(root.left) - self.hight(root.right) == 2:
                if self.hight(root.left.left) >= self.hight(root.left.right):
                    # print("RS RIGHT")
                    root = self.simple_rotation(root, True)
                else:
                    # print("RD RIGHT")
                    root = self.double_rotation(root, True)
            if self.hight(root.right) - self.hight(root.left) == 2:
                if self.hight(root.right.right) >= self.hight(root.right.left):
                    # print("RS LEFT")
                    root = self.simple_rotation(root, False)
                else:
                    # print("RD LEFT")
                    root = self.double_rotation(root, False)
        return root
        #a partir de estos son funciones que hacemos para resolver ejercicios particulares.
    def villain_in_order(self):
        def __villain_in_order(root):
            if root is not None:
                __villain_in_order(root.left)
                if root.other_values["is_villain"] is True:
                    print(root.value)
                __villain_in_order(root.right)

        if self.root is not None:
            __villain_in_order(self.root)

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

arbol = BinaryTree()
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

    


                
"para usarlo el profe hizo: "
" pos= arbol.search(22)"
"print( pos.value, pos.left, pos.right.value )" 

"lo que muestra es: valor encontrado / 22 none 27"
arbol = BinaryTree() 
#arbol.insert(19)
#arbol.insert(7)
#arbol.insert(11)
#arbol.insert(22)
#arbol.in_order()



"las opciones son : que sea una hoja, que el nodo tenga 1 hijo y que el nodo tenga 2 hijos (se va por la izq o derecha)"


# es una eliminacion recursiva 
def delete (self, value: Any):

    #esta funcion la vamos a usar para encontrar el nodo que va a reemplazar al que queremos eliminar 
    def __replace (root):
        if root.right is None:
            return root
        elif root.left is None:
            return root


    def __delete (root, value):


        #la condicion de fin es que el arbol este vacio 
        if root is None:
            if value < root.value:
                __delete (root.value, value)

            elif value > root.value:
                __delete (root.value, value)


#si la izq y la derecha son none significa que tiene a los dos hijos 
#si no es mayor ni menor, significa que lo encontramos 

#se determina que es el mayor cuando a su derecha ya no hay nada (porque cda vez que el numero es mayor, va la la derecha)
#si es que hay algo en la derecha, cicla todas las veces hasta que no haya mas nada en la derecha (recursividad)

#en una parte devuelve none porque puede ser que no este 
# delete_value = none 