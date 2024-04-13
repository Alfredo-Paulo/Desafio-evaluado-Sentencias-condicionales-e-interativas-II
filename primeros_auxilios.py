# Se requiere la construcción de una aplicación interactiva primeros_auxilios.py que
# entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega
# en tiempo real.

import sys
import time
from pyfiglet import Figlet
import pyfiglet
from PyInquirer import prompt
import PyInquirer

# Función para mostrar el título de la aplicación
def show_title():
    f = Figlet(font='slant')
    print(f.renderText('Primeros Auxilios'))

# Función para mostrar un mensaje de espera
def show_waiting_message():
    print("\nPor favor, espera un momento mientras procesamos tu solicitud...\n")
    time.sleep(2)

# Función para mostrar los pasos a seguir en caso de emergencia
def show_emergency_steps(emergency_type):
    print("\nPasos a seguir en caso de", emergency_type)
    if emergency_type == 'ahogamiento':
        print("1. Llama al 911.")
        print("2. Intenta sacar a la persona del agua.")
        print("3. Realiza RCP si la persona no está respirando.")
    elif emergency_type == 'quemadura':
        print("1. Enfriar la quemadura con agua corriente durante al menos 10 minutos.")
        print("2. Cubrir la quemadura con un apósito estéril.")
        print("3. Buscar atención médica si la quemadura es grave.")
    elif emergency_type == 'paro cardíaco':
        print("1. Llama al 911.")
        print("2. Comienza la RCP (Resucitación Cardiopulmonar) inmediatamente.")
        print("3. Usa un desfibrilador externo automático (DEA) si está disponible.")

# Función principal para ejecutar la aplicación
def main():
    show_title()
    
    # Definir las preguntas para el usuario
    questions = [
        {
            'type': 'list',
            'name': 'emergency_type',
            'message': 'Selecciona el tipo de emergencia:',
            'choices': ['ahogamiento', 'quemadura', 'paro cardíaco']
        }
    ]
    
    # Pedir al usuario que seleccione el tipo de emergencia
    answers = prompt(questions)
    emergency_type = answers['emergency_type']
    
    show_waiting_message()
    
    # Mostrar los pasos a seguir para la emergencia seleccionada
    show_emergency_steps(emergency_type)

if __name__ == "__main__":
    main()