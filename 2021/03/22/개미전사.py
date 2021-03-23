N = 4
foods = [1, 3, 1, 5]

def dp(n):
    if n < 2:
        return foods[n]

    return max(dp(n - 2), dp(n - 3) + foods[n - 1])

print(dp(4))