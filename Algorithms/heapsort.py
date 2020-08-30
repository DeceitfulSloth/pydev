# Heapsort sorting algorithm implementation
# For educational purposes

def makeHeap(array):
    print('Making heap')
    print('Calculating sink range')
    numToSink = len(array) // 2
    print('Sinking the first ' + str(numToSink) + ' elements of the array')
    for x in range(numToSink-1, 0, -1):
        sink(array, x, len(array))
    print('Heap built')
    print(arrayg)

def swap(array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

def sink(array, index, length):
    leftPos = ((index + 1) * 2) - 1
    rightPos = ((index + 1) * 2)
    biggest = "N"
    if (leftPos < length):   # right child in range
        left = array[leftPos]
        biggest = "L"
    if (rightPos < length):
        right = array[rightPos]
        if right > left:
            biggest = "R"
    if biggest == "N":
        return
    elif biggest == "L":
        # swap in array positions index and leftpos
        swap(array, index, leftPos)
        sink(array, leftPos, length)
    else:
        # swap in array positions index and rightPos
        swap(array, index, rightPos)
        sink(array, rightPos, length)
    

def sort(array, length):
    makeHeap(array)
    sortHeap(array, length)



a = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]

print(a)

sort(a, len(a))

print(a)
