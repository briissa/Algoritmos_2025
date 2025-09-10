from typing import Any, Optional


class BinaryTree:

    class __nodeTree:
        """ este es el nodo dentro del arbol binario"""
        def __init__(self, value: Any, other_values: Optional[Any]= None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None

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


    def post_order(self):
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
                __pre_order(root.left)
                print(root.value)
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