#!/usr/bin/python3
'''A Python script that fetches https://alu-intranet.hbtn.io/status'''

import urllib.request

if __name__ == '__main__':
    url = 'https://0.0.0.0:5050/status'

    # Make the request
    with urllib.request.urlopen(url) as response:
        content = response.read()

    # Display the required output
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode("utf-8")))
