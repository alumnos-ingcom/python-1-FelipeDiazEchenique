################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de

Escribir una función que indique con `True` si un número
entero es multiplo de otro, utilizando sumas y restas.
"""


def es_multiplo(numero, multiplo):
    """
    Recibe 2 números enteros y retorna:
    * True, si un número entero es multiplo de otro.
    * False, si un número entero NO es multiplo de otro
    """
    valor_return = True

    numero = abs(numero)
    multiplo = abs(multiplo)

    suma = multiplo
    while multiplo < numero:
        multiplo += suma

    if multiplo > numero:
        valor_return = False

    return valor_return


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese un número: ", end='')
    numero_entrada = int(input())
    print("Ingrese el múltiplo: ", end='')
    multiplo_entrada = int(input())

    if es_multiplo(numero_entrada, multiplo_entrada):
        print(f"\n{multiplo_entrada} es múltiplo de {numero_entrada}.")
    else:
        print(f"\n{multiplo_entrada} NO es múltiplo de {numero_entrada}.")


if __name__ == "__main__":
    principal()
