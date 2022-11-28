### 점화식을 찾아야하는 문제
# DP인 이유
# 작은 문제로 쪼갤 수 있고, 이전 데이터 조합으로 새로운 값을 만들기 때문

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

import sys

n = int(sys.stdin.readline().rstrip())
input_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

for i in input_list:
    print(dp[i])
