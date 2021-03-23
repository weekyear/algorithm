N = 26

cache = [0 for _ in range(N + 1)]
cache[2] = 1
cache[3] = 1
cache[5] = 1

def dp(n):
    if n == 1:
        return 1

    if not cache[n]:
        enable_lst = []
        for a in [2, 3, 5]:
            if not n % a:
                enable_lst.append(dp(n // a))
        enable_lst.append(dp(n - 1))

        cache[n] = min(enable_lst) + 1

    return cache[n]

print(dp(26))