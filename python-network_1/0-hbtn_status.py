#!/usr/bin/python3
'''A Python script that fetches a URL'''

import urllib.request

if __name__ == '__main__':
    url = 'https://alu-intranet.hbtn.io/status'  # Make sure the URL is correct
    # Add custom headers, including User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    request = urllib.request.Request(url, headers=headers)  # Pass the headers to the request
    try:
        with urllib.request.urlopen(request) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print("HTTP Error: {} - {}".format(e.code, e.reason))
    except urllib.error.URLError as e:
        print("URL Error: {}".format(e.reason))
