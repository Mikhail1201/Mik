#Daniel Padilla, Miguel Alzate
#
#1.
suma_p1 = 0
for i in range(1,6):
    suma_p1 += i
print(f"La suma de los primeros 5 números enteros es:{suma_p1}")

#2.
n_p2 = int(input("Ingrese el número de valores a promediar:"))
suma_p2 = 0
for i in range(1, n_p2+1):
    num = int(input(f"Ingrese el número {i}:"))
    suma_p2 += num
    print(f"{i}º valor leído.")
prom_p2 = suma_p2/n_p2
print(f"El promedio de los números leídos es:{prom_p2}")

#3.
n_p3 = int(input("Ingrese el número de valores:"))
cont_p3 = 0
for i in range(1, n_p3+1):
    num = int(input(f"Ingrese el número {i}:"))
    if num>50:
        cont_p3 += 1
    print(f"{i}º valor leído.")
print(f"La cantidad de números mayores que 50 es:{cont_p3}")

#4.
n_p4 = int(input("Ingrese el número:"))
fact_p4 = 1
num_p4 = 1
while num_p4<=n_p4:
    if n_p4 != 0:
        fact_p4 *= num_p4
        num_p4 += 1
    else:
        fact_p4 = 1
        break
print(f"El factorial de {n_p4} es:{fact_p4}")

#5.
n_p5 = int(input("Ingrese la cantidad de números a escribir:"))
cont_p5 = 0
suma_p5 = 0
for i in range(1, n_p5+1):
    num_p5 = int(input(f"Ingrese el valor {i}:"))
    if num_p5<<25:
        cont_p5 += 1
        suma_p5 += num_p5
    print(f"{i}º número leído.")
prom_p5 = suma_p5/n_p5

#6.
for i in range(1, 20, 2):
    print(i)

#7.
#Hay que tener en cuenta que: la suma de los numeros impares es igual al cuadrado de los naturales, por ejemplo
#1+3 = 2^2 , 1+3+5 = 3^2 , 1+3+5+7 = 4^2, etc

n_p7 = int(input("Ingrese su número:"))
cont_p7 = 0
suma_p7 = 0
for i in range(1, n_p7+1, 2):
    suma_p7 += i
    if suma_p7<=n_p7:
        cont_p7 += 1
        print(f"Se utiliza el número {i}")
sumatoria_p7 = cont_p7*cont_p7
print(f"Se utilizaron {cont_p7} números, y la sumatoria es:{sumatoria_p7}")

#8. 
votos_totales = 0
votos_si = 0
votos_no = 0
voto = input("Ingrese su voto(si o no ):").lower()
while voto != "si" and voto != "no" and voto != "fin":
    if voto != "si" and voto != "no" and voto != "fin":
        voto = input("Valor incorrecto. Ingrese su voto(si o no ):").lower()

while voto != "fin":
    if voto == "si":
        votos_si += 1
    elif voto == "no":
        votos_no += 1
    voto = input("Ingrese su voto(si o no ):").lower()
    while voto != "si" and voto != "no" and voto != "fin":
        if voto != "si" and voto != "no" and voto != "fin":
            voto = input("Valor incorrecto. Ingrese su voto(si o no ):").lower()
votos_totales = votos_si + votos_no
print(f"El conteo de votos es:{votos_totales}, en si:{votos_si}, en no:{votos_no}")
if votos_si>votos_no:
    print("Ganador: Si")
elif votos_no>votos_si:
    print("Ganador: No")
else:
    print("Ganador: Empate")

#9.
n_p9 = int(input("Ingrese el número ganador:"))
cont_p9 = 0
num_actual = -1
while num_actual != n_p9:
    num_actual = int(input("Ingrese el valor sacado de la urna:"))
    cont_p9 += 1
print(f"Se sacaron {cont_p9} números antes de sacar el número ganador.")