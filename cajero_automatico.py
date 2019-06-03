# Proyecto: Simulador de Cajero con Python

# Librerias
import sys

# Dependencias
from Console import Println, Input
from Funciones import *

# Variables 
exitApplication = False
intentosDisponibles = 3
actualAcc = None

# Programa
IniciarCajero()
while (exitApplication == False):
    if (actualAcc == None):
        if (intentosDisponibles > 0):
            intentosDisponibles -= 1
            actualAcc = Ingresar()
            if (actualAcc == None): 
                Println("> No se encontraron coincidencias en la base de datos.")
            else:
                Println("> Bienvenido de nuevo, %s." % (actualAcc.name))
        else:
            Println("> Ud. agotó todos sus intentos de inicio de sesión.")
            Println("> Comuniquese al 0800-000-000 para más información.")
            exitApplication = True
    else:
        MostrarOperacionesDisponibles()
        Input("> Presione enter para salir.")
        # Preguntar sobre operacion a realizar
        # Realizar operacion
        # preguntar si salir
        # quiere salir:
            # saludar
            # esperar x seg.
            # salir
            # borrar pantalla
        # no quiere salir:
            # empezar de nuevo

Println("> Que tenga buenos días.")
sys.exit()