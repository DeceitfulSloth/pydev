# Basic Insertion Sort
# For educational purposes only
# Uses swaps

a = [1,2,3,4,5,4,3,2,1]

for x in range(len(a)-1, 0, -1):
    bigVal = None
    bigPos = None
    for y in range(0, x, 1):
        if str(type(bigVal)) == "<class 'NoneType'>" or a[y] > bigVal:
            bigVal = a[y]
            bigPos = y

    a[bigPos] = a[x]
    a[x] = bigVal

print(a)
        
