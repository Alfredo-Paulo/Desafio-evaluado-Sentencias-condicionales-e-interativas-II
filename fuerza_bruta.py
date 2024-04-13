# Determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en
# minúscula. El programa fuerza_bruta debe intentar todas las combinaciones de letras
# posibles, en orden alfabético, hasta que la combinación de letras sea igual a la de la
# contraseña indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha.

from string import ascii_lowercase
from pyfiglet import Figlet
import pyfiglet

def show_title():
    f = Figlet(font='slant')
    print(f.renderText('Fuerza Bruta !'))

def fuerza_bruta(password):
    intentos = 0
    for letra in password:
        encontrado = False
        for guess in ascii_lowercase:
            intentos += 1
            if guess == letra:
                encontrado = True
                print(guess,intentos)
                break
        if not encontrado:
            return -1  # Si una letra de la contraseña no se encuentra en ascii_lowercase, se devuelve -1
    return intentos

def main():
    show_title()
    password = input("Ingrese la contraseña: ").lower()  # Convertimos la contraseña a minúsculas
    intentos = fuerza_bruta(password)
    if intentos == -1:
        print("Error: La contraseña contiene caracteres no válidos.")
    else:
        print("La contraseña fue forzada en", intentos, "intentos.")

if __name__ == "__main__":
    main()