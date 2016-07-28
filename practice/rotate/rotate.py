"""Uses request to print the HTML of a given website entered as an argument on the command line."""


import requests
import sys


def get_request_object(website):
    """Gets a request object to be manipulated.

    >>> get_request_object('https://www.google.com/')
    words
    """
    return requests.get(website)


def output(request_object):
    """Prints out the text of the request object.

    >>> output()
    words
    """
    print(request_object.text)


def main():
    request_object = get_request_object(sys.argv[1])
    output(request_object)
if __name__ == '__main__':
    main()