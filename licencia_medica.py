import time
from datos import guardar_datos

def solicitar_licencia_medica(lista_empleados, empleado_activo, archivo_empresa="datos_empleados.csv"):
    print("Solicitud en proceso...")
    time.sleep(2)  # simula el tiempo de procesamiento del bot

    if empleado_activo["estado"] == "pendiente":
        mensaje_final = "Ya tiene una licencia médica pendiente. Recursos Humanos le dará seguimiento."
        print(mensaje_final)
        return mensaje_final

    empleado_activo["estado"] = "pendiente"
    guardar_datos(lista_empleados, archivo_empresa)

    mensaje_final = (
        "Solicitud derivada a Recursos Humanos exitosamente. "
        "Recursos Humanos estará contactándose con usted."
    )
    print(mensaje_final)
    return mensaje_final
