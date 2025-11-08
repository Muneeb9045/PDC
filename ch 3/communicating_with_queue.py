import multiprocessing
import random
import time

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

class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for task in calculator_tasks:
            self.queue.put(task)
            print(f"Producer added task: {task[0]} ({task[2]}, {task[3]})")
            time.sleep(random.randint(1, 2))
            print(f"Queue size: {self.queue.qsize()}")

class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("Queue is empty, consumer exiting.")
                break
            else:
                task = self.queue.get()
                name, func, a, b = task
                result = func(a, b)
                print(f"Consumer executed task: {name} ({a}, {b}) => Result = {result}")
                time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)

    process_producer.start()
    process_consumer.start()

    process_producer.join()
    process_consumer.join()

    print("All calculator tasks completed!")
