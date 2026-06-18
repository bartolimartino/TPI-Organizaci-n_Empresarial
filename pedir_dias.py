import csv 
from datos import guardar_datos

def pedir_dias(lista_empleados, empleado_activo):
    while True:
            print(f"Dias disponibles: {empleado_activo['dias_disponibles']}")
            print(f"Estado: {empleado_activo['estado']}")

            if empleado_activo["estado"] == "rechazada":
                print(f"Lo siento {empleado_activo['nombre']}, No tiene dias disponibles.")
                return

            if empleado_activo["estado"] == "pendiente":
                print("Tiene una licencia pendiente, no puede pedir vacaciones.")
                return

            while True:
                try:
                    cantidad = int(input(f"Cuantos dias desea pedir? (maximo {empleado_activo['dias_disponibles']}): "))

                    if cantidad <= 0:
                        print("Error: debe ingresar un numero mayor a cero.")
                        continue

                    if cantidad > empleado_activo["dias_disponibles"]:
                        print(f"Error: no tiene suficientes dias. Saldo actual: {empleado_activo['dias_disponibles']}.")
                        continue

                    break

                except ValueError:
                    print("Error: debe ingresar un numero entero.")
                    continue

    # Si llega hasta aca, la cantidad es valida
            empleado_activo["dias_disponibles"] -= cantidad
            if empleado_activo["dias_disponibles"] == 0:
                empleado_activo["estado"] = "rechazada"

            guardar_datos(lista_empleados, "datos_empleados.csv")  # acá se usa lista_empleados

            print(f"Solicitud aprobada. Saldo restante: {empleado_activo['dias_disponibles']}.")
            return
    
    