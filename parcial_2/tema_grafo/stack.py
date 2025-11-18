from typing  import Any, Optional

#de tipo le ponemos Any para que acepte cualquie tipo de dato
#  para apilar numero, string, todo 

class Stack:
 # cuando le agregamos doble guion bajo, queremos dcir que ese atributo (__elements) es privado
 # y no se puede acceder desde afuera de la clase

 def __init__(self):  #definimos el constructor de la clase(siempre se llama igual)
     self.__elements = [] #inicializamos la pila vacia
 #definimos el constructor de la clase

 #esta funcion es para agregar un elemento a la pila, en la ult posicion
 def push (self, value: Any)-> None:  # no me interesa que me devuelva nada
     self.__elements.append(value)     

 #esta funcion es la que elimina al ultimo de la pila
 def pop (self) -> Optional[Any]:
    return (
        self.__elements.pop()
        if self.__elements 
        else None
    )
   #el self es algo generico, cuando entre un objeto que sea ejecutable ese self lo adopta.

 def size (self)-> int: #sempre espero de salida un entero, si esta vacia que me devuelva 0
    # len devuelvela cantidad de elementos que hay en la pila
    return len (self.__elements)
 

 #devuelve el valor  del elemento que esta en la cima de la pila pero sin eliminarlo 
 def On_top (self)-> Optional[Any]:
    return(
        self.__elements[-1]
        if self.__elements #el 'self' es como el 'this' en java (con esto nombramos a la clase)
        else None # si la pila esta vacia decvuelve (none) 
    )
 
 def show (self):
      aux_stack= Stack()
      while self.size() > 0:
         value = self.pop()
         print(value)
         aux_stack.push (value)
      
      while aux_stack.size() > 0:
         self.push (aux_stack.pop())   

 #esta funcion no sirve para ver el funcionamiento y verificar.
 #pero no va dentro de nuestros ejercicios
    
 #una vez que creamos la clase, la instaciamos para poder usarla
# stack= Stack() #creamos nuestro objeto de tipo stack

# from random import randint #para generar numeros aleatorios
# #de la libreria random importamos randint. 
# for i in range (5):
#    stack.push (randint (1, 10))#le pasamos un velor inicial y uno final(ambos incluidos)

# stack.show() #muestro la pila
# print(stack.pop())
# stack.show()

#el "(self)" que esta dentro de la clase en cada funcion, es el mismo que el "stack" que esta afuera "(stack,show())"
# hacen referencia a la misma cosa stack=self