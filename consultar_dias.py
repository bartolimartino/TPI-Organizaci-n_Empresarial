import csv

def consultar_dias_vacacioens(empleado_activo, archivo_csv="datos_empleados.csv"):
    try:
        with open(archivo_csv, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["id_personal"].strip() == empleado_activo["id_personal"]:
                    dias = fila["dias_disponibles"].strip()
                    nombre = fila["nombre"].strip()
                    mensaje = f"Hola {nombre}, tenés {dias} días de vacaciones disponibles."
                    print(mensaje)
                    return mensaje

            mensaje = "No se encontró su registro en el archivo de empleados."
            print(mensaje)
            return mensaje
    except FileNotFoundError:
        mensaje = f"Error: no se encontró el archivo '{archivo_csv}'."
        print(mensaje)
        return mensaje
    except KeyError:
        mensaje = "Error: el archivo CSV no tiene las columnas esperadas."
        print(mensaje)
        return mensaje
    except Exception as e:
        mensaje = f"Error al consultar los días disponibles: {e}"
        print(mensaje)
        return mensaje
