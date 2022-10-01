
validNs = []

n = 1
while len(validNs) != 6:
    solutionFound = False
    for a in range(0,10):
        for b in range(0,7):
            for c in range(0,3):
                # print(6*a + 9*b)
                if 6*a + 9*b + 20*c == n:
                    solutionFound = True
    if solutionFound:
        validNs.append(n)
        # print(n)
    else:
        validNs.clear()
    n+=1

print(validNs[0] -1)
