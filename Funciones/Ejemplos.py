"""
En este scipt de python se van a trabajar los ejemlos de funciones
desarrollados en clase, los cuales pueden utilizarse para implementar
y modificar para un mejor entendiemiento de temas.

Prof: Juan Pablo Escobar
c.c 1088343921
07/04/26
"""



def suma(a, b):
    """
    Es esta función se puede ver que la suma entre dos
    variables "a" y "b" y despues de imprimira el
    resultado del esta suma.

    Args:
        a (int): Esta variable se puede es preferiblemente un etero y es el primer valor
                 que se va ingresar para la suma. 
        b (int): Esta variable se puede es preferiblemente un etero y es el segundo valor
                 que se va ingresar para la suma.
    """
    print(a + b)

suma(5, 3)


## Calculadora:

def suma(a, b):
    """
    En este caso se va a hacer lo mismo del caso anterior pero con
    la diferencia de va a retornar el resultado de cada uno de las
    operaciones.

    Args:
        a (int): Esta variable se puede es preferiblemente un etero y es el primer valor
                 que se va ingresar para la suma. 
        b (int): Esta variable se puede es preferiblemente un etero y es el segundo valor
                 que se va ingresar para la suma.

    Returns:
        int: El resultado de la suma.
    """
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

#print(suma(5, 3))


##Fibonacci:

def fibonacci(n):
    """Esta función realiza la serie de Fibonacci, buscando realizar
       lo de manera recursiva, es decir, la función se llama a sí misma,
       para obtener el resultado de la serie.

    Args:
        n (int): La posición en la serie de Fibonacci que se desea calcular.

    Returns:
        int: El número de Fibonacci en la posición n.
    """

    if not isinstance(n, int):
        raise TypeError(f"Error: Se esperaba un 'int', pero se recibió {type(n)}")

    # Caso base: si n es 0 o 1, devolvemos n directamente
    if n <= 1:
        return n
    else:
        # La función se llama a sí misma dos veces (Recursión)
        return fibonacci(n - 1) + fibonacci(n - 2)
    



posicion = input("Ingrese un valor en donde se va a calcular el numero de Fibonacci: ")
resultado = fibonacci(posicion)
print(f"El número de Fibonacci en la posición {posicion} es: {resultado}")