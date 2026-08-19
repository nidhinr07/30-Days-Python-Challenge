# Day 21 - Multiprocessing

import multiprocessing
import time


# -----------------------------------
# Process Function
# -----------------------------------

def task(name):
    print(f"{name} started")                  # Display process start

    time.sleep(2)                             # Simulate work

    print(f"{name} completed")                # Display process completion


# -----------------------------------
# Create Processes
# -----------------------------------

if __name__ == "__main__":

    process1 = multiprocessing.Process(
        target=task,
        args=("Process 1",)
    )

    process2 = multiprocessing.Process(
        target=task,
        args=("Process 2",)
    )


    # -----------------------------------
    # Start Processes
    # -----------------------------------

    process1.start()                          # Start first process
    process2.start()                          # Start second process


    # -----------------------------------
    # Wait for Processes
    # -----------------------------------

    process1.join()                           # Wait for first process
    process2.join()                           # Wait for second process

    print("All processes completed")           # Display final message
