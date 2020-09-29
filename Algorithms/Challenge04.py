# Solution to challenge 4 of the python challenge
# This solution will work in one run, but could only be created with some trial and error

# Requests for downloading webpages, re for parsing page content
import requests, re

# Basic URL we will be using
baseURL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = "12345"

# repeating search control
failed = False
while (failed == False):

    # Get webpage
    res = requests.get(baseURL + num)

    # If page successfully found:
    if(res.status_code == requests.codes.ok):
        print('Request ok')
        print(res.text)

        # Search for all occurences as it returns an array of strings
        target = re.findall('the next nothing is ([0-9]+)', res.text)

        # Exactly one result found. Normal case.
        if (len(target) == 1):
            num = target[0]

        # Special case.
        elif (res.text == 'Yes. Divide by two and keep going.'):
            num = str(int(num)/2)

        # Error or end state
        else:
            print('Unhandled page text.')
            failed = True

    # If number found from previous page does not lead to a valid webpage:
    else:
        print('Target not found')
        print('Current num: ' + num)
        failed = True


    
