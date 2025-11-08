from threading import Barrier, Thread
from time import ctime, sleep
from random import randrange

# Define calculator operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

# Each thread will perform one operation
operations = [
    ("Addition", add, 10, 5),
    ("Subtraction", subtract, 20, 7),
    ("Multiplication", multiply, 3, 6),
    ("Division", divide, 8, 2)
]

num_threads = len(operations)
barrier = Barrier(num_threads)

def calculator_thread(name, func, a, b):
    sleep(randrange(1, 4))  # simulate different calculation times
    result = func(a, b)
    print(f"{name} thread: {a} and {b} => Result = {result} (Time: {ctime()})")
    barrier.wait()  # wait for all threads to reach the barrier

def main():
    print("=== PARALLEL CALCULATOR START ===\n")
    threads = []

    # Create and start threads
    for name, func, a, b in operations:
        t = Thread(target=calculator_thread, args=(name, func, a, b))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("\n=== All Calculations Finished! ===")

if __name__ == "__main__":
    main()
