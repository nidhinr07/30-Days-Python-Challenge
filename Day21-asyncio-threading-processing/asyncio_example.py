# Day 21 - Asyncio

import asyncio


# -----------------------------------
# Basic Async Function
# -----------------------------------

async def task(name, delay):
    print(f"{name} started")                  # Display task start

    await asyncio.sleep(delay)                # Wait asynchronously

    print(f"{name} completed")                # Display task completion


# -----------------------------------
# Run Multiple Async Tasks
# -----------------------------------

async def main():

    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 1),
        task("Task 3", 3)
    )


asyncio.run(main())                           # Start async program
