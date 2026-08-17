# Day 18 - Command Line Utility, Walrus Operator, Shutil, Requests & BeautifulSoup 🐍

## Introduction

On the eighteenth day of my Python learning journey, I learned about **command line utility, walrus operator, shutil module, requests module, GET requests, POST requests, and BeautifulSoup**.

The topics covered today are **command line utility, walrus operator, shutil, requests, GET request, POST request, and basic web scraping using BeautifulSoup**.

---

# 1. Command Line Utility

A **command line utility** allows us to pass information to a Python program through the command line.

Python provides the `sys` module to work with command line arguments.

```python
import sys

print(sys.argv)
```

`sys.argv` stores the arguments passed through the command line.

---

# 2. Walrus Operator

The **walrus operator `:=`** allows us to assign a value to a variable while using it inside an expression.

### Example

```python
if (number := 10) > 5:
    print(number)
```

Here, the value is assigned to `number` and checked in the same expression.

---

# 3. shutil Module

The **`shutil` module** provides functions for working with files and directories.

It can be imported using:

```python
import shutil
```

Some commonly used functions are:

- `shutil.copy()`
- `shutil.copytree()`
- `shutil.move()`
- `shutil.rmtree()`

These functions are used to copy, move, and remove files or directories.

---

# 4. requests Module

The **`requests` module** is used to send HTTP requests to websites and APIs.

It can be installed using:

```text
pip install requests
```

It can then be imported using:

```python
import requests
```

---

# 5. GET Request

A **GET request** is used to request or retrieve data from a server.

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
print(response.text)
```

`requests.get()` sends a GET request to the given URL.

---

# 6. POST Request

A **POST request** is commonly used to send data to a server.

```python
import requests

data = {
    "name": "Alex"
}

response = requests.post("https://example.com", data=data)

print(response.status_code)
```

`requests.post()` sends data to the given URL.

---

# 7. BeautifulSoup

**BeautifulSoup** is a Python library used to extract information from HTML documents.

It is commonly used for basic web scraping.

It can be installed using:

```text
pip install beautifulsoup4
```

It can be imported using:

```python
from bs4 import BeautifulSoup
```

### Basic Example

```python
from bs4 import BeautifulSoup

html = "<h1>Hello Python</h1>"

soup = BeautifulSoup(html, "html.parser")

print(soup.h1.text)
```

BeautifulSoup parses the HTML and allows us to access elements from the page.

---

# Key Learnings

- Learned command line utilities.
- Learned `sys.argv`.
- Learned the walrus operator `:=`.
- Learned the `shutil` module.
- Learned important `shutil` functions.
- Learned the `requests` module.
- Learned GET requests.
- Learned POST requests.
- Learned the BeautifulSoup library.
- Learned basic HTML parsing.
- Learned the basics of web scraping.

---

# Note

These topics introduced useful Python tools for working with command line arguments, files, directories, HTTP requests, and HTML documents.
