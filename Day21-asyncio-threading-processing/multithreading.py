# Day 21 - Multithreading

import threading
import time


# -----------------------------------
# Thread Function
# -----------------------------------

def task(name):
    print(f"{name} started")                  # Display task start

    time.sleep(2)                             # Simulate waiting

    print(f"{name} completed")                # Display task completion


# -----------------------------------
# Create Threads
# -----------------------------------

thread1 = threading.Thread(
    target=task,
    args=("Thread 1",)
)

thread2 = threading.Thread(
    target=task,
    args=("Thread 2",)
)


# -----------------------------------
# Start Threads
# -----------------------------------

thread1.start()                              # Start first thread
thread2.start()                              # Start second thread


# Wait for Threads
thread1.join()                               # Wait for first thread
thread2.join()                               # Wait for second thread

print("All threads completed")                # Display final message
