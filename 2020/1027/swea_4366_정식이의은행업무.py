import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    twoNum = input()
    threeNum = input()

    intTwo = int(twoNum, 2)
    intThree = int(threeNum, 3)
    difference = intThree - intTwo

    twoList = []
    threeList = []

    for i in range(len(twoNum)):
        curNum = int(twoNum[i])
        if curNum:
            twoList.append(-2 ** (len(twoNum)-1-i))
        else:
            twoList.append(2 ** (len(twoNum)-1-i))

    for i in range(len(threeNum)):
        curNum = int(threeNum[i])
        if curNum == 2:
            threeList.append(-3 ** (len(threeNum)- 1 - i))
            threeList.append(-(3 ** (len(threeNum) - 1 - i)) * 2)
        elif curNum == 1:
            threeList.append(3 ** (len(threeNum)-1-i))
            threeList.append(-3 ** (len(threeNum) - 1 - i))
        else:
            threeList.append(3 ** (len(threeNum) - 1 - i))
            threeList.append((3 ** (len(threeNum) - 1 - i)) * 2)

    result = 0
    for m in range(len(twoList)):
        for n in range(len(threeList)):
            if twoList[m] - threeList[n] == difference:
                result = intTwo + twoList[m]
                break

        if result:
            break

    print('#{} {}'.format(tc+1, result))
