# Day 21 - Asyncio, Multithreading & Multiprocessing 🐍

## Introduction
On the twenty-first day of my Python learning journey, I learned about **asyncio, multithreading, and multiprocessing**. The topics covered today are **asynchronous programming using `asyncio`, multithreading using the `threading` module, and multiprocessing using the `multiprocessing` module**.

---

# 1. Asyncio
`asyncio` is a Python module used for writing asynchronous programs. It allows a program to handle multiple tasks without waiting for each task to completely finish before starting another one. It is commonly useful for tasks that involve waiting, such as network operations and other I/O operations.

### Important Keywords
- `async`
- `await`
- `asyncio.run()`
- `asyncio.sleep()`

### Basic Example
```python
import asyncio

async def task():
    print("Task started")
    await asyncio.sleep(2)
    print("Task completed")

asyncio.run(task())
```
Here, `async` defines an asynchronous function and `await` pauses the function while allowing other asynchronous tasks to run.

---

# 2. Multithreading
**Multithreading** allows multiple threads to execute tasks within the same program. Python provides the `threading` module for working with threads. It can be imported using:

```python
import threading
```

### Basic Example
```python
import threading

def task():
    print("Task is running")

thread = threading.Thread(target=task)
thread.start()
thread.join()
```
`start()` begins the thread, while `join()` waits for the thread to finish. Multithreading is commonly useful for **I/O-bound tasks**.

---

# 3. Multiprocessing
**Multiprocessing** allows multiple processes to run independently. Python provides the `multiprocessing` module for creating and managing processes. It can be imported using:

```python
import multiprocessing
```

### Basic Example
```python
import multiprocessing

def task():
    print("Process is running")

process = multiprocessing.Process(target=task)
process.start()
process.join()
```
`start()` starts the process, while `join()` waits for the process to finish. Multiprocessing can be useful for **CPU-bound tasks**.

---

# 4. Multithreading vs Multiprocessing

| Multithreading | Multiprocessing |
| :--- | :--- |
| Uses threads | Uses processes |
| Threads share the same memory | Processes have separate memory |
| Useful for I/O-bound tasks | Useful for CPU-bound tasks |
| Uses `threading` | Uses `multiprocessing` |

---

# 5. Asyncio vs Multithreading
Both `asyncio` and multithreading can be useful when a program spends time waiting for tasks to complete. With `asyncio`, tasks are managed using an asynchronous event loop. With multithreading, multiple threads can run tasks concurrently.

---

# Key Learnings
* Learned asynchronous programming.
* Learned the `asyncio` module.
* Learned `async` and `await`.
* Learned `asyncio.run()`.
* Learned `asyncio.sleep()`.
* Learned multithreading.
* Learned the `threading` module.
* Learned `Thread()`.
* Learned `start()` and `join()`.
* Learned multiprocessing.
* Learned the `multiprocessing` module.
* Learned `Process()`.
* Learned the difference between threads and processes.

---

# Note
These concepts introduced different ways of handling multiple tasks in Python. `asyncio` is useful for asynchronous I/O operations, multithreading is commonly useful for I/O-bound tasks, and multiprocessing is useful for CPU-bound tasks.
