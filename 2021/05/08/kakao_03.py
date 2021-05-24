def solution(n, k, cmd):
    answer = ['O'] * n
    idxs = [i for i in range(n)]
    collector = []
    remain_num = n
    for c in cmd:
        if c[0] == "U":
            cur_u = int(c.split()[1])
            # while cur_u > 0:
            #     k -= 1
            #     if k < 0:
            #         break
            #     if answer[k] == 'O':
            #         cur_u -= 1
            k = idxs[idxs[k] - cur_d] if k - cur_d > -1 else 0
            # k = k if k > -1 else 0
        elif c[0] == "D":
            cur_d = int(c.split()[1])
            # while cur_d > 0:
            #     k += 1
            #     if k > n - 1:
            #         break
            #     if answer[k] == 'O':
            #         cur_d -= 1
            k = idxs[idxs[k] + cur_d] if k + cur_d < n else n - 1
            # k = k if k < n else n - 1
        elif c[0] == "C":
            answer[k] = 'X'
            cur_k = k
            collector.append(k)
            remain_num -= 1

            for i in range(cur_k, remain_num):
                idxs[i] = idxs[i - 1]
            while k < n and answer[k] == 'X':
                k += 1
            if k == n:
                while cur_k > -1 and answer[cur_k] == 'X':
                    cur_k -= 1
                k = cur_k
        elif c[0] == "Z":
            z = collector.pop()
            answer[z] = 'O'
            add_idx = -1
            for i in range(remain_num - 1):
                if idxs[i + 1] > z:
                    add_idx = i
            remain_num += 1

            if add_idx != -1:
                for j in range(add_idx + 1, remain_num):
                    idxs[j] = idxs[j - 1]
                idxs[add_idx] = z

    return ''.join(answer)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))