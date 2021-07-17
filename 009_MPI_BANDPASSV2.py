import numpy as np
from bpf import bpf
from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = np.load('./DATA/LINE_EW_PERIHAKA_100.npy') #(1133, 1126)
data = data[:, 0:1000]

lo = 5
hi = 20
sr = 4

import time

###FOR LOOP
start = time.time()
chunk = data[:,rank*250:(rank+1)*250]
chunkbpf = bpf(chunk,5,30,sr)
np.save('./DATA/chunk_%s'%(rank+1), chunkbpf)
end = time.time()
print("Computation time %f secs" % (end - start))


