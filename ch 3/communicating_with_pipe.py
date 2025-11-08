import multiprocessing

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

def producer(pipe):
    """Send calculator tasks to consumer"""
    output_pipe, _ = pipe
    for task in calculator_tasks:
        output_pipe.send(task)
    output_pipe.close()

def consumer(pipe_1, pipe_2):
    """Receive tasks, execute, send results"""
    _, input_pipe = pipe_1
    output_pipe, _ = pipe_2
    input_pipe.close()
    try:
        while True:
            task = input_pipe.recv()
            name, func, a, b = task
            result = func(a, b)
            output_pipe.send(f"{name}: {a}, {b} => Result = {result}")
    except EOFError:
        output_pipe.close()

if __name__ == '__main__':
    # Pipe 1: producer to consumer
    pipe_1 = multiprocessing.Pipe(True)
    producer_process = multiprocessing.Process(target=producer, args=(pipe_1,))
    producer_process.start()

    # Pipe 2: consumer to main process
    pipe_2 = multiprocessing.Pipe(True)
    consumer_process = multiprocessing.Process(target=consumer, args=(pipe_1, pipe_2))
    consumer_process.start()

    # Close unused ends in main
    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            # Receive results from consumer
            print(pipe_2[1].recv())
    except EOFError:
        print("All calculator tasks completed!")
