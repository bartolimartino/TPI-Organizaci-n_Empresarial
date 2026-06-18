# TPI-Organizaci-n_Empresarial



#Manual de uso del chatbot MAX:

#Paso 1, 1.ª interacción: El usuario debe interactuar con el bot (en este caso, ejecutar el archivo Menu_principal.py).

#Paso 2, DNI: El usuario deberá ingresar su DNI que lo identifica como empleado en la base de datos.

#Paso 3, seleccionar opción: El usuario deberá elegir entre las opciones que aparecen en pantalla según sus necesidades.
#Opciones: pedir días, consultar días de vacaciones, solicitar licencia médica, salida del programa.

#Paso 4, completar: Según la opción elegida, rellenar los campos solicitados por el chatbot.

# Maquina de estados
El bot pasa por una serie de estados donde se llevan a cabo procesos como entradas de datos, toma de decisiones, etc. Lo importante es que en todo momento el sistema "sabe" en qué situación está, y eso determina qué puede hacer a continuación:

#INICIO: el bot espera el DNI del usuario

#MENU: el usuario está autenticado y elige una opción

#PIDIENDO_DIAS: el bot espera que ingrese la cantidad de días

#CONFIRMANDO_LICENCIA: el bot deriva la solicitud a RR.HH

#FIN: el usuario cerró la sesión
