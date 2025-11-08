import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared list for calculator tasks
tasks = []
event = threading.Event()

# Calculator functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

# List of calculator tasks: (operation_name, func, a, b)
calculator_tasks = [
    ("Addition", add, 10, 5),
    ("Subtraction", subtract, 20, 7),
    ("Multiplication", multiply, 3, 6),
    ("Division", divide, 8, 2),
]

class Producer(threading.Thread):
    def run(self):
        for task in calculator_tasks:
            time.sleep(random.randint(1, 3))  # simulate delay in producing task
            tasks.append(task)
            logging.info(f'Producer added task: {task[0]} ({task[2]}, {task[3]})')
            event.set()      # notify consumer
            event.clear()    # reset event

class Consumer(threading.Thread):
    def run(self):
        for _ in range(len(calculator_tasks)):
            event.wait()  # wait until a task is produced
            task = tasks.pop(0)
            name, func, a, b = task
            result = func(a, b)
            logging.info(f'Consumer executed task: {name} ({a}, {b}) => Result = {result}')

def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    logging.info("All calculator tasks completed!")

if __name__ == "__main__":
    main()
