from ctypes import sizeof
import numpy as np
from random import *
#Crear un arreglo de dos dimensiones de tamaño 4 y 4 con elementos caracteres. Se pide, contar las vocales.

arrayCar = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
arrayA = np.zeros((4,4), dtype = str)
largo = len(arrayCar)
print(arrayCar[randint(0,largo)])
cont = 0
for i  in range (4):
    for j in range (4):
         
        arrayA[i][j]  = arrayCar[randint(0,largo)]
        if arrayA[i][j] == "a" or arrayA[i][j] == "e" or arrayA[i][j] == "i" or arrayA[i][j] == "o" or arrayA[i][j] == "u":
            cont  = cont +1
                                
print (arrayA)

print(f"El arreglo contiene {cont} Vocales ")