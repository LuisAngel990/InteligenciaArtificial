import msvcrt
import os

class Perceptron:
    
    table = []
    countGen = 1
    
    def generarArray(self, entradas):
        row = []
        count = int("0")
        for x in range(entradas):
            count += (2**x)

        
        for x in range (count + 1):
            bin = ""
            n = x
            row = []
            while n != 0:
                bit = n % 2
                cociente = n // 2
                bin = (("%s" % bit) + bin)
                n = cociente
            while len(bin) < entradas:
                bin = "0" + bin
            for x in bin:
                row.append(x)
            self.table.append(row)


    def __init__(self):
        os.system("cls")
        print("Perceptron Simple\n")
        entradas = int(input("Número de entradas: "))
        valB = int(input("Valor del bias: "))
        header = "[b]"
        for x in range (entradas):
            header += ("[x%s]" % (x + 1))
        header += "[s(y)]"
        print(header)
        self.generarArray(entradas)
        for row in self.table:
            temp = ("[%s]" % valB)
            res = 1
            for data in row:
                if data == "0":
                    temp += "[-1]"
                    res = -1
                else:
                    temp += "[1]"
            temp += ("[%s]" % res)
            print(temp)

        #Solicitar datos
        print("Generación 1")
        wb = float(input("Peso del bias: "))
        w = []
        for x in range(entradas):
            w.append(1.0)
        for x in range(entradas):
            n = float(input("Peso del x%s: " % (x + 1)))
            w[x] = n
        
        countRow = 0
        count = int("0")
        for x in range(entradas):
            count += (2**x)
        count += 1
        while countRow < count:
            #Paso 1 obtener y
            y = valB * wb 
            val = 1
            for x in range(entradas):
                wx = 1
                if self.table[countRow][x] == "0":
                    wx = -1
                    val = -1
                y += wx * w[x]
            #Paso 2 obtener factor de activación
            if y < 0:
                y = -1
            else:
                y = 1
            #Paso 3 obtener el error
            e = val - (y)
            #Paso 4 obtener nuevos pesos en caso de haber error
            
            if e != 0:
                self.countGen += 1 
                wb += (0.4 * e * valB)
                print("---------------------------------")
                print("Generación %s:" % self.countGen)
                print("Peso del bias: %s" % wb)
                #wTemp = []
                for x in range(entradas):
                    wx = 1
                    if self.table[countRow][x] == "0":
                        wx = -1
                    w[x] += (0.4 * e * wx)
                    #wTemp.append(w[x] + (0.4 * e * wx))
                    print("Peso de x%s: %s" % ((x + 1), w[x]))
                countRow = 0
                
                #w = wTemp
            else:
                countRow += 1
            
        msvcrt.getch()

Perceptron()