# 16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1-empleados, 2-staff de tecnologías de la información “TI”, 3-gerente), y resuelva la
# siguiente situación:

# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.


from queue_ import Queue_
from heap import HeapMax



# Definición de prioridades: 3 (Gerente), 2 (TI), 1 (Empleado)
cola_impresion = HeapMax() 

print("COLA DE IMPRESION CON PRIORIDAD")

# a. cargue tres documentos de empleados (P=1)
cola_impresion.arrive( 1, "juan")
cola_impresion.arrive(1, "lucas")
cola_impresion.arrive( 1, "Domingo")
print("Cargados 3 Empleados") 


# b. imprima el primer documento de la cola.
print("\n PRIMER documento de la cola (P=1):")
if cola_impresion.size() > 0:
    documento_impreso = cola_impresion.attention() # Saca el de mayor prioridad
    # El resultado es una lista [prioridad, nombre_documento]
    print(f" Impreso: {documento_impreso[1]}") 
print(f" Restantes: {cola_impresion.size()}") 


# c. cargue dos documentos del staff de TI (P=2).
cola_impresion.arrive(2,"jose")
cola_impresion.arrive( 2,"martin")
print("Cargados 2 de TI (P=2)")

# d. cargue un documento del gerente (P=3).
cola_impresion.arrive( 3,"erne")
print(f"Cargado 1 Gerente (P=3). Tamaño: {cola_impresion.size()}")



# e. imprima los dos primeros documentos de la cola.
print("\n Imprimiendo los DOS PRIMEROS documentos:")

# Documento 1 (Debe ser el Gerente, P=3)
if cola_impresion.size() > 0:
    doc_1 = cola_impresion.attention()
    print(f"  -> 1er Impreso: {doc_1[1]} (P={doc_1[0]})")
else:
    print("La cola está vacía para el 1er documento.")
    
# Documento 2 (Debe ser uno de TI, P=2)
if cola_impresion.size() > 0:
    doc_2 = cola_impresion.attention()
    print(f" 2do Impreso: {doc_2[1]} (doc= {doc_2[0]})")
else:
    print("La cola solo tenía un documento.")

print(f"  Restantes: {cola_impresion.size()}")



# f. cargue dos documentos de empleados (P=1) y uno de gerente (P=3).
cola_impresion.arrive( 1,"luucc")
cola_impresion.arrive( 1,"max")
cola_impresion.arrive(3,"josse")
print("Cargados 2 Empleados (P=1) y 1 Gerente (P=3)")


# g. imprima todos los documentos de la cola de impresión.
print("\n Imprimiendo TODOS los documentos restantes:")

contador = 1
while cola_impresion.size() > 0:
    documento_impreso = cola_impresion.attention()
    print(f" {contador}: {documento_impreso[1]} (P={documento_impreso[0]})")
    contador += 1
    
print("Cola vacia")
