def match(s, p):

    isStar = []
    
    for x in range(len(p)):
        if p[x] == "*":
            isStar.append(True)
        else:
            isStar.append(False)

    patternChunks = []

    pointer = len(p) - 1

    while (pointer >= 0):
        if isStar[pointer]:
            res = p[pointer-1] + "*"
            patternChunks = [res] + patternChunks
            pointer = pointer - 2
        else:
            res = p[pointer]
            patternChunks = [res] + patternChunks
            pointer = pointer -1

    swapOccured = True

    while swapOccured:
        swapOccured = False

        for x in range(len(patternChunks)-1):
            if patternChunks[x][1] ==  "*" and patternChunks[x][0] == patternChunks[x+1]:
                swapOccured = True
                temp = patternChunks[x]
                patternChunks[x] = patternChunks[x+1]
                patternChunks[x+1] = temp
