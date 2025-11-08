# process_15.py
import multiprocessing
import time

def task():
    time.sleep(2)

if __name__ == "__main__":
    start = time.time()

    processes = []
    for i in range(15):  # 15 processes
        p = multiprocessing.Process(target=task)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print(f"Total execution time for 15 processes: {end - start:.2f} seconds")
