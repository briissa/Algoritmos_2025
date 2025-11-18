from typing import Any, Optional

class Queue_:
    def __init__(self) :
        self.__elements = [] #la cola vacia 
        
        
    # Agrega un elemento al final de la cola
    def arrive(self, value : Any)-> None: #la funcion no retorna nada 
        self.__elements.append(value)

   #como podria esta la cola vacia, le pasamos any.
    def attention(self) -> Optional[Any]: #no le pasamos nada como parametros porque no podemos elegir que se va.
        return(
            self.__elements.pop(0) #con el pop y (0), elimino el primer elemento
            if self.__elements
            else None
            )
        
    def size(self) -> int: #siempre va a devolver un entero xq es el tamaño de la cola
        return len(self.__elements)
        
        
        # Devolver el primer elemento sin eliminarlo
    def on_front(self)-> Optional[Any]: #any porque si la cola esta vacai no tenemos nada para mover al frente
        return (
            self.__elements[0] #accede al primer elemento
            if self.__elements
            else None
            )
        

        #mover el primer elemento al final de la cola
    def move_to_end (self) -> Optional[Any]:
        if self.__elements: 
            value = self.attention()
            self.arrive(value)
            return value

    def show (self):
        for i in range (len (self.__elements)):
            print( self.move_to_end())

