################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos

Escribir una función que reciba un número e indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.
"""


def signo(numero):
    """
    Recibe un número entero y retorna:

    1, si es positivo.
    0, si es cero.
    -1, si es negativo.
    """
    auxiliar = (numero + abs(numero)) - numero

    if auxiliar != numero:
        valor_temp = -1    # El número es negativo.
    elif (auxiliar + auxiliar) == (auxiliar + 0):
        valor_temp = 0    # El número es cero.
    elif auxiliar == numero:
        valor_temp = 1    # El número es positivo.

    return valor_temp


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese un número: ", end='')
    numero_entrada = int(input())

    valor_salida = signo(numero_entrada)

    if valor_salida == 1:
        print(f"\nEl número {numero_entrada} es positivo.")
    elif valor_salida == 0:
        print(f"\nEl número {numero_entrada} es cero.")
    elif valor_salida == -1:
        print(f"\nEl número {numero_entrada} es negativo.")


if __name__ == "__main__":
    principal()
