################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio6.py` que estan en
`src`
"""

import pytest
from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor


def test_ordenar_mayor_a_menor_ordenados_3_2_1():
    """
    Funcion ordenar de mayor a menor con números positivos
    ordenados 3, 2, 1.
    """
    numero1 = 3
    numero2 = 2
    numero3 = 1
    resultado = ordenar_mayor_a_menor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (3, 2, 1), "No obtenemos el resultado esperado."


def test_ordenar_mayor_a_menor_ordenados_3_1_2():
    """
    Funcion ordenar de mayor a menor con números positivos
    ordenados 3, 1, 2.
    """
    numero1 = 3
    numero2 = 1
    numero3 = 2
    resultado = ordenar_mayor_a_menor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (3, 2, 1), "No obtenemos el resultado esperado."


def test_ordenar_mayor_a_menor_ordenados_2_1_3():
    """
    Funcion ordenar de mayor a menor con números positivos
    ordenados 2, 1, 3.
    """
    numero1 = 2
    numero2 = 1
    numero3 = 3
    resultado = ordenar_mayor_a_menor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (3, 2, 1), "No obtenemos el resultado esperado."


def test_ordenar_mayor_a_menor_ordenados_2_3_1():
    """
    Funcion ordenar de mayor a menor con números positivos
    ordenados 2, 3, 1.
    """
    numero1 = 2
    numero2 = 3
    numero3 = 1
    resultado = ordenar_mayor_a_menor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (3, 2, 1), "No obtenemos el resultado esperado."


def test_ordenar_mayor_a_menor_ordenados_1_2_3():
    """
    Funcion ordenar de mayor a menor con números positivos
    ordenados 1, 2, 3.
    """
    numero1 = 1
    numero2 = 2
    numero3 = 3
    resultado = ordenar_mayor_a_menor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (3, 2, 1), "No obtenemos el resultado esperado."


def test_ordenar_mayor_a_menor_ordenados_1_3_2():
    """
    Funcion ordenar de mayor a menor con números positivos
    ordenados 1, 3, 2.
    """
    numero1 = 1
    numero2 = 3
    numero3 = 2
    resultado = ordenar_mayor_a_menor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (3, 2, 1), "No obtenemos el resultado esperado."


def test_ordenar_menor_a_mayor_ordenados_3_2_1():
    """
    Funcion ordenar de menor a mayor con números positivos
    ordenados 3, 2, 1.
    """
    numero1 = 3
    numero2 = 2
    numero3 = 1
    resultado = ordenar_menor_a_mayor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (1, 2, 3), "No obtenemos el resultado esperado."


def test_ordenar_menor_a_mayor_ordenados_3_1_2():
    """
    Funcion ordenar de menor a mayor con números positivos
    ordenados 3, 1, 2.
    """
    numero1 = 3
    numero2 = 1
    numero3 = 2
    resultado = ordenar_menor_a_mayor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (1, 2, 3), "No obtenemos el resultado esperado."


def test_ordenar_menor_a_mayor_ordenados_2_1_3():
    """
    Funcion ordenar de menor a mayor con números positivos
    ordenados 2, 1, 3.
    """
    numero1 = 2
    numero2 = 1
    numero3 = 3
    resultado = ordenar_menor_a_mayor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (1, 2, 3), "No obtenemos el resultado esperado."


def test_ordenar_menor_a_mayor_ordenados_2_3_1():
    """
    Funcion ordenar de menor a mayor con números positivos
    ordenados 2, 3, 1.
    """
    numero1 = 2
    numero2 = 3
    numero3 = 1
    resultado = ordenar_menor_a_mayor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (1, 2, 3), "No obtenemos el resultado esperado."


def test_ordenar_menor_a_mayor_ordenados_1_2_3():
    """
    Funcion ordenar de menor a mayor con números positivos
    ordenados 1, 2, 3.
    """
    numero1 = 1
    numero2 = 2
    numero3 = 3
    resultado = ordenar_menor_a_mayor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (1, 2, 3), "No obtenemos el resultado esperado."


def test_ordenar_menor_a_mayor_ordenados_1_3_2():
    """
    Funcion ordenar de menor a mayor con números positivos
    ordenados 1, 3, 2.
    """
    numero1 = 1
    numero2 = 3
    numero3 = 2
    resultado = ordenar_menor_a_mayor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "El resultado debe ser un una tupla."
    assert resultado == (1, 2, 3), "No obtenemos el resultado esperado."
