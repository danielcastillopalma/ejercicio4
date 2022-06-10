import numpy as np

arrayBus = np.ones((10,5))
cont  = 1
for i in range (10):
    for j in range(5):
        if j == 2:
            arrayBus[i][j] = 0
        else:
            
            arrayBus[i][j] = cont
            cont = cont +1
print(arrayBus)
