################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas

Se quiere transformar temperaturas en grados fahrenheit a
grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados
centigrados en fahrenheit como un número decimal, utilice esta
formula para calcular los grados centígrados y retorne el
resultado obtenido. Y viceversa.
"""


def convertir_a_fahrenheit(celsius):
    """
    Recibe un número en grados celsius y lo retorna a grados fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32

    return fahrenheit


def convertir_a_celsius(fahrenheit):
    """
    Recibe un número en grados fahrenheit y lo retorna a grados celsius.
    """
    celsius = (fahrenheit - 32) * 5/9

    return celsius


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Primero de celsius a fahrenheit
    print("Ingrese los grados celsius: ", end='')
    celsius_entrada = float(input())

    fahrenheit_salida = convertir_a_fahrenheit(celsius_entrada)

    print(f"{celsius_entrada:.1f}° C = {fahrenheit_salida:.1f}° F")

    # Segundo de fahrenheit a celsius
    print("Ingrese los grados fahrenheit: ", end='')
    fahrenheit_entrada = float(input())

    celsius_salida = convertir_a_celsius(fahrenheit_entrada)

    print(f"{fahrenheit_entrada:.1f}° F = {celsius_salida:.1f}° C")


if __name__ == "__main__":
    principal()
