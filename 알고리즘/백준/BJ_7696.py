def check(num, boundaryList, startList):
    startNum = -1
    loc = 0
    for i in range(len(boundaryList)):
        temp = boundaryList[i]
        if num < temp:
            startNum = boundaryList[i-1]
            loc = startList[i-1]
            break

    return startNum, loc

def found(num, startNum, loc):
    ans = 0
    count = num - startNum
    while True:
        tempStr = str(loc)
        tempSet = set(tempStr)
        if len(tempSet) == len(tempStr):
            count -= 1
        if count == 0:
            ans = loc
            break
        
        loc += 1
    return ans
        


boundaryList = [0, 9, 90]
startList = [1, 10, 100, 1000, 10000, 100000, 1000000]
standard = 81
sumList = 90
for i in range(8, 4, -1):
    standard *= i
    count = sumList + (standard)
    sumList = count
    boundaryList.append(count)

while True:
    n = int(input())
    if n == 0:
        break
    else:
        startNum, loc = check(n, boundaryList, startList)
        max_ = found(n, startNum, loc)
        print(max_)
        

