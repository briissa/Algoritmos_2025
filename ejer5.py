#5. Desarrollar una función que permita convertir un número romano en un número decimal.


def romano_a_decimal(romano):
    # Diccionario con los valores de los números romanos
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    #si la longitud de la cadena es 1, devolvemos su valor directamente
    if len(romano) == 1:
        return valores[romano[0]]

    # Obtener el valor del carácter actual y el siguiente pere despues poder sumar o restar
    actual = valores[romano[0]]
    siguiente = valores[romano[1]]
    #esta parte la va a hacer recursivamente, por eso llamamos a la funcion dentro de la misma


    # Si el valor actual es menor que el siguiente, se resta, sino se suma.(haci es con los romanos)
    if actual < siguiente:
        return -actual + romano_a_decimal(romano[1:])
    else:
        return actual + romano_a_decimal(romano[1:])


print("ingrese el numero romano que quiere convertir")
romano = input() #debo ingresar mayusculas
resultado = romano_a_decimal(romano) #a lo que me devuelme mi funcion, se lo asigno a resultado
print(f"El número romano {romano} equivale a {resultado} en decimal.")