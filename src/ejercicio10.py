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
    valor_return = None
    nuevo_texto = ""

    # Este loop elimina los espacio y convierte las mayúsculas en minúsculas.
    i = 0
    while i < len(texto):
        if texto[i] != ' ':
            nuevo_texto += texto[i].lower()
        i += 1

    # Este loop verifica si es palíndromo o no.
    i = 0
    j = len(nuevo_texto) - 1
    while i < len(nuevo_texto):
        if nuevo_texto[i] != nuevo_texto[j]:
            valor_return = False
        i += 1
        j -= 1

    if valor_return is None:
        valor_return = True

    return valor_return


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
