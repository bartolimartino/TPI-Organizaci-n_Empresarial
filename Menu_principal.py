
import csv
from datos import datos_a_lista
from pedir_dias import pedir_dias
from licencia_medica import solicitar_licencia_medica
from consultar_dias import consultar_dias_vacacioens 

def mostrar_menu():   
    while True:
        try:
            print("\n---|ChatBot - Gestión de vacaciones|---")
            print(f"\n¡Hola {empleado_activo['nombre']}! soy Max, el ChatBot asignado a la Gestión de vacaciones. ¿Como puedo ayudarte?")
            print("1°) - Pedir Dias")
            print("2°) - Consultar saldo de dias")
            print("3°) - Presentación licencia médica")
            print("4°) - Salir")  

            eleccion = int(input("Ingrese una opción del menu: "))

            if eleccion < 1 or eleccion > 4:
                print(
                    "\n¡Vaya hubo un error! Lo siento, la opción ingresada no se encuentra dentro del rango existente, pruebe con una dentro del rango: (1/4) "
                )
                continue

            return eleccion

        except ValueError:
            print("\n ¡Vaya hubo un error! Debe ingresar un valor númerico dentro del rango disponibles: (1/4), intente de nuevo")
            continue


# ==================
# Bloque principal
# ==================

archivo_empresa = "datos_empleados.csv" 
lista_empleados = datos_a_lista(archivo_empresa)

empleado_activo = None
while empleado_activo is None:
    print("--|Bienvenido al área de gestion de vacaciones de TechCorp S.A.|-- ")
    print("---------------------------------------------------------------------")
    dni = input("Por favor ingrese su número de identificación personal: ").strip()

    for empleado in lista_empleados:
        if empleado["id_personal"] == dni:
            empleado_activo = empleado
            break
    if empleado_activo is None:
        print("Identificador no encontrado, intente nuevamente.")





while True:
    try:
        opcion = mostrar_menu()
        if opcion == 1:
            pedir_dias(lista_empleados, empleado_activo)
        if opcion == 2:
            consultar_dias_vacacioens(empleado_activo, archivo_empresa)
        if opcion == 3:
            licencia = solicitar_licencia_medica()
        if opcion == 4:
            pass
            print("Saliendo del programa, hasta pronto")
            break

    except Exception as e:
        print("ERROR: Ocurrio un error inesperado:", type(e).__name__, {e})