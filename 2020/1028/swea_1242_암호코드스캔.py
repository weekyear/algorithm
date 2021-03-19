barcodes = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}

hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000',
    '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    data_list = [input() for _ in range(N)]
    binaryData = []

    bar_type = {}
    for i in range(N):
        temp = []
        if not bar_type.get(data_list[i]):
            bar_type[data_list[i]] = 1
            for d in data_list[i]:
                temp.extend(hex_to_bin[d])
            binaryData.append(''.join(temp))

    answer = 0
    pass_type = {}
    for data in binaryData:
        password = [0] * 8
        idx = M * 4 - 1
        cnt = 7
        while idx > -1:
            a = b = c = 0
            if data[idx] != '0':
                while data[idx] == '1': c += 1; idx -= 1
                while data[idx] == '0': b += 1; idx -= 1
                while data[idx] == '1': a += 1; idx -= 1
                while idx > 0 and data[idx] == '0': idx -= 1

                div_num = min(a, b, c)
                num = barcodes[str(a // div_num) + str(b // div_num) + str(c // div_num)]
                password[cnt] = num
                cnt -= 1

                if cnt == -1:
                    pass_key = ''.join(map(str, password))
                    if not pass_type.get(pass_key):
                        pass_type[pass_key] = 1
                        if ((password[0] + password[2] + password[4] + password[6]) * 3 + (password[1] + password[3] + password[5]) + password[7]) % 10 == 0:
                            answer += sum(password)
                    cnt = 7
            else:
                idx -= 1

    print('#{} {}'.format(tc+1, answer))