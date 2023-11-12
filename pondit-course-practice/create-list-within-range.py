import math

minNum = int(input())
maxNum = int(input())


def createList(r1, r2):
    if r1 == r2:
        return r1
    else:
        res = []
        while r1 < r2+1:
            res.append(r1)
            r1 += 1
        return res


if minNum < maxNum:
    numList = createList(minNum, maxNum)
else:
    numList = createList(maxNum, minNum)

print(numList)

for n in range(minNum, maxNum+1):
    if n > 1:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                break
            else:
                print(n)
