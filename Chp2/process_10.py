# process_10.py
import multiprocessing
import time

def task():
    time.sleep(2)

if __name__ == "__main__":
    start = time.time()

    processes = []
    for i in range(10):  # 10 processes
        p = multiprocessing.Process(target=task)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print(f"Total execution time for 10 processes: {end - start:.2f} seconds")
