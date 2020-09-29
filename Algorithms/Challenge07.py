# Python challenge 07

from PIL import Image
import requests, os, re

image = Image.open('data\\07\\oxygen.png')

width, height = image.size

#print (str(width) + ' ' + str(height))

values = []

#print(image.getpixel((5,5)))



for x in range(width):
    image.putpixel((x, int(height/2)),(255,0,0))

    values.append(image.getpixel((x, int(height/2) + 1)))
    
    image.putpixel((x, int(height/2) + 2),(255,0,0))

culledValues = []

for x in values:
    culledValues.append(x[0])    

final = []

for x in range(607):
    #print('X: '+str(x))
    #try:
        #print('Final value in final: ' + str(final[len(final)-1]))
    #except:
        #print('Final value in final: does not exist')
    #print('Value under consideration: ' + str(culledValues[x]))
    if x == 0:
        final.append(culledValues[x])
        #print('First item')
    else:
        if str(final[len(final)-1]) != str(culledValues[x]):
            final.append(culledValues[x])
            #print('Copied value')
        #else:
            #print('Did not copy')
            
    #input()


firstText = ''.join(map(chr, final))

nums = re.findall('[0-9]+',firstText)

secondText = ''.join(map(chr, map(int, nums)))

print(secondText)


