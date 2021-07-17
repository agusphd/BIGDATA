import numpy as np
import time

grv = np.random.random()
grv = np.random.random(size=(1000,1000,100))
def calculate(i):
    phi = np.random.random() * 0.05 + 0.15*i
    Sw  = 1 - np.random.random() * 0.7
    Fvf = 1.6
    vol = np.sum(grv)
    OOIP = vol * phi * (1-Sw) * Fvf * 7758
    return OOIP

start = time.time()
for i in range(100):
    print(calculate(i))

end = time.time()

print("Computation time %f secs" % (end - start))
