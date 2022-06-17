################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números

Escribir una función que utilizando sumas y restas,
reciba dos valores y retorne:
 * Retornar `-1` si el primero es menor que el segundo
 * Retornar `0` si son iguales
 * Retornar `1` si el primero es mayor que el segundo
"""


def compara(numero_1, numero_2):
    """
    Recibe dos números enteros y retorna:

    -1 si el primero es menor que el segundo.
    0 si son iguales.
    1 si el primero es mayor que el segundo.
    """
    auxiliar = (numero_1 + numero_2 + abs(numero_1 - numero_2)) - numero_1

    if auxiliar != numero_1:
        valor_temp = -1    # El primer número es MENOR que el segundo.
    elif (numero_1 + numero_2) == (numero_1 + numero_1):
        valor_temp = 0    # Ambos números son IGUALES.
    elif auxiliar == numero_1:
        valor_temp = 1    # El primer número es MAYOR que el segundo.

    return valor_temp


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese el primer número: ", end='')
    numero_entrada_1 = int(input())
    print("Ingrese el segundo número: ", end='')
    numero_entrada_2 = int(input())

    valor_salida = compara(numero_entrada_1, numero_entrada_2)

    if valor_salida == -1:
        print(f"\nEl primer número es MENOR que el segundo. \
{numero_entrada_1} < {numero_entrada_2}")
    elif valor_salida == 0:
        print(f"\nAmbos números son iguales. \
{numero_entrada_1} == {numero_entrada_2}")
    elif valor_salida == 1:
        print(f"\nEl primer número es MAYOR que el segundo. \
{numero_entrada_1} > {numero_entrada_2}")


if __name__ == "__main__":
    principal()
