################
# Felipe Díaz Echenique - @FelipeDiazEchenique
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número

Escribir un programa que permita transformar un número
solicitado expresado en grados, minutos y segundos a segundos a segundos.
Y otra que haga el cambio en el sentido contrario, devolviendo una `tuple`.
"""


def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Recibe 3 números enteros positivos (horas, minutos y segundos)
    y retorna la conversión del total a segundos.
    """
    if horas < 0 or minutos < 0 or segundos < 0:
        try:
            raise ValueError("\nError al ingresar un valor negativo.")
        except ValueError as exc:
            print(exc)

    segundos_total = 0

    segundos_total += horas * 3600
    segundos_total += minutos * 60
    segundos_total += segundos

    return segundos_total


def decimal_a_sexadecimal(numero):
    """
    Recibe un número entero positivo (segundos) y retorna una
    tupla con las conversión a horas, minutos y segundos.
    """
    if numero < 0:
        try:
            raise ValueError("\nError al ingresar un valor negativo.")
        except ValueError as exc:
            print(exc)

    horas = 0
    minutos = 0
    segundos = 0

    if numero >= 3600:
        horas = numero // 3600
        numero -= horas * 3600
    if numero >= 60:
        minutos = numero // 60
        numero -= minutos * 60
    if numero > 0:
        segundos = numero

    tupla_total = (horas, minutos, segundos)

    return tupla_total


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    print("Ingrese los grados: ", end='')
    grados_entrada = int(input())
    print("Ingrese los minutos: ", end='')
    minutos_entrada = int(input())
    print("Ingrese los segundos: ", end='')
    segundos_entrada = int(input())

    segundos_salida = sexadecimal_a_decimal(grados_entrada,
                                            minutos_entrada,
                                            segundos_entrada)
    print(f"\nSegundos: {segundos_salida}")

    tupla_h_m_s = decimal_a_sexadecimal(segundos_salida)
    print(f"\nHoras: {tupla_h_m_s[0]}\
            \nMinutos: {tupla_h_m_s[1]}\
            \nSegundos: {tupla_h_m_s[2]}")


if __name__ == "__main__":
    principal()
