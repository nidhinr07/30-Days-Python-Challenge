# Day 18 - Requests Module and BeautifulSoup

import requests
from bs4 import BeautifulSoup


# -----------------------------------
# GET Request
# -----------------------------------

url = "https://example.com"                  # Store website URL

response = requests.get(url)                 # Send GET request

print(response.status_code)                   # Display response status

print(response.text)                         # Display webpage content


# -----------------------------------
# POST Request
# -----------------------------------

data = {
    "name": "Alex",
    "age": 20
}                                            # Store data to send

response = requests.post(
    "https://httpbin.org/post",
    data=data
)                                            # Send POST request

print(response.status_code)                  # Display response status

print(response.text)                         # Display response data


# -----------------------------------
# BeautifulSoup
# -----------------------------------

html = """
<html>
    <body>
        <h1>Python Learning</h1>
        <p>Day 18</p>
    </body>
</html>
"""                                          # Store sample HTML

soup = BeautifulSoup(
    html,
    "html.parser"
)                                            # Parse HTML content

print(soup.h1.text)                          # Get heading text

print(soup.p.text)                           # Get paragraph text
