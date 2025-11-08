import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared items list will hold calculator tasks
tasks = []
condition = threading.Condition()

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
    ("Division", divide, 8, 2)
]


class Producer(threading.Thread):
    def run(self):
        for task in calculator_tasks:
            time.sleep(0.5)  # simulate task creation delay
            with condition:
                tasks.append(task)
                logging.info(f'Produced task: {task[0]} ({task[2]}, {task[3]})')
                condition.notify()  # notify consumer


class Consumer(threading.Thread):
    def run(self):
        for _ in range(len(calculator_tasks)):
            time.sleep(1)  # simulate consumption delay
            with condition:
                while len(tasks) == 0:
                    logging.info('No tasks to consume. Waiting...')
                    condition.wait()

                task = tasks.pop(0)
                name, func, a, b = task
                result = func(a, b)
                logging.info(f'Consumed task: {name} ({a}, {b}) => Result = {result}')
                condition.notify()


def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    logging.info('All calculator tasks processed!')


if __name__ == "__main__":
    main()
