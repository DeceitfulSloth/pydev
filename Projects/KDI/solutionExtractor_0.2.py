# Extract files from folder
# @author: Jason Oliver - jason.oliver@uni.kn

import os, re, sys, zipfile, shutil

print('Solution Extractor 0.2')
print('The current working directory is: ' + os.getcwd())

print('Searching for "Assignment..."')
result = ""
files = os.listdir()
for x in files:
    searcher = re.search("^Assignment.*.zip$", x)
    if searcher != None:
        # success
        print('Suitable zip file found: ' + x)
        result = x
    
while (result == ""):
    print('No suitable file found in directory.')
    print('Enter target directory to continue or leave blank to quit.')
    response = input()
    if response == "":
        sys.exit()
    else:
        os.chdir(response)
        files = os.listdir()
        for x in files:
            searcher = re.search("^Assignment.*.zip$", x)
            if searcher != None:
                # success
                print('Suitable zip file found: ' + x)
                result = x

# Now that we have a file we will extract it

zippedFile = zipfile.ZipFile(result)
content = zippedFile.namelist()
for x in content:
    zippedFile.extract(x)
zippedFile.close()

os.chdir(result[:-4])
#print('Moved to directory: ' + os.getcwd())

# Create folders for the solutions
for x in range(1,7):
    os.mkdir(str(x))

os.mkdir('bad people who cannot follow instructions')

#print('Created solution folders by group')

userFolders = os.listdir('Abgaben')

for x in userFolders:
    
    individualFile = os.listdir(os.path.join('Abgaben', x))[0]
    
    firstDigit = individualFile[0:1]
    first2Digits = individualFile[0:2]

    #print(individualFile)    

    if firstDigit == "1" or first2Digits == "01":
        # Move to group 1
        shutil.move(os.path.join('Abgaben', x, individualFile), os.path.join('1'))
    elif firstDigit == "2" or first2Digits == "02":
        # Move to group 2
        shutil.move(os.path.join('Abgaben', x, individualFile), os.path.join('2'))
    elif firstDigit == "3" or first2Digits == "03":
        # Move to group 3
        shutil.move(os.path.join('Abgaben', x, individualFile), os.path.join('3'))
    elif firstDigit == "4" or first2Digits == "04":
        # Move to group 4
        shutil.move(os.path.join('Abgaben', x, individualFile), os.path.join('4'))
    elif firstDigit == "5" or first2Digits == "05":
        # Move to group 5
        shutil.move(os.path.join('Abgaben', x, individualFile), os.path.join('5'))
    elif firstDigit == "6" or first2Digits == "06":
        # Move to group 6
        shutil.move(os.path.join('Abgaben', x, individualFile), os.path.join('6'))
    else:
        # Move to group bad people
        shutil.move(os.path.join('Abgaben', x, individualFile), os.path.join('bad people who cannot follow instructions'))

print('Extraction completed successfully')


# Remove unneeded files and folders.
response = ""
while response != "y" and response != "n":
    print('Remove empty folders and .zip file? (y/n)')
    response = input()
    
if response == "n":
    pass
    print('No files or folders removed')
elif response == "y":
    shutil.rmtree("Abgaben")
    os.chdir("..")
    os.remove(result)
    print('Files & folders removed')

# Remove
response = ""
while response != "y" and response != "n":
    print('Delete all submissions from all groups except own group? (y/n)')
    print('This is useful to save space with files downloaded which will be marked by other tutors.')
    response = input()
    
if response == "n":
    pass
elif response == "y":
    print (os.getcwd())






print('Script complete. Press enter to exit.')
input()














