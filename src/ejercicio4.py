################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta

Escribir una función que haga la suma entre dos números
enteros sin hacer la operación de manera directa. Esto quiere
decir que para hacer la suma entre 4 y 3, las operaciones
resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""


def suma_lenta(numero_1, numero_2):
    """
    Recibe dos números enteros y retorna el resultado de la suma lenta.
    """

    suma = numero_1
    contador = numero_2

    print(f"\n{suma} ", end='')

    if numero_2 > 0:
        # Suma lenta para números positivos.
        while contador > 0:
            suma += 1
            contador -= 1
            print(f"+ 1 ", end='')

    else:
        # Suma lenta para números negativos
        while contador < 0:
            suma -= 1
            contador += 1
            print(f"- 1 ", end='')

    return suma


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese el primer número: ", end='')
    numero_entrada_1 = int(input())
    print("Ingrese el segundo número: ", end='')
    numero_entrada_2 = int(input())

    valor_salida = suma_lenta(numero_entrada_1, numero_entrada_2)

    print(f"= {valor_salida}")


if __name__ == "__main__":
    principal()
