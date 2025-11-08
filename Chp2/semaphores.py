import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Semaphore allows 2 consumers to run concurrently
semaphore = threading.Semaphore(2)

# Shared item (calculator task)
task_box = []

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

def producer():
    # Produce a random calculator task
    task = random.choice(calculator_tasks)
    task_box.append(task)
    logging.info(f'Producer added task: {task[0]} ({task[2]}, {task[3]})')
    # Release semaphore to allow consumers to consume
    semaphore.release()

def consumer():
    # Acquire semaphore before consuming
    semaphore.acquire()
    if task_box:
        task = task_box.pop(0)
        name, func, a, b = task
        result = func(a, b)
        logging.info(f'Consumer executed task: {name} ({a}, {b}) => Result = {result}')
    else:
        logging.info('Consumer found no task to execute')

def main():
    threads = []

    # Simulate 10 iterations of producers and consumers
    for _ in range(10):
        t_producer = threading.Thread(target=producer)
        t_consumer1 = threading.Thread(target=consumer)
        t_consumer2 = threading.Thread(target=consumer)

        # Start threads
        t_producer.start()
        t_consumer1.start()
        t_consumer2.start()

        # Join threads
        t_producer.join()
        t_consumer1.join()
        t_consumer2.join()

if __name__ == "__main__":
    main()
