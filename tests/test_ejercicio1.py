################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio1.py` que estan en
`src`
"""

import pytest
from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_celsius


def test_convertir_a_fahrenheit():
    """
    Funcion convertir de celsius a fahrenheit
    con numero positivo.
    """
    numero = 10
    resultado = convertir_a_fahrenheit(numero)
    assert isinstance(resultado, float), "El resultado debe ser un numero real."
    assert resultado == 50, "No obtenemos el resultado esperado."


def test_convertir_a_fahrenheit_decimal():
    """
    Funcion convertir de celsius a fahrenheit
    con numero positivo con decimal.
    """
    numero = 10.5
    resultado = convertir_a_fahrenheit(numero)
    assert isinstance(resultado, float), "El resultado debe ser un numero real"
    assert resultado == 50.9, "No obtenemos el resultado esperado."


def test_convertir_a_celsius():
    """
    Funcion convertir de fahrenheit a celsius
    con numero positivo.
    """
    numero = 50
    resultado = convertir_a_celsius(numero)
    assert isinstance(resultado, float), "El resultado debe ser un numero real"
    assert resultado == 10, "No obtenemos el resultado esperado."


def test_convertir_a_celsius_decimal():
    """
    Funcion convertir de fahrenheit a celsius
    con numero positivo con decimal.
    """
    numero = 50.9
    resultado = convertir_a_celsius(numero)
    assert isinstance(resultado, float), "El resultado debe ser un numero real"
    assert resultado == 10.5, "No obtenemos el resultado esperado."
