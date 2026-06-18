import csv

def datos_a_lista(datos_empleados):
    try:
        with open(datos_empleados, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            lista_empleados = []

            for fila in lector:
                empleado = {
                    "id_personal": fila["id_personal"].strip(),
                    "nombre": fila["nombre"].strip(),
                    "dias_disponibles": int(fila["dias_disponibles"].strip()),
                    "estado": fila["estado"].strip()
                }
                lista_empleados.append(empleado)
                
            return lista_empleados

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{datos_empleados}'.")
        return None
    
def guardar_datos(lista_empleados, archivo_empresa):
    with open(archivo_empresa, "w", newline="", encoding="utf-8") as archivo:
        campos = ["id_personal", "nombre", "dias_disponibles", "estado"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for empleado in lista_empleados:
            escritor.writerow(empleado)
    

