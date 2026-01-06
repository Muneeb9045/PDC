import multiprocessing
import time

NUM_PROCESSES = 4
NUM_UPDATES = 10000
PRINT_INTERVAL = 1000

shared_total = multiprocessing.Value('i', 0)

def process_update(process_id, shared_total):
    for i in range(1, NUM_UPDATES + 1):
        shared_total.value += 1
        time.sleep(0.00001)

        if i % PRINT_INTERVAL == 0:
            print(f"Process {process_id}  shared_total = {shared_total.value}")

# Start processes
processes = []
for pid in range(1, NUM_PROCESSES + 1):
    p = multiprocessing.Process(target=process_update, args=(pid, shared_total))
    processes.append(p)
    p.start()

for p in processes:
    p.join()