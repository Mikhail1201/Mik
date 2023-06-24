#Librería time para poder utilizar la función .sleep y de esta manera hacer que espere 1s para sumar 1 al relog
import time
seconds = 0
minutes = 0
hours = 0
x = 0
#Defino una condicion para salir del bucle, en este caso pongo que x sea menor que 24h
while x<86400:
    #con esto, segundos no pasará nunca de 60
    seconds = x % 60
    #Lo mismo que con los segundos
    minutes = int(x / 60) % 60
    #Aquí para que no pase de 24
    hours = int(x / 3600) % 24
    #Este print se reescribe así mismo una vez vuelve a hacer llamado
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end='\r')
    #Si ponemos el sleep en 0 irá rapido, si lo ponemos en 1, aumentará segundo a segundo
    time.sleep(1)
    #Este permitirá que x vaya aumentando a medida que se lee el codigo
    x += 1
print(f"{hours:02}:{minutes:02}:{seconds:02}")


