################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio10.py` que estan en
`src`
"""

import pytest
from src.ejercicio10 import es_palindromo


def test_es_palindromo_sin_espacio_y_mayusculas():
    """
    Funcion es_palindromo con una palabra sin mayusuca y espacios.
    """
    frase = "neuquen"
    resultado = es_palindromo(frase)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico."
    assert resultado == True, "No obtenemos el resultado esperado."


def test_es_palindromo_sin_espacio_con_mayusculas():
    """
    Funcion es_palindromo con una palabra sin espacios pero
    con mayúsculas.
    """
    frase = "Neuquen"
    resultado = es_palindromo(frase)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico."
    assert resultado == True, "No obtenemos el resultado esperado."


def test_es_palindromo_con_espacio_sin_mayusculas():
    """
    Funcion es_palindromo con una palabra sin mayúsculas pero
    con espacios.
    """
    frase = "arriba la birra"
    resultado = es_palindromo(frase)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico."
    assert resultado == True, "No obtenemos el resultado esperado."


def test_es_palindromo_con_espacio_y_mayusculas():
    """
    Funcion es_palindromo con una palabra con mayúsculas y espacios.
    """
    frase = "Arriba la birra"
    resultado = es_palindromo(frase)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico."
    assert resultado == True, "No obtenemos el resultado esperado."


def test_es_palindromo_con_numeros():
    """
    Funcion es_palindromo con una palabra con numeros.
    """
    frase = "12321"
    resultado = es_palindromo(frase)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico."
    assert resultado == True, "No obtenemos el resultado esperado."


def test_es_palindromo_con_numeros_no_palindromo():
    """
    Funcion es_palindromo con una palabra con numeros.
    """
    frase = "123213"
    resultado = es_palindromo(frase)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico."
    assert resultado == False, "No obtenemos el resultado esperado."

