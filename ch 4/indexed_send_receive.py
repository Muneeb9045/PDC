from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("my rank is:", rank)

if rank == 0:
    data = 10000000
    destination_process = 1
    comm.send(data, dest=destination_process)
    print("sending data %d to process %d" % (data, destination_process))

if rank == 1:
    data = "hello"
    destination_process = 0
    comm.send(data, dest=destination_process)
    print("sending data '%s' to process %d" % (data, destination_process))

if rank == 0:
    data1 = comm.recv(source=1)
    print("data received is = %s" % data1)