def solution(n, k, cmd):
    answer = ['O'] * n
    collector = []
    for c in cmd:
        if c[0] == "U":
            cur_u = int(c.split()[1])
            while cur_u > 0:
                k -= 1
                if k < 0:
                    break
                if answer[k] == 'O':
                    cur_u -= 1
            k = k if k > -1 else 0
        elif c[0] == "D":
            cur_d = int(c.split()[1])
            while cur_d > 0:
                k += 1
                if k > n - 1:
                    break
                if answer[k] == 'O':
                    cur_d -= 1
            k = k if k < n else n - 1
        elif c[0] == "C":
            answer[k] = 'X'
            cur_k = k
            collector.append(k)
            while k < n and answer[k] == 'X':
                k += 1
            if k == n:
                while cur_k > -1 and answer[cur_k] == 'X':
                    cur_k -= 1
                k = cur_k
        elif c[0] == "Z":
            z = collector.pop()
            answer[z] = 'O'
    return ''.join(answer)