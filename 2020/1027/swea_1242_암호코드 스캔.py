import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

numDict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

for tc in range(T):
    if tc == 14:
        a = 1
    N, M = map(int, input().split())

    passwords = []
    for n in range(N):
        line = input().strip('0')
        if '0000' in line:
            temps = line.split('0000')
            for temp in temps:
                temp = temp.strip('0')
                if temp and temp not in passwords:
                    for p in passwords:
                        if p in temp:
                            break
                    else:
                        passwords.append(temp)
        elif line:
            if line not in passwords:
                passwords.append(line)

    binPasswords = []
    for password in passwords:
        binList = []
        for p in password:
            n = int(p, 16)
            binList.append('1' if n & 8 else '0')
            binList.append('1' if n & 4 else '0')
            binList.append('1' if n & 2 else '0')
            binList.append('1' if n & 1 else '0')
        binPassword = ''.join(binList).rstrip('0').lstrip('0')
        lenBin = len(binPassword)
        n = 1
        while len(binPassword) > 7 * n:
            final_code = binPassword[len(binPassword) - 7 * n:len(binPassword)]
            final_code = final_code.replace('0' * n, '0')
            final_code = final_code.replace('1' * n, '1')
            val = numDict.get(final_code)
            if val is not None:
                break
            else:
                n += 1
        else:
            continue

        if lenBin < 56 * n:
            for _ in range(56 * n - lenBin):
                binPassword = '0' + binPassword
        lenBin = len(binPassword)
        temp = binPassword[lenBin - 56 * n: lenBin]
        temp = temp.replace('0' * n, '0')
        temp = temp.replace('1' * n, '1')
        if not len(temp) % 56:
            binPasswords.append(temp)

    result = 0

    for binP in binPasswords:
        nums = []
        for i in range(8):
            cur_code = binP[i*7:i*7+7]
            if numDict.get(cur_code) is not None:
                nums.append(numDict.get(cur_code))
            else:
                continue
        if len(nums) == 8 and ((nums[0] + nums[2] + nums[4] + nums[6]) * 3 + (nums[1] + nums[3] + nums[5]) + nums[7]) % 10 == 0:
            result += sum(nums)

    print('#{} {}'.format(tc + 1, result))