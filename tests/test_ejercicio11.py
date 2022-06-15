################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio11.py` que estan en
`src`
"""

import pytest
from src.ejercicio11 import es_multiplo


def test_es_multiplo_positivos_true():
    """
    Funcion es_multiplo con 2 numeros positivos multiplos.
    """
    numero1 = 10
    numero2 = 5
    resultado = es_multiplo(numero1, numero2)
    assert isinstance(resultado, bool), "El resultado debe ser una tupla."
    assert resultado == True, "No obtenemos el resultado esperado."


def test_es_multiplo_positivos_false():
    """
    Funcion es_multiplo con 2 numeros positivos no multiplos.
    """
    numero1 = 10
    numero2 = 7
    resultado = es_multiplo(numero1, numero2)
    assert isinstance(resultado, bool), "El resultado debe ser una tupla."
    assert resultado == False, "No obtenemos el resultado esperado."


def test_es_multiplo_positivos_y_negativo():
    """
    Funcion es_multiplo con un numero positivo y
    el otro negativo.
    """
    numero1 = 10
    numero2 = -5
    resultado = es_multiplo(numero1, numero2)
    assert isinstance(resultado, bool), "El resultado debe ser una tupla."
    assert resultado == True, "No obtenemos el resultado esperado."


def test_es_multiplo_negativo_y_positivos():
    """
    Funcion es_multiplo con un numero negativo y
    el otro positivo.
    """
    numero1 = -10
    numero2 = 5
    resultado = es_multiplo(numero1, numero2)
    assert isinstance(resultado, bool), "El resultado debe ser una tupla."
    assert resultado == True, "No obtenemos el resultado esperado."


def test_es_multiplo_negativos():
    """
    Funcion es_multiplo con 2 números negativos.
    """
    numero1 = -10
    numero2 = -5
    resultado = es_multiplo(numero1, numero2)
    assert isinstance(resultado, bool), "El resultado debe ser una tupla."
    assert resultado == True, "No obtenemos el resultado esperado."
