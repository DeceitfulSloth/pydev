# Python challenge 07

# imports
from PIL import Image
import requests, os, re

# get image from file
image = Image.open('data\\07\\oxygen.png')

# print size
width, height = image.size

# Determine rows where greyscale data is encoded.
print(f'Size: {width}, {height}')
print('Greyscale pixels in first column:')
for y in range(height):
    if image.getpixel((0,y))[0] == image.getpixel((0,y))[1] and image.getpixel((0,y))[0] == image.getpixel((0,y))[2]:
        print(y, image.getpixel((0,y)))

# Determine columns where greyscale data is encoded.
print('Greyscale pixels in the 47th row (the 47th row contains the encoded data):')
for x in range(width):
    if image.getpixel((x,47))[0] == image.getpixel((x,47))[1] and image.getpixel((x,47))[0] == image.getpixel((x,47))[2]:
        print(x, image.getpixel((x,47)))

# Add found grey values to list from ranges found earlier.
found_values = []
for x in range(0,608,7):
    found_values.append(image.getpixel((x,47))[0])

# Display found numbers
print(f'found values: {found_values}')

# ASCII conversion
found_letters = []
for i in found_values:
    found_letters.append(chr(i))

# Display found letters
print(f'found letters: {found_letters}')

# Compress array to string
compressed = ''.join(found_letters)
print(compressed)

# Next we need to get the values from the array: [105, 10, 16, 101, 103, 14, 105, 16, 121]
next_level_values = [105, 110, 116, 101, 103, 114, 105, 116, 121]
next_level_letters = []
for i in next_level_values:
    next_level_letters.append(chr(i))

# Finally we print the converted string
next_level = ''.join(next_level_letters)
print(next_level)

# i,LF,DLE,e,g,SO,i,DLE,y


