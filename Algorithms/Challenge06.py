# Python challgenge 06

import os, re, zipfile

# Get data folder
dataFolder = os.getcwd() + "\\data\\06"

file = zipfile.ZipFile(dataFolder + "\\channel.zip")

num = '90052'
comments = []

while True:
    f = file.read(num + '.txt').decode("utf-8")
    
    comments.append(file.getinfo(num + '.txt').comment.decode("utf-8"))

    result = re.search('([0-9]+)',f)
    if result == None:
        break
    
    num = result.group(1)

combined = ''.join(comments)

print(combined)
