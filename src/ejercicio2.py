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

    2 si es positivo.
    1 si es cero.
    0 si es negativo.
    """

    if 1 + (numero // (2 ** 50)) - (-numero // (2 ** 50)) == 2:
        valor_temp = "positivo"    # Si la formula es igual a 2, entonces es positivo.
    elif 1 + (numero // (2 ** 50)) - (-numero // (2 ** 50)) == 1:
        valor_temp = "cero"    # Si la formula es igual a 1, entonces es cero.
    elif 1 + (numero // (2 ** 50)) - (-numero // (2 ** 50)) == 0:
        valor_temp = "negativo"    # Si la formula es igual a 0, entonces es negativo.

    return valor_temp


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese un número: ", end='')
    numero_entrada = int(input())

    valor_salida = signo(numero_entrada)

    if valor_salida == "positivo":
        print(f"\nEl número {numero_entrada} es positivo.")
    elif valor_salida == "cero":
        print(f"\nEl número {numero_entrada} es cero.")
    elif valor_salida == "negativo":
        print(f"\nEl número {numero_entrada} es negativo.")


if __name__ == "__main__":
    principal()
