import msvcrt
import numpy
import os
os.system("cls")
print("Reinas\n")
dimensiones = 0
#Obtener dimensiones del tablero
while dimensiones < 1:
    dimensiones = int(input("Digite las dimensiones del tablero:"))
    if dimensiones < 1:
        print("Error: dimensiones no validas.")
#Generar un array para el tablero
tablero = numpy.zeros((dimensiones,dimensiones))

#Imprimir la cabecera
x = 0
header = ""
while x < dimensiones:
    header += ("  %s" % (x + 1))
    x += 1
print(header) 
#Imprimir el tablero
y = 0
while y < dimensiones:
    x = 0
    row = ("%s " % (y + 1))
    while x < dimensiones:
        if tablero[x][y] == 0:
            row += ("[ ]")
        if tablero[x][y] == 1:
            row += ("[R]")
        x += 1
    print("%s" % row)
    y += 1

#Obtener la primera reina
ejeY = int(input("Ingrese el eje Y de la primera reina: "))
ejeX = int(input("Ingrese el eje X de la primera reina: "))
#Colocar la primera reina en el tablero
tablero[ejeX - 1][ejeY - 1] = 1
#Contador de espacios ocupados del tablero
count = 1
#Contador de reinas
countR = 1
#Ciclo para poner las reinas y las pocisiones en que apuntan
while True:
    #Horizontales
    n = 0
    while n < dimensiones:
        if tablero[n][ejeY - 1] == 0:
            tablero[n][ejeY - 1] = 2
            count += 1
        n += 1
    #Verticales
    n = 0
    while n < dimensiones:
        if tablero[ejeX - 1][n] == 0:
            tablero[ejeX - 1][n] = 2
            count += 1
        n += 1
    #Diagonales
    n1 = ejeX
    n2 = ejeY
    while n1 < dimensiones and n2 < dimensiones:
        if tablero[n1][n2] == 0:
            tablero[n1][n2] = 2
            count += 1
        n1 += 1
        n2 += 1
    n1 = ejeX - 2
    n2 = ejeY - 2
    while n1 >= 0 and n2 >= 0:
        if tablero[n1][n2] == 0:
            tablero[n1][n2] = 2
            count += 1
        n1 -= 1
        n2 -= 1
    n1 = ejeX - 2
    n2 = ejeY
    while n1 >= 0 and n2 < dimensiones:
        if tablero[n1][n2] == 0:
            tablero[n1][n2] = 2
            count += 1
        n1 -= 1
        n2 += 1
    n1 = ejeX
    n2 = ejeY - 2
    while n1 < dimensiones and n2 >= 0:
        if tablero[n1][n2] == 0:
            tablero[n1][n2] = 2
            count += 1
        n1 += 1
        n2 -= 1
    
    #Detener el ciclo
    if count >= (dimensiones * dimensiones):
        break
    
    #Seleccionar una nueva reina
    found = False
    y = 0
    while y < dimensiones:
        x = 0
        while x < dimensiones:
            if tablero[x][y] == 0:
                found = True
                ejeX = x + 1
                ejeY = y + 1
                tablero[x][y] = 1
                count += 1
                countR += 1
                break
            x += 1
        if found == True:
            break
        y += 1
#Imprimir el tablero final
x = 0
header = ""
while x < dimensiones:
    header += ("  %s" % (x + 1))
    x += 1
print(header) 
y = 0
while y < dimensiones:
    x = 0
    row = ("%s " % (y + 1))
    while x < dimensiones:
        if tablero[x][y] == 0 or tablero[x][y] == 2:
            row += ("[ ]")
        if tablero[x][y] == 1:
            row += ("[R]")
        x += 1
    print("%s" % row)
    y += 1
#Imprimir el numero de reinas
print("Numero de reinas: %s \n" % countR)
msvcrt.getch()