import numpy as np
import time
import multiprocessing
cpus = multiprocessing.cpu_count()

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
def montecarlomulti(i):
    print(calculate(i))


raynos = np.arange(0,100,1)
ncpu = cpus - 2
rit = int(len(raynos) / ncpu)
rmdr = int(len(raynos) % ncpu)

for m in range(rit):
    processes = []
    for i in range(ncpu):
        k = (i + (m * ncpu))
        p = multiprocessing.Process(target=montecarlomulti, args=[k])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

processes = []
for i in range(rmdr):
    k = (i + (ncpu * rit))
    p = multiprocessing.Process(target=montecarlomulti, args=[k])
    p.start()
    processes.append(p)

for process in processes:
    process.join()
end = time.time()

end = time.time()

print("Computation time %f secs" % (end - start))