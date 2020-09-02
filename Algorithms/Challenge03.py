# Python challenge 3
# We need to find a character sequence with 3 big, 1 small, 3 big, with all big the same

# Import os for file access and re for regex.
import os, re

# Determine file location on my laptop.
cwd = os.getcwd()
dataFolder = cwd + "\\data"
#print(dataFolder)
filePath = dataFolder + "\\03.txt"
#print(filePath)

# Verify file existence.
print("File containing target data found: " + str(os.path.isfile(filePath)))

# Read file.
text = open(filePath).read()

# Search text for all occurences matching our regex.
# Note the the brackets to only show the middle lower case letter
result = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text)

# Join resulting strings for easier reading.
result = "".join(result)

print(result)
