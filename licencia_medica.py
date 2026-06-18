import csv
import time
def solicitar_licencia_medica():
   
    print("Solicitud en proceso...")
    time.sleep(2)  # simula el tiempo de procesamiento del bot

    mensaje_final = (
        "Solicitud derivada a Recursos Humanos exitosamente. "
        "Recursos Humanos estará contactándose con usted."
    )
    print(mensaje_final)
    return mensaje_final
