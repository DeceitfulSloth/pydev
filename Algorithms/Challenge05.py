# Solution to python challenge 05

# Get data from page
from urllib.request import urlopen

# Decode raw data
import pickle

# Get data
rawData = urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

# Decode data
data = pickle.load(rawData)

# Print data
for x in data:
    for y in x:
        print(y[0]*int(y[1]), end = '')
    print('')
