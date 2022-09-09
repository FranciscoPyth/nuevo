# funciones en .py

# prueba 1
from audioop import reverse


def sumar(a, b):
    resultado = a + b
    return resultado

suma = sumar(10, 5)
print(suma)


# prueba 2
def saludo(cantidad_saludos):
    """Esta función recoge los nombres ingresados por el usuario en una lista y devuelve la cantidad de saludos que el usario ingresa"""

    lista_nombres = []

    # Bucle de ingreso de nombres
    for i in range(cantidad_saludos):

        nombre = input("Ingrese su nombre: ")
        print("Hola! ", nombre)

        lista_nombres.append(nombre)

    return lista_nombres


nombres = saludo(int(input("Ingrese la cantidad de saludos que desea: ")))

# funcion 3
def orden(lista, sentido):
    """"""

    lista.sort(reverse=sentido)

    return lista

# Tip para comentar o documentar nuestra funcion (prueba 2)
