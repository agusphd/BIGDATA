import time
import numpy as np
## Matrix Multiplication
def matrix():
    N = 200
    X = np.random.random((N,N))
    Y = np.random.random((N,N))
    Z = np.zeros((N,N))
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                Z[i][j] += X[i][k] * Y[k][j]

start = time.time()
matrix()
end = time.time()
print("Computation time %f secs" % (end - start))