import numpy as np
from bpf import bpf
from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

traces = np.load('./DATA/LINE_EW_PERIHAKA_100.npy') #(1133, 1126)
lo = 5
hi = 20
sr = 4

import time

###FOR LOOP
start = time.time()

if rank==0:
    chunk1 = bpf(traces[:,0:250], lo, hi, sr)
    np.save('./DATA/chunk1', chunk1)
elif rank==1:
    chunk2 = bpf(traces[:,250:500], lo, hi, sr)
    np.save('./DATA/chunk2', chunk2)
elif rank==2:
    chunk3 = bpf(traces[:,500:750], lo, hi, sr)
    np.save('./DATA/chunk3', chunk3)
elif rank==3:
    chunk4 = bpf(traces[:,750:None], lo, hi, sr)
    np.save('./DATA/chunk4', chunk4)
end = time.time()
print("Computation time %f secs" % (end - start))


