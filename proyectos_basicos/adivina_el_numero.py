
# importamos el modulo random
import random

# definimos nuestra variable


def adivina_el_numero(x):
    print("================================")
    print("    ¡Bienvenido(a) al Juego!    ")
    print("================================")
    print("Tu meta es adivinar el número generado por la computadora.")

    # generamos un numero aleatorio entre 1 y x
    numero_aleatorio = random.randint(1, x)

    prediccion = 0

    while prediccion != numero_aleatorio:
        # hacemos un input de numeros enteros con f-string
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este número es muy grande.")

    print(
        f"¡Felicitaciones! Adivinaste el número {numero_aleatorio} correctamente.")


adivina_el_numero(10)
