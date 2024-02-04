# Python challenge 10

# We are given the beginning of a series a = [1, 11, 21, 1211, 111221,
# We are asked len(a[30]) = ?
# Thus we must calculate the series, or at least the length of the items.

# The series is a look-and-say sequence

def getNext(value):
    string = str(value)

    return_val = ""
    counter = -1
    
    for i in range(len(string)):
        if i == 0 or string[i] != string[i-1]:
            # New value
            if i == 0:
                counter = 1
            else:   
                return_val = return_val + str(counter) + str(string[i-1])
                counter = 1
        else:
            counter += 1

    return_val = return_val + str(counter) + str(string[-1])

    return return_val


def getSequence(n):
    values = ['1']

    for i in range(n-1):
        values.append(getNext(values[-1]))

    return values

a = getSequence(31)

print(type(a))
print(len(a))
print(len(a[30]))

#http://www.pythonchallenge.com/pc/return/5808.html
