# Day 19 - Generators & Function Caching 🐍

## Introduction

On the nineteenth day of my Python learning journey, I learned about **generators and function caching**.

The topics covered today are **generators, the `yield` keyword, generator functions, `next()`, function caching, and `lru_cache()`**.

---

# 1. Python Generators

A **generator** is a special type of function that generates values one at a time instead of returning all the values at once.

Generators use the `yield` keyword to produce values.

### Example

```python
def numbers():
    yield 10
    yield 20
    yield 30


result = numbers()
print(result)
```

The function produces each value one at a time.

---

# 2. yield Keyword

The **`yield`** keyword is used to produce a value from a generator.

Unlike `return`, `yield` pauses the function and remembers its current state.

```python
def count():
    yield 1
    yield 2
    yield 3
```

When the generator continues, it starts from where it previously stopped.

---

# 3. Generator Function

A **generator function** is a function that contains one or more `yield` statements.

When a generator function is called, it returns a generator object instead of immediately executing the function.

```python
def numbers():
    yield 10
    yield 20
    yield 30


result = numbers()
print(result)
```

The values are generated when the generator is iterated.

---

# 4. next() Function

The `next()` function is used to get the next value from a generator.

```python
def numbers():
    yield 10
    yield 20
    yield 30


result = numbers()

print(next(result))  # Output: 10
print(next(result))  # Output: 20
print(next(result))  # Output: 30
```

Each call to `next()` continues the generator from where it previously stopped.

---

# 5. Function Caching

**Function caching** stores the result of a function so that the same calculation does not need to be performed again.

Python provides caching functionality through the `functools` module.

```python
from functools import lru_cache
```

Caching can be useful when a function performs the same calculation multiple times.

---

# 6. lru_cache()

`lru_cache()` is a function from the `functools` module that can store previously calculated results.

It is commonly used as a decorator.

### Example

```python
from functools import lru_cache


@lru_cache
def square(number):
    return number * number


print(square(5))
print(square(5))
```

When the function is called again with the same argument, the previously calculated result can be reused.

This can improve performance when the same calculations are performed repeatedly.

---

# Key Learnings

* Learned Python generators.
* Learned the `yield` keyword.
* Learned generator functions.
* Learned generator objects.
* Learned the `next()` function.
* Learned function caching.
* Learned the `functools` module.
* Learned `lru_cache()`.
* Understood how caching can avoid repeated calculations.

---

# Note

Generators are useful for producing values one at a time, while function caching helps reuse previously calculated results and can improve program performance.
