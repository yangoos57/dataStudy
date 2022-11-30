# https://cotak.tistory.com/12

# 다시풀기


# 틀린 방식

import sys

n = int(sys.stdin.readline())
dp = [9] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] * 2 - (2 ** (i - 2))

print(dp[n] % 1000000000)
