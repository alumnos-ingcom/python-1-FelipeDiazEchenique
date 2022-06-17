################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio4.py` que estan en
`src`
"""

import pytest
from src.ejercicio4 import suma_lenta


def test_suma_lenta_positivo():
    """
    Funcion suma lenta con 2 números positivos.
    """
    numero1 = 5
    numero2 = 4
    resultado = suma_lenta(numero1, numero2)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == 9, "No obtenemos el resultado esperado."


def test_suma_lenta_negativo():
    """
    Funcion suma lenta con 2 números negativos.
    """
    numero1 = -5
    numero2 = -4
    resultado = suma_lenta(numero1, numero2)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == -9, "No obtenemos el resultado esperado."


def test_suma_lenta_positivo_negativo():
    """
    Funcion suma lenta con un número positivo y el otro negativo.
    """
    numero1 = 5
    numero2 = -4
    resultado = suma_lenta(numero1, numero2)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == 1, "No obtenemos el resultado esperado."


def test_suma_lenta_negativo_positivo():
    """
    Funcion suma lenta con un número negativo y el otro positivo.
    """
    numero1 = -5
    numero2 = 4
    resultado = suma_lenta(numero1, numero2)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == -1, "No obtenemos el resultado esperado."


def test_suma_lenta_cero():
    """
    Funcion suma lenta con ambos números en 0.
    """
    numero1 = 0
    numero2 = 0
    resultado = suma_lenta(numero1, numero2)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == 0, "No obtenemos el resultado esperado."

