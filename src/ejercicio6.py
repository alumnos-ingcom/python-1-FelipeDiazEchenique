################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores

Escribir una función que a partir de tres variables de tipo entero retorne
una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""


def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Recibe 3 numeros enteros y retorna una tupla con los números
    ordenados de mayor a menor.
    """
    if uno > dos:
        if uno > tres:
            if dos > tres:
                mayor_a_menor = (uno, dos, tres)
            else:
                mayor_a_menor = (uno, tres, dos)
        else:
            mayor_a_menor = (tres, uno, dos)
    else:
        if dos > tres:
            if uno > tres:
                mayor_a_menor = (dos, uno, tres)
            else:
                mayor_a_menor = (dos, tres, uno)
        else:
            mayor_a_menor = (tres, dos, uno)

    return mayor_a_menor


def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Recibe 3 numeros enteros y retorna una tupla con los números
    ordenados de menor a mayor.
    """
    if uno < dos:
        if uno < tres:
            if dos < tres:
                menor_a_mayor = (uno, dos, tres)
            else:
                menor_a_mayor = (uno, tres, dos)
        else:
            menor_a_mayor = (tres, uno, dos)
    else:
        if dos < tres:
            if uno < tres:
                menor_a_mayor = (dos, uno, tres)
            else:
                menor_a_mayor = (dos, tres, uno)
        else:
            menor_a_mayor = (tres, dos, uno)

    return menor_a_mayor


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese primer número: ", end='')
    numero_entrada_1 = int(input())
    print("Ingrese segundo número: ", end='')
    numero_entrada_2 = int(input())
    print("Ingrese tercer número: ", end='')
    numero_entrada_3 = int(input())

    tupla_mayor = ordenar_mayor_a_menor(numero_entrada_1, numero_entrada_2,
                                        numero_entrada_3)
    print(f"\nMayor a menor = {tupla_mayor}")

    tupla_menor = ordenar_menor_a_mayor(numero_entrada_1, numero_entrada_2,
                                        numero_entrada_3)
    print(f"Menor a mayor = {tupla_menor}")


if __name__ == "__main__":
    principal()
