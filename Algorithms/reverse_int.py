
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    ret = 0
        
    if x >= 0:
        rev = str(x)[::-1]
        ret = int(rev)
        print(ret)
                        
    else:
        pos = str(x)[1::]
        rev = pos[::-1]
        neg = "-" + rev
        ret = int(neg)

    print(ret)   
    if isValid(ret):
        return x
    else:
        return 0

def isValid(x):
    if x >= -(2^31) and x < 2^31:
        return True
    else:
        if x >= -(2^31):
            print('Big enough')
        else:
            print('Not big enough')
        if x < 2^31:
            print('Small enough')
        else:
            print('Not small enough')

print(reverse(-15))
