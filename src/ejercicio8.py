################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos

Escribir una función que indique con `True` si un numero indicado es Primo.
"""


def es_primo(numero):
    """
    Recibe un número y retorna:
    * True, si es un número primo.
    * False, si NO es un número primo.
    """
    if numero <= 1:
        try:
            raise ValueError("\nEl número ingresado debe ser mayor a 1.")
        except ValueError as exc:
            print(exc)

    valor_return = None
    contador = 2
    while contador < numero:
        if numero % contador == 0:
            valor_return = False
        contador += 1

    if valor_return is None:
        valor_return = True

    return valor_return


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese un número: ", end='')
    numero_entrada = int(input())

    if es_primo(numero_entrada):
        print("\nEs número primo.")
    else:
        print("\nNO es número primo.")


if __name__ == "__main__":
    principal()
