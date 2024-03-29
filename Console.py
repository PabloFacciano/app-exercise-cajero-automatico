
# Librerías
import sys
import time

# Configuración
animaciones = True
animacionPorCaracter = True
milisegundosEntreAnimacion = 25

def _wait():
    time.sleep(milisegundosEntreAnimacion  / 1000)

def Print(text):
    if (animaciones):
        if (animacionPorCaracter):
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                _wait()
        else:
            sys.stdout.write(text)
            sys.stdout.flush()
            _wait()
    else:
        sys.stdout.write(text)
        sys.stdout.flush()
