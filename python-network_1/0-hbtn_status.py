        #!/usr/bin/python3
import urllib.request

url = "https://alu-intranet.hbtn.io/status"

# Fetching the URL content
with urllib.request.urlopen(url) as response:
    body = response.read()

# Printing the response body details
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
