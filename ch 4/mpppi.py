from mpi4py import MPI 
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
for i in range(5):
    print(f"Hello from process {rank} of {size}")
 



mpiexec -n 4 python mpppi.py