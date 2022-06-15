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
            raise ValueError("El número ingresado debe ser mayor a 1.")
        except ValueError as exc:
            return exc

    contador = 2
    while contador < numero:
        if numero % contador == 0:
            return False
        contador += 1

    return True


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese un número: ", end='')
    numero_entrada = int(input())

    if numero_entrada <= 1:
        error = es_primo(numero_entrada)
        print(f"\n{error}")
    else:
        if es_primo(numero_entrada):
            print("\nEs número primo.")
        else:
            print("\nNO es número primo.")


if __name__ == "__main__":
    principal()
