################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio8.py` que estan en
`src`
"""

import pytest
from src.ejercicio8 import es_primo


def test_es_primo_numero_primo():
    """
    Funcion es_primo con un número primo.
    """
    numero = 11
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico."
    assert resultado == True, "No obtenemos el resultado esperado."


def test_es_primo_numero_no_primo():
    """
    Funcion es_primo con un número no primo.
    """
    numero = 10
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico."
    assert resultado == False, "No obtenemos el resultado esperado."


def test_es_primo_numero_1():
    """
    Funcion es_primo con número 1.
    """
    numero = 1
    resultado = es_primo(numero)
    with pytest.raises(ValueError):
        raise ValueError("\nEl número ingresado debe ser mayor a 1.")


def test_es_primo_numero_0():
    """
    Funcion es_primo con número 0.
    """
    numero = 0
    resultado = es_primo(numero)
    with pytest.raises(ValueError):
        raise ValueError("\nEl número ingresado debe ser mayor a 1.")


def test_es_primo_numero_negativo():
    """
    Funcion es_primo con un número negativo.
    """
    numero = -1
    resultado = es_primo(numero)
    with pytest.raises(ValueError):
        raise ValueError("\nEl número ingresado debe ser mayor a 1.")
