N, M = 3, 7
coins = [2, 3, 5]

cache = [M + 2 for _ in range(M + 1)]

for c in coins:
    cache[c] = 1

result = -1
for i in range(min(coins), M + 1):
    if cache[i] == M + 2:
        min_coin = M + 2
        for d in coins:
            if min_coin > cache[i - d]:
                min_coin = cache[i - d]
        cache[i] = min_coin + 1

if cache[M] == M + 2:
    print(-1)
else:
    print(cache[M])