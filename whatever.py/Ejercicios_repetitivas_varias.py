#Daniel Padilla y Miguel Alzate
#
#1
n1 = int(input("Ingrese su número:"))
contP1 = 0
sumaP1 = 0
for i in range(1, n1+1, 2):
    sumaP1 += i
    if sumaP1<=n1:
        contP1 += 1
        print(f"Se utiliza el número {i}")
sumatoriaP1 = contP1*contP1
print(f"Se utilizaron {contP1} números, y la sumatoria es:{sumatoriaP1}")

#2
dinero = int(input("Ingrese la cantidad de dinero que posee:"))
n2 = int(input("Ingrese el número de artículos que va a comprar:"))
contP2 = 0
listArts = []
listPrec = []

for i in range(1, n2+1):
    obj = input(f"Ingrese el producto {i}:")
    prec = int(input(f"Ingrese su valor:"))
    listArts.append(obj)
    listPrec.append(prec)

for v1, v2 in zip(listArts, listPrec):
    if (dinero - v2) > 0:
        dinero -= v2
        contP2 += 1
        print(f"Se compró el artículo {v1}, con valor de {v2}")
print(f"Se compraron {contP2} artículos, sobró {dinero}")

#3
for i in range(10):
    n3 = int(input(f"Digite el {i+1}º número:"))
    cub = n3*n3*n3
    cuart = cub*n3
    print(f"El cubo del número {n3} es:{cub}, y su cuarta es:{cuart}")

#4
listPositiveNumbers = []
for i in range(10):
    n4 = int(input(f"Digite el {i+1}º número:"))
    if n4 > 0:
        listPositiveNumbers.append(n4)
print(listPositiveNumbers)

#5
n5 = int(input("Ingrese su número:"))
tablaMultiplicar = {}
for i in  range(1, 11):
    mult = n5 * i
    tablaMultiplicar.update({f"{i}x{n5}": mult})
    
print(f"Tabla de multiplicar para {n5}")
print(tablaMultiplicar)

#6
for i in range(1, 16):
    n6 = int(input(f"Ingrese el {i}º número:"))
    if n6 < 0:
        n6 *= -1
        print(n6)
    else:
        print(n6)

#7
sumaP7 = 0
for calf in range(7):
    n7 = float(input(f"Ingrese la nota {calf+1}º:"))
    sumaP7 += n7
promP7 = sumaP7/7
print(f"Su promedio en la asignatura de Diseño de Algoritmos es:{promP7}")

#8
contPosP8 = 0
contNegP8 = 0
contNeuP8 = 0
for i in range(20):
    n8 = int(input(f"Digite el {i+1}º número:"))
    if n8<0:
        contNegP8 += 1
    elif n8>0:
        contPosP8 += 1
    else:
        contNeuP8 += 1
print(f"La cantidad de números positivos es:{contPosP8}, neutros {contNeuP8} y la cantidad de"
    f"negativos {contNegP8}")

#9 
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
    time.sleep(0)
    #Este permitirá que x vaya aumentando a medida que se lee el codigo
    x += 1
print(f"{hours:02}:{minutes:02}:{seconds:02}")