import msvcrt
import numpy
import os
class Caballos:
    tablero = numpy.zeros((8,8))
    countMejor = 1
    mejor  = numpy.zeros((8,8))
    #Copiar arreglos
    def copiar(self, arr1, arr2):
        y = 0
        while y < 8:
            x = 0
            while x < 8:
                arr2[x][y] = arr1[x][y]
                x += 1
            y += 1
    #Funcion para llenar el tablero
    def llenar(self, n, ejeX, ejeY, tablero):
        newX = ejeX + 2
        newY = ejeY + 1
        tablero2 = numpy.zeros((8,8))
        self.copiar(tablero, tablero2)
        if newX >= 1 and newX <= 8 and newY >= 1 and newY <= 8:
            if tablero2[newX - 1][newY - 1] == 0:
                tablero2[newX - 1][newY - 1] = n + 1
                if (n + 1) > self.countMejor:
                    self.countMejor = (n + 1)
                    #Imprimir el tablero final
                    x = 0
                    os.system("cls")
                    print("Caballos\n")
                    print("Mejor tablero actual (%s caballos)..." % self.countMejor)
                    header = ""
                    while x < 8:
                        header += ("  %s" % (x + 1))
                        x += 1
                    print(header) 
                    y = 0
                    while y < 8:
                        x = 0
                        row = ("%s " % (y + 1))
                        while x < 8:
                            if tablero2[x][y] == 0:
                                row += ("[ ]")
                            else:
                                row += ("[%s]" % int(tablero2[x][y]))
                            x += 1
                        print("%s" % row)
                        y += 1
                self.llenar((n + 1), newX, newY, tablero2)
        newX = ejeX - 2
        newY = ejeY - 1
        tablero2 = numpy.zeros((8,8))
        self.copiar(tablero, tablero2)
        if newX >= 1 and newX <= 8 and newY >= 1 and newY <= 8:
            if tablero2[newX - 1][newY - 1] == 0:
                tablero2[newX - 1][newY - 1] = n + 1
                if (n + 1) > self.countMejor:
                    self.countMejor = (n + 1)
                    #Imprimir el tablero final
                    x = 0
                    os.system("cls")
                    print("Caballos\n")
                    print("Mejor tablero actual (%s caballos)..." % self.countMejor)
                    header = ""
                    while x < 8:
                        header += ("  %s" % (x + 1))
                        x += 1
                    print(header) 
                    y = 0
                    while y < 8:
                        x = 0
                        row = ("%s " % (y + 1))
                        while x < 8:
                            if tablero2[x][y] == 0:
                                row += ("[ ]")
                            else:
                                row += ("[%s]" % int(tablero2[x][y]))
                            x += 1
                        print("%s" % row)
                        y += 1
                self.llenar((n + 1), newX, newY, tablero2)
        newX = ejeX + 1
        newY = ejeY + 2
        tablero2 = numpy.zeros((8,8))
        self.copiar(tablero, tablero2)
        if newX >= 1 and newX <= 8 and newY >= 1 and newY <= 8:
            if tablero2[newX - 1][newY - 1] == 0:
                tablero2[newX - 1][newY - 1] = n + 1
                if (n + 1) > self.countMejor:
                    self.countMejor = (n + 1)
                    #Imprimir el tablero final
                    x = 0
                    os.system("cls")
                    print("Caballos\n")
                    print("Mejor tablero actual (%s caballos)..." % self.countMejor)
                    header = ""
                    while x < 8:
                        header += ("  %s" % (x + 1))
                        x += 1
                    print(header) 
                    y = 0
                    while y < 8:
                        x = 0
                        row = ("%s " % (y + 1))
                        while x < 8:
                            if tablero2[x][y] == 0:
                                row += ("[ ]")
                            else:
                                row += ("[%s]" % int(tablero2[x][y]))
                            x += 1
                        print("%s" % row)
                        y += 1
                self.llenar((n + 1), newX, newY, tablero2)
        newX = ejeX - 1
        newY = ejeY - 2
        tablero2 = numpy.zeros((8,8))
        self.copiar(tablero, tablero2)
        if newX >= 1 and newX <= 8 and newY >= 1 and newY <= 8:
            if tablero2[newX - 1][newY - 1] == 0:
                tablero2[newX - 1][newY - 1] = n + 1
                if (n + 1) > self.countMejor:
                    self.countMejor = (n + 1)
                    #Imprimir el tablero final
                    x = 0
                    os.system("cls")
                    print("Caballos\n")
                    print("Mejor tablero actual (%s caballos)..." % self.countMejor)
                    header = ""
                    while x < 8:
                        header += ("  %s" % (x + 1))
                        x += 1
                    print(header) 
                    y = 0
                    while y < 8:
                        x = 0
                        row = ("%s " % (y + 1))
                        while x < 8:
                            if tablero2[x][y] == 0:
                                row += ("[ ]")
                            else:
                                row += ("[%s]" % int(tablero2[x][y]))
                            x += 1
                        print("%s" % row)
                        y += 1
                self.llenar((n + 1), newX, newY, tablero2)
        newX = ejeX + 2
        newY = ejeY - 1
        tablero2 = numpy.zeros((8,8))
        self.copiar(tablero, tablero2)
        if newX >= 1 and newX <= 8 and newY >= 1 and newY <= 8:
            if tablero2[newX - 1][newY - 1] == 0:
                tablero2[newX - 1][newY - 1] = n + 1
                if (n + 1) > self.countMejor:
                    self.countMejor = (n + 1)
                    #Imprimir el tablero final
                    x = 0
                    os.system("cls")
                    print("Caballos\n")
                    print("Mejor tablero actual (%s caballos)..." % self.countMejor)
                    header = ""
                    while x < 8:
                        header += ("  %s" % (x + 1))
                        x += 1
                    print(header) 
                    y = 0
                    while y < 8:
                        x = 0
                        row = ("%s " % (y + 1))
                        while x < 8:
                            if tablero2[x][y] == 0:
                                row += ("[ ]")
                            else:
                                row += ("[%s]" % int(tablero2[x][y]))
                            x += 1
                        print("%s" % row)
                        y += 1
                self.llenar((n + 1), newX, newY, tablero2)
        newX = ejeX - 2
        newY = ejeY + 1
        tablero2 = numpy.zeros((8,8))
        self.copiar(tablero, tablero2)
        if newX >= 1 and newX <= 8 and newY >= 1 and newY <= 8:
            if tablero2[newX - 1][newY - 1] == 0:
                tablero2[newX - 1][newY - 1] = n + 1
                if (n + 1) > self.countMejor:
                    self.countMejor = (n + 1)
                    #Imprimir el tablero final
                    x = 0
                    os.system("cls")
                    print("Caballos\n")
                    print("Mejor tablero actual (%s caballos)..." % self.countMejor)
                    header = ""
                    while x < 8:
                        header += ("  %s" % (x + 1))
                        x += 1
                    print(header) 
                    y = 0
                    while y < 8:
                        x = 0
                        row = ("%s " % (y + 1))
                        while x < 8:
                            if tablero2[x][y] == 0:
                                row += ("[ ]")
                            else:
                                row += ("[%s]" % int(tablero2[x][y]))
                            x += 1
                        print("%s" % row)
                        y += 1
                self.llenar((n + 1), newX, newY, tablero2)
        newX = ejeX - 1
        newY = ejeY + 2
        tablero2 = numpy.zeros((8,8))
        self.copiar(tablero, tablero2)
        if newX >= 1 and newX <= 8 and newY >= 1 and newY <= 8:
            if tablero2[newX - 1][newY - 1] == 0:
                tablero2[newX - 1][newY - 1] = n + 1
                if (n + 1) > self.countMejor:
                    self.countMejor = (n + 1)
                    #Imprimir el tablero final
                    x = 0
                    os.system("cls")
                    print("Caballos\n")
                    print("Mejor tablero actual (%s caballos)..." % self.countMejor)
                    header = ""
                    while x < 8:
                        header += ("  %s" % (x + 1))
                        x += 1
                    print(header) 
                    y = 0
                    while y < 8:
                        x = 0
                        row = ("%s " % (y + 1))
                        while x < 8:
                            if tablero2[x][y] == 0:
                                row += ("[ ]")
                            else:
                                row += ("[%s]" % int(tablero2[x][y]))
                            x += 1
                        print("%s" % row)
                        y += 1
                self.llenar((n + 1), newX, newY, tablero2)
        newX = ejeX + 1
        newY = ejeY - 2
        tablero2 = numpy.zeros((8,8))
        self.copiar(tablero, tablero2)
        if newX >= 1 and newX <= 8 and newY >= 1 and newY <= 8:
            if tablero2[newX - 1][newY - 1] == 0:
                tablero2[newX - 1][newY - 1] = n + 1
                if (n + 1) > self.countMejor:
                    self.countMejor = (n + 1)
                    #Imprimir el tablero final
                    x = 0
                    os.system("cls")
                    print("Caballos\n")
                    print("Mejor tablero actual (%s caballos)..." % self.countMejor)
                    header = ""
                    while x < 8:
                        header += ("  %s" % (x + 1))
                        x += 1
                    print(header) 
                    y = 0
                    while y < 8:
                        x = 0
                        row = ("%s " % (y + 1))
                        while x < 8:
                            if tablero2[x][y] == 0:
                                row += ("[ ]")
                            else:
                                row += ("[%s]" % int(tablero2[x][y]))
                            x += 1
                        print("%s" % row)
                        y += 1
                self.llenar((n + 1), newX, newY, tablero2)

    def __init__(self):
        os.system("cls")
        print("Caballos\n")
        #Generar un array para el tablero
        self.tablero = numpy.zeros((8,8))
        #Array para la mejor opcion
        self.mejor = numpy.zeros((8,8))
        self.countMejor = 1
        
        #Imprimir la cabecera
        x = 0
        header = ""
        while x < 8:
            header += ("  %s" % (x + 1))
            x += 1
        print(header) 
        #Imprimir el tablero
        y = 0
        while y < 8:
            x = 0
            row = ("%s " % (y + 1))
            while x < 8:
                if self.tablero[x][y] == 0:
                    row += ("[ ]")
                if self.tablero[x][y] == 1:
                    row += ("[R]")
                x += 1
            print("%s" % row)
            y += 1
        #Obtener el primer caballo
        ejeY = int(input("Ingrese el eje Y del primer caballo: "))
        ejeX = int(input("Ingrese el eje X del primer caballo: "))
        #Colocar el primer caballo en el tablero
        self.tablero[ejeX - 1][ejeY - 1] = 1
        #Contador de espacios ocupados del tablero
        n = 1
        #Imprimir el tablero final
        x = 0
        header = ""
        while x < 8:
            header += ("  %s" % (x + 1))
            x += 1
        print(header) 
        y = 0
        while y < 8:
            x = 0
            row = ("%s " % (y + 1))
            while x < 8:
                if self.tablero[x][y] == 0 or self.tablero[x][y] == 2:
                    row += ("[ ]")
                else:
                    row += ("[%s]" % int(self.tablero[x][y]))
                x += 1
            print("%s" % row)
            y += 1
        tablero2 = numpy.zeros((8,8))
        self.copiar(self.tablero, tablero2)
        self.llenar(n, ejeX, ejeY, tablero2)
        msvcrt.getch()

Caballos()