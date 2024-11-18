#!/usr/bin/python3
'''A Python script that fetches a URL'''

import urllib.request

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    # Create a Request object with a custom User-Agent header
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))

