################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio2.py` que estan en
`src`
"""

import pytest
from src.ejercicio2 import signo


def test_signo_positivo():
    """
    Funcion signo con número posivo.
    """
    numero = 5
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == 1, "No obtenemos el resultado esperado."


def test_signo_negativo():
    """
    Funcion signo con número negativo.
    """
    numero = -5
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == -1, "No obtenemos el resultado esperado."


def test_signo_cero():
    """
    Funcion signo con número cero.
    """
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == 0, "No obtenemos el resultado esperado."


def test_signo_positivo_decimal():
    """
    Funcion signo con número posivo con decimal.
    """
    numero = 5.5
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == 1, "No obtenemos el resultado esperado."

