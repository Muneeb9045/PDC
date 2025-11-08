import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time, sleep
from datetime import datetime

# Calculator functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

# Shared lock for safe printing
serializer = Lock()

# Barrier for synchronized tasks
synchronizer = Barrier(2)

def task_with_barrier(func, a, b):
    """Tasks that wait for other process to reach the barrier"""
    name = multiprocessing.current_process().name
    synchronizer.wait()  # wait for paired process
    result = func(a, b)
    with serializer:
        print(f"Process {name} executed task: {func.__name__}({a}, {b}) => Result = {result}")

def task_without_barrier(func, a, b):
    """Tasks that run independently"""
    name = multiprocessing.current_process().name
    sleep(1)  # simulate delay
    result = func(a, b)
    with serializer:
        print(f"Process {name} executed task: {func.__name__}({a}, {b}) => Result = {result}")

if __name__ == '__main__':
    # Processes that will synchronize
    p1 = Process(name='p1 - add', target=task_with_barrier, args=(add, 10, 5))
    p2 = Process(name='p2 - subtract', target=task_with_barrier, args=(subtract, 20, 7))

    # Processes that will run independently
    p3 = Process(name='p3 - multiply', target=task_without_barrier, args=(multiply, 3, 6))
    p4 = Process(name='p4 - divide', target=task_without_barrier, args=(divide, 8, 2))

    # Start all processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # Join all processes
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("\nAll calculator tasks completed!")
