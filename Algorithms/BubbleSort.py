# Naive Bubble Sort Algorithm
# For educational purposes only

a= [1,2,3,4,5,4,3,2,1]

print(a)

for x in range(len(a)-1):
    for y in range (len(a)-1):
        if a[y] > a[y+1]:
            temp = a[y]
            a[y] = a[y+1]
            a[y+1] = temp

print(a)

