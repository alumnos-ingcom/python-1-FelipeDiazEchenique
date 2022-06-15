################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo

Escribir una función que indique con True si una palabra o frase
ingresada se trata de un palindromo. Palíndromo, es si se lee igual
de derecha a izquierda que de izquierda a derecha.
"""


def es_palindromo(texto):
    """
    Recibe una cadena de caracteres y retorna:
    * True, si es palíndromo.
    * False, si NO es palíndromo.
    """
    texto_modificado = texto.lower()
    texto_modificado = texto_modificado.replace(" ", "")

    if texto_modificado == texto_modificado[::-1]:
        return True

    return False


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese una palabra o frase: ", end='')
    texto_entrada = str(input())

    if es_palindromo(texto_entrada):
        print("\nEs palíndromo")
    else:
        print("\nNO es palíndromo")


if __name__ == "__main__":
    principal()
