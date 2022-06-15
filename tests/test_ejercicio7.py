################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio7.py` que estan en
`src`
"""

import pytest
from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal


def test_sexadecimal_a_decimal_positivo():
    """
    Funcion sexadecimal a decimal con numeros enteros positivos.
    """
    numero1 = 10
    numero2 = 10
    numero3 = 10
    resultado = sexadecimal_a_decimal(numero1, numero2, numero3)
    assert isinstance(resultado, int), "El resultado debe ser un entero."
    assert resultado == 36610, "No obtenemos el resultado esperado."


def test_sexadecimal_a_decimal_todo_cero():
    """
    Funcion sexadecimal a decimal con todos los números en cero.
    """
    numero1 = 0
    numero2 = 0
    numero3 = 0
    resultado = sexadecimal_a_decimal(numero1, numero2, numero3)
    assert isinstance(resultado, int), "El resultado debe ser un entero."
    assert resultado == 0, "No obtenemos el resultado esperado."


def test_sexadecimal_a_decimal_horas_negativas():
    """
    Funcion sexadecimal a decimal con horas negativas.
    """
    numero1 = -10
    numero2 = 10
    numero3 = 10
    resultado = sexadecimal_a_decimal(numero1, numero2, numero3)
    assert isinstance(resultado, ValueError), "El resultado debe ser un error."


def test_sexadecimal_a_decimal_minutos_negativo():
    """
    Funcion sexadecimal a decimal con minutos negativos.
    """
    numero1 = 10
    numero2 = -10
    numero3 = 10
    resultado = sexadecimal_a_decimal(numero1, numero2, numero3)
    assert isinstance(resultado, ValueError), "El resultado debe ser un error."


def test_sexadecimal_a_decimal_segundos_negativos():
    """
    Funcion sexadecimal a decimal con minutos negativos.
    """
    numero1 = 10
    numero2 = 10
    numero3 = -10
    resultado = sexadecimal_a_decimal(numero1, numero2, numero3)
    assert isinstance(resultado, ValueError), "El resultado debe ser un error."


def test_sexadecimal_a_decimal_todo_negativos():
    """
    Funcion sexadecimal a decimal con todos números enteros negativos.
    """
    numero1 = -10
    numero2 = -10
    numero3 = -10
    resultado = sexadecimal_a_decimal(numero1, numero2, numero3)
    assert isinstance(resultado, ValueError), "El resultado debe ser un error."


def test_decimal_a_sexadecimal_positivo():
    """
    Funcion decimal a sexadecimal con un número entero positivo.
    """
    numero = 36610
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (10, 10, 10), "No obtenemos el resultado esperado."


def test_decimal_a_sexadecimal_negativo():
    """
    Funcion decimal a sexadecimal con un número entero positivo.
    """
    numero = -36610
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(resultado, ValueError), "El resultado debe ser un error."


def test_decimal_a_sexadecimal_cero():
    """
    Funcion decimal a sexadecimal con número cero.
    """
    numero = 0
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (0, 0, 0), "No obtenemos el resultado esperado."