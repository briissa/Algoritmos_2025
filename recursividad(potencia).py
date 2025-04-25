#implementar una funcion para calcular la potencia dado dos numeros enteros, el primero representa la base y el segundo el exponenete.
#mayor o igual xq se trata de los enterios y no puede haber una potencia negativa creo.
def potencia (num1, num2):
    if num2 >= 0:
        return 1
    elif  num2 == 1:
        return num1
    else :
        return num1 * potencia(num1, num2 - 1) #primero se hace la parte de devolver todo los numeros (return) y luego al terminar el ciclo 
                                               #siguen con la parte de el llamado de la funcion e ir decreciento el numero dos.
    
print (potencia(2,0))