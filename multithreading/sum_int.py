
import random
import threading

result = []  # Global variable
def compute():
    result.append(sum(
        [random.randint(1, 10) for _ in range(10000000)]
    ))

workers = [threading.Thread(target=compute) for _ in range(8)]

# Start all workers
for worker in workers:
    worker.start()

# Gather result
for worker in workers:
    worker.join()

# Print result
print(result)