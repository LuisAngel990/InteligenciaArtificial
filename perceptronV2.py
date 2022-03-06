import msvcrt
import os
import random
class Perceptron:
    def __init__(self):
        while True:
            os.system("cls")
            print("Perceptron\n")
            entradas = []
            rand_init = random.SystemRandom ()
            print("Entradas:")
            umbral = rand_init.randint(1, 5)
            print("u: %s" % umbral)
            for i in range(3):
                w = rand_init.uniform (0.0, 1.70)
                entradas.append(w)
                print("w%s: %s" % (i + 1, w))
            val_x1 = 0
            val_x2 = 0
            val_x3 = 0
            print("[x1] [x2] [x3] [y(x)]")
            for i in range(2):
                if i > 0:
                    val_x1 = 1
                for j in range(2):
                    if j > 0:
                        val_x2 = 1
                    for k in range (2):
                        if k > 0:
                            val_x3 = 1
                        y = 0
                        acum = (val_x1 * entradas[0])
                        acum += (val_x2 * entradas[1])
                        acum += (val_x3 * entradas[2])
                        if acum >= umbral:
                            y = 1
                        print("[%s] [%s] [%s] [%s]" % (val_x1, val_x2, val_x3, y))
                    val_x3 = 0
                val_x2 = 0

            msvcrt.getch()

Perceptron()