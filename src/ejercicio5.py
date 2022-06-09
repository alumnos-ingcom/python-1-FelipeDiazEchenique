################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones

Escribir una función que mediante restas sucesivas, obtenga el valor del
cociente y resto de dos números enteros.
"""

import sys


def division_lenta(dividendo, divisor):
    """
    Recibe dos números enteros y retorna el cociente y el resto de los mismos.
    """

    try:
        dividendo/divisor
    except ZeroDivisionError as error:
        print(f"\nError al ingresar {divisor} como divisor.\
                \nZeroDivisionError: {error}")
        sys.exit()

    cociente = 0

    # Dividendo y Divisor positivos.
    if dividendo > 0 and divisor > 0:
        while dividendo >= divisor:
            dividendo -= divisor
            cociente += 1

    # Dividendo y Divisor negativos.
    elif dividendo < 0 and divisor < 0:
        dividendo = abs(dividendo)
        divisor = abs(divisor)

        while dividendo >= divisor:
            dividendo -= divisor
            cociente += 1

    # Dividendo positivo y Divisor negativo (viceversa).
    elif dividendo < 0 or divisor < 0:
        dividendo = abs(dividendo)
        divisor = abs(divisor)

        while dividendo >= divisor:
            dividendo -= divisor
            cociente += 1

        dividendo *= -1
        cociente *= -1

    resto = dividendo

    return cociente, resto


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese el dividendo: ", end='')
    dividendo_entrada = int(input())
    print("Ingrese el divisor: ", end='')
    divisor_entrada = int(input())

    cociente_salida, resto_salida = division_lenta(dividendo_entrada,
                                                   divisor_entrada)

    print(f"\nCociente: {cociente_salida}\tResto: {resto_salida}")


if __name__ == "__main__":
    principal()
