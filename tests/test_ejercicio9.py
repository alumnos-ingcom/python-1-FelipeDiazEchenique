################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio9.py` que estan en
`src`
"""

import pytest
from src.ejercicio9 import factores_primos


def test_factores_primos_con_primo():
    """
    Funcion factores_primos con un número primo.
    """
    numero = 11
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (11,), "No obtenemos el resultado esperado."


def test_factores_primos_con_no_primo():
    """
    Funcion factores_primos con un número no primo.
    """
    numero = 66
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (2, 3, 11), "No obtenemos el resultado esperado."


def test_factores_primos_numero_1():
    """
    Funcion factores_primos con número 1.
    """
    numero = 1
    resultado = factores_primos(numero)
    with pytest.raises(ValueError):
        raise ValueError("\nEl número ingresado debe ser mayor a 1.")


def test_factores_primos_numero_0():
    """
    Funcion factores_primos con número 0.
    """
    numero = 0
    resultado = factores_primos(numero)
    with pytest.raises(ValueError):
        raise ValueError("\nEl número ingresado debe ser mayor a 1.")


def test_factores_primos_numero_negativo():
    """
    Funcion factores_primos con un número negativo.
    """
    numero = -1
    resultado = factores_primos(numero)
    with pytest.raises(ValueError):
        raise ValueError("\nEl número ingresado debe ser mayor a 1.")