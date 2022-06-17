################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio3.py` que estan en
`src`
"""

import pytest
from src.ejercicio3 import compara


def test_compara_menor_mayor():
    """
    Funcion compara con el primer numero menor y segundo mayor.
    """
    numero1 = 5
    numero2 = 10
    resultado = compara(numero1, numero2)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == -1, "No obtenemos el resultado esperado."


def test_compara_igual():
    """
    Funcion compara con el primer numero igual al segundo.
    """
    numero1 = 5
    numero2 = 5
    resultado = compara(numero1, numero2)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == 0, "No obtenemos el resultado esperado."


def test_compara_mayor_menor():
    """
    Funcion compara con el primer numero mayor y segundo menor.
    """
    numero1 = 10
    numero2 = 5
    resultado = compara(numero1, numero2)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == 1, "No obtenemos el resultado esperado."


def test_compara_mayor_menor_negativo():
    """
    Funcion compara con el primer numero mayor y segundo menor.
    Ambos negativos.
    """
    numero1 = -5
    numero2 = -10
    resultado = compara(numero1, numero2)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == 1, "No obtenemos el resultado esperado."


def test_compara_menor_mayor_negativo():
    """
    Funcion compara con el primer numero menor y segundo mayor.
    Ambos negativos.
    """
    numero1 = -10
    numero2 = -5
    resultado = compara(numero1, numero2)
    assert isinstance(resultado, int), "El resultado debe ser un numero real."
    assert resultado == -1, "No obtenemos el resultado esperado."
