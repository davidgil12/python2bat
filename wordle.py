import random

# palabras Secretas, ademas de eleccion aleatorias de ellas
def seleccionar_palabra():
    palabras = ['python', 'programacion', 'desarrollo', 'ahorcado', 'juego']
    return random.choice(palabras)

# Muestra el progreso del juego:

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    return progreso

# Definimos la funcion principal del Juego

def jugar():
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = set()
    intentos = 6

# Bucle del Juego

    print("¡Bienvenido al juego del Ahorcado!")
    
    while intentos > 0:
        print(f"\nPalabra: {mostrar_progreso(palabra_secreta, letras_adivinadas)}")
        print(f"Tienes {intentos} intentos restantes.")

        # Solicita la entrada del jugador

        letra = input("Adivina una letra: ").lower()

        # comprobar si la letra ya ha sido adivinada

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        # actualizar el conjunto de letras adivinadas

        letras_adivinadas.add(letra)

        # comprobar si la letra es correcta

        if letra not in palabra_secreta:
            intentos -= 1
            print("Letra incorrecta.")

        #comprobar si el jugador ha ganado

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
            break

        # manejar la perdida del juego

    else:
        print(f"¡Has perdido! La palabra era: {palabra_secreta}")

# ejecutamos el juego

if __name__ == "__main__":
    jugar()