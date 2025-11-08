import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition for thread-safe print
threadLock = threading.Lock()

# Calculator functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

# List of calculator tasks: (name, func, a, b)
calculator_tasks = [
    ("Addition", add, 10, 5),
    ("Subtraction", subtract, 20, 7),
    ("Multiplication", multiply, 3, 6),
    ("Division", divide, 8, 2),
    ("Addition2", add, 15, 25),
    ("Subtraction2", subtract, 100, 30),
    ("Multiplication2", multiply, 7, 8),
    ("Division2", divide, 50, 5),
    ("DivisionByZero", divide, 10, 0)
]

class CalculatorThread(Thread):
    def __init__(self, name, func, a, b, duration):
        Thread.__init__(self)
        self.name = name
        self.func = func
        self.a = a
        self.b = b
        self.duration = duration

    def run(self):
        # simulate calculation delay
        time.sleep(self.duration)
        result = self.func(self.a, self.b)
        # Acquire lock before printing to avoid garbled output
        threadLock.acquire()
        print(f"---> {self.name} running in process ID {os.getpid()}")
        print(f"      Calculation: {self.a} & {self.b} => Result = {result}\n")
        threadLock.release()


def main():
    start_time = time.time()

    threads = []
    # Create threads for each calculator task
    for task in calculator_tasks:
        name, func, a, b = task
        duration = randint(1, 3)  # random delay to simulate processing time
        t = CalculatorThread(name, func, a, b, duration)
        threads.append(t)
        t.start()

    # Join all threads
    for t in threads:
        t.join()

    print("All calculator tasks finished!")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
