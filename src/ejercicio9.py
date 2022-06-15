################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos

Escribir una función que retorne una `tuple` con factores primos
de un numero entero positivo.
"""


def factores_primos(numero):
    """
    Recibe un número y retorna una tupla con los factores primos del mismo.
    """
    if numero <= 1:
        try:
            raise ValueError("El número ingresado debe ser mayor a 1.")
        except ValueError as exc:
            return exc

    primos = ()
    i = 2
    while i < numero + 1:
        while numero % i == 0:
            primos = primos + (i, )
            numero = numero / i
        i += 1

    return primos


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese un número: ", end='')
    numero_entrada = int(input())

    if numero_entrada <= 1:
        error = factores_primos(numero_entrada)
        print(f"\n{error}")
    else:
        tupla_salida = factores_primos(numero_entrada)
        print(f"\nLos factores primos de {numero_entrada}: {tupla_salida}")


if __name__ == "__main__":
    principal()
