import threading
import time
import random

# Thread-safe box to store calculator tasks
class TaskBox:
    def __init__(self):
        self.lock = threading.RLock()
        self.tasks = []

    def add_task(self, task):
        with self.lock:
            self.tasks.append(task)

    def remove_task(self):
        with self.lock:
            if self.tasks:
                return self.tasks.pop(0)
            return None

# Calculator functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

# Thread to add calculator tasks (producer)
def adder(box, task_count):
    operations = [
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
    print(f"{task_count} tasks to ADD\n")
    while task_count:
        task = random.choice(operations)
        box.add_task(task)
        time.sleep(1)
        task_count -= 1
        print(f"ADDED task {task[0]} --> {task_count} tasks remaining\n")

# Thread to remove and execute calculator tasks (consumer)
def remover(box, task_count):
    print(f"{task_count} tasks to EXECUTE\n")
    while task_count:
        task = box.remove_task()
        if task:
            name, func, a, b = task
            result = func(a, b)
            print(f"EXECUTED task: {name} ({a}, {b}) => Result = {result}\n")
            task_count -= 1
        else:
            print("No tasks available, waiting...")
        time.sleep(1)

def main():
    box = TaskBox()

    t1 = threading.Thread(target=adder, args=(box, random.randint(5, 10)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(5, 10)))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All calculator tasks processed!")

if __name__ == "__main__":
    main()
