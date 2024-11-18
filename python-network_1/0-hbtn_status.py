#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using urllib"""

import urllib.request

url = "https://alu-intranet.hbtn.io/status"

# Fetch and process the response using a `with` statement
with urllib.request.urlopen(url) as response:
    body = response.read()

# Print the body details as required
print("Body response:")
print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))
print("\t- utf8 content: {}".format(body.decode("utf-8")))
