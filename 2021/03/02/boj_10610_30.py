import sys
sys.stdin = open('input_10610.txt', 'r')

N = input()

isExistZero = False
allSum = 0

for n in N:
    if n == '0':
        isExistZero = True
    else:
        allSum += int(n)

if allSum % 3 == 0 and isExistZero:
    listN = list(map(int, list(N)))
    listN.sort(reverse=True)
    strN = ''.join(str(e) for e in listN)
    print(int(strN))
else:
    print(-1)