
from typing import Any, Optional

class List(list):
    # a las funciones anteriores las estoy almacenando en el diccionario 

    CRITERION_FUNCTIONS= {} #aca nos queda solo un diccionario generico

    def add_criterion (
        self,
        key_criterion: str,
        function,
    ):
        self.CRITERION_FUNCTIONS[key_criterion] = function


    #        son otras formas de escribir las funciones pero es lo mimso que hicimos en stack y queue
    def show(   # def show(self) -> None : (son lo mismo)
        self
    ) -> None:
        for element in self:
            print(element)


   #eliminar 
    def delete_value(
        self,
        value,
        key_value: str = None,
    ) -> Optional[Any]:
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index

    #esta cometado porque lo podemoes hacer como una funcion o como algo mas simple.
    # def insert_value(
    #     self,
    #     value: Any,
    # ) -> None:
    #
    #    - esto es lo mas simple 
    #     # list_number.append(2)

    #  ej: for person in people:
    #       lis_people.append (person.dni) 'dni' es el criterio, siempre se lo debo de pasr, xq sino no sabe que debe ordenar

    #     # list_number.insert(1, 11)
   

   
    def sort_by_criterion( 
        self,
        criterion_key: str = None,
    ) -> None:
        #la idea para criterio es tener un diccionario de funciones, luego en base al criterio que pasa el asuario
        # a esa funcion se la paso a 'criterion', asignandole lo que esta en mayusculas que dentro contiene funciones 
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and  isinstance(self[0], (int, str, bool)): #es para cuando es un tipo de dato simple
            self.sort()
        else:
            print('criterio de orden no encontrado')

    def search(
        self,
        search_value,
        search_key: str = None,
    ) -> int:
        self.sort_by_criterion(search_key)
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end: #busqueda binaria
            #aca a criterio le paso lo qeu es un diccionario que dentro del diccionario hay funciones y dento de las funciones hay item lo cuales vamos a usar para indicar que queremos buscar
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value  < search_value:
                start = middle +1
            else:
                end = middle -1
            middle = (start + end) // 2


