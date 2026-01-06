from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = 10000000
    destination_process = 1
    comm.send(data, dest=destination_process)
    print("Sending data %d to process %d" % (data, destination_process))
    
    data_received = comm.recv(source=1)
    print("data received is = %s" % data_received)

elif rank == 1:
    data = "hello"
    destination_process = 0
    comm.send(data, dest=destination_process)
    print("Sending data '%s' to process %d" % (data, destination_process))
    
    data_received = comm.recv(source=0)
    print("data received is = %d" % data_received)