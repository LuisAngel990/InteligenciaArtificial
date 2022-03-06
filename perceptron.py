import msvcrt
import os
class Perceptron:
    def __init__(self):
        os.system("cls")
        print("Perceptron\n")
        entradas = []
        print("Entrada:")
        x = input("x1: ")
        w = input("w1: ")
        entradas.append([x , w])
        cont = 2

        while True:
            print("¿Desea agregar otra entrada?")
            print("1) Si")
            print("2) No")
            op = int(input("Opcion: "))
            if op == 2:
                break
            print("Entrada:")
            x = input("x%s: " % cont)
            w = input("w%s: " % cont)
            entradas.append([x , w])

            cont += 1

        umbral = int(input("Umbral minimo: "))

        cont = 0

        for entrada in entradas:
            print(entrada[0])
            print("1) Si")
            print("2) No")
            op = int(input("Opcion: "))
            if op == 1:
                cont += int(entrada[1])

        if cont >= umbral:
            print("Salida: 1")
        else:
            print("Salida: 0")

        msvcrt.getch()

Perceptron()