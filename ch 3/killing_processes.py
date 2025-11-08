import multiprocessing
import time

# Calculator functions
def add(x, y):
    for i in range(3):
        print(f"Adding {x} + {y}, step {i+1}")
        time.sleep(1)
    print(f"Result: {x + y}")

def subtract(x, y):
    for i in range(3):
        print(f"Subtracting {x} - {y}, step {i+1}")
        time.sleep(1)
    print(f"Result: {x - y}")

def multiply(x, y):
    for i in range(3):
        print(f"Multiplying {x} * {y}, step {i+1}")
        time.sleep(1)
    print(f"Result: {x * y}")

def divide(x, y):
    for i in range(3):
        print(f"Dividing {x} / {y}, step {i+1}")
        time.sleep(1)
    if y == 0:
        print("Error! Division by zero.")
    else:
        print(f"Result: {x / y}")

if __name__ == '__main__':
    # Create processes for each calculator operation
    p1 = multiprocessing.Process(target=add, args=(10, 5))
    p2 = multiprocessing.Process(target=subtract, args=(20, 7))
    p3 = multiprocessing.Process(target=multiply, args=(3, 6))
    p4 = multiprocessing.Process(target=divide, args=(8, 2))

    processes = [p1, p2, p3, p4]

    # Start all processes
    for p in processes:
        print('Process before execution:', p, p.is_alive())
        p.start()
        print('Process running:', p, p.is_alive())

    # Example: terminate one process early (simulate failure or control)
    print("\nTerminating multiply process early...\n")
    p3.terminate()  # terminate multiply process
    p3.join()

    # Join all other processes
    for p in processes:
        if p.is_alive():
            p.join()
        print('Process joined:', p, p.is_alive(), 'Exit code:', p.exitcode)

    print("\nAll calculator processes completed!")
