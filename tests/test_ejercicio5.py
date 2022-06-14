################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio4.py` que estan en
`src`
"""

import pytest
from src.ejercicio5 import division_lenta


def test_division_lenta_positivo():
    """
    Funcion división lenta con 2 números positivos.
    """
    numero1 = 6
    numero2 = 2
    resultado1, resultado2 = division_lenta(numero1, numero2)
    assert isinstance(resultado1, int), "El resultado debe ser un numero entero."
    assert isinstance(resultado2, int), "El resultado debe ser un numero entero."
    assert resultado1 == 3, "No obtenemos el resultado esperado."
    assert resultado2 == 0, "No obtenemos el resultado esperado."


def test_division_lenta_negativo_positivo():
    """
    Funcion división lenta con el primer número negativo
    y el segundo positivo.
    """
    numero1 = -6
    numero2 = 2
    resultado1, resultado2 = division_lenta(numero1, numero2)
    assert isinstance(resultado1, int), "El resultado debe ser un numero entero."
    assert isinstance(resultado2, int), "El resultado debe ser un numero entero."
    assert resultado1 == -3, "No obtenemos el resultado esperado."
    assert resultado2 == 0, "No obtenemos el resultado esperado."


def test_division_lenta_positivo_negativo():
    """
    Funcion división lenta con el primer número positivo
    y el segundo negativo.
    """
    numero1 = 6
    numero2 = -2
    resultado1, resultado2 = division_lenta(numero1, numero2)
    assert isinstance(resultado1, int), "El resultado debe ser un numero entero."
    assert isinstance(resultado2, int), "El resultado debe ser un numero entero."
    assert resultado1 == -3, "No obtenemos el resultado esperado."
    assert resultado2 == 0, "No obtenemos el resultado esperado."


def test_division_lenta_negativo():
    """
    Funcion división lenta con 2 números negativos.
    """
    numero1 = -6
    numero2 = -2
    resultado1, resultado2 = division_lenta(numero1, numero2)
    assert isinstance(resultado1, int), "El resultado debe ser un numero entero."
    assert isinstance(resultado2, int), "El resultado debe ser un numero entero."
    assert resultado1 == 3, "No obtenemos el resultado esperado."
    assert resultado2 == 0, "No obtenemos el resultado esperado."


def test_division_lenta_cero_divisor():
    """
    Funcion división lenta con cero en el divisor.
    """
    numero1 = 5
    numero2 = 0
    resultado = division_lenta(numero1, numero2)
    assert isinstance(resultado, ZeroDivisionError), "El resultado debe ser un error."


def test_division_lenta_positivo_con_resto():
    """
    Funcion división lenta con 2 números positivos con
    resto en el resultado.
    """
    numero1 = 11
    numero2 = 3
    resultado1, resultado2 = division_lenta(numero1, numero2)
    assert isinstance(resultado1, int), "El resultado debe ser un numero entero."
    assert isinstance(resultado2, int), "El resultado debe ser un numero entero."
    assert resultado1 == 3, "No obtenemos el resultado esperado."
    assert resultado2 == 2, "No obtenemos el resultado esperado."


def test_division_lenta_positivo_sin_cociente_con_resto():
    """
    Funcion división lenta con 2 números positivos con
    resto en el resultado y sin cociente.
    """
    numero1 = 3
    numero2 = 11
    resultado1, resultado2 = division_lenta(numero1, numero2)
    assert isinstance(resultado1, int), "El resultado debe ser un numero entero."
    assert isinstance(resultado2, int), "El resultado debe ser un numero entero."
    assert resultado1 == 0, "No obtenemos el resultado esperado."
    assert resultado2 == 3, "No obtenemos el resultado esperado."


def test_division_lenta_cero_dividendo():
    """
    Funcion división lenta con cero en el dividendo.
    """
    numero1 = 0
    numero2 = 5
    resultado1, resultado2 = division_lenta(numero1, numero2)
    assert isinstance(resultado1, int), "El resultado debe ser un numero entero."
    assert isinstance(resultado2, int), "El resultado debe ser un numero entero."
    assert resultado1 == 0, "No obtenemos el resultado esperado."
    assert resultado2 == 0, "No obtenemos el resultado esperado."
