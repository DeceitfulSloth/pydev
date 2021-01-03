import os, sys

fileLocation = os.path.join(os.getcwd(),"data","02.txt")

if os.path.isfile(fileLocation):
    print("File found")
else:
    print("File not found")
    sys.exit()

chars = []
counts = []
location = 0

f = open(fileLocation, "r")
for x in f.read():

    try:
        location = chars.index(x)
        counts[location] = counts[location] + 1
    except:
        location = len(chars)
        chars.append(x)
        counts.append(1)
        
pairs = dict(zip(chars, counts))

final = []

for x, y in pairs.items():
    if y == 1:
        final.append(x)


print("Target word: " + "".join(final))
