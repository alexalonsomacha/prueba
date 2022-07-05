import random
# definimos nuestra variable


def adivina_el_numero_compu(x):

    print("=============================")
    print("   ¡Bienvenido(a) al Juego!  ")
    print("=============================")
    print(
        f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        # generamos la prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior

        # obtenemos respuesta del usuario
        respuesta = input(
            f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    print(f"¡Siii! La compu adivino tu número correctamente: {prediccion}")


adivina_el_numero_compu(10)
