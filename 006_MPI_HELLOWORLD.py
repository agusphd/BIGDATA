from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank==0:
    print ('Process Data 1')
elif rank==1:
    print ('Process Data 2')
elif rank==2:
    print ('Process Data 3')
elif rank==3:
    print ('Process Data 4')
