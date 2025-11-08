# thread_15.py
import threading
import time

def task():
    time.sleep(2)

if __name__ == "__main__":
    start = time.time()

    threads = []
    for i in range(15):  # 15 threads
        t = threading.Thread(target=task)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"Total execution time for 15 threads: {end - start:.2f} seconds")
