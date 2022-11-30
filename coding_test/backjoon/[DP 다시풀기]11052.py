# https://www.acmicpc.net/problem/11052

# DP 문제였지만 Greedy로 접근하게 되는 문제

# 다르게 말하면 모든 경우의 수를 고려하는 문제를 매번 최선을 선택한 방식으로 문제를 풀었다.

# DP 문제이므로 점화식을 찾으려 했는데 규칙이 어떻게 형성되는지 모르겠다.


# Greedy로 접근했던 방식
import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst = [0] + lst

avg_lst = [0] * (n + 1)

# 주어진 선택지의 개당 값을 구해서 최대 값을 비교하는 방식으로 진행하려고 했음
for i in range(1, n + 1):
    avg_lst[i] = lst[i] / i


count_lst = []
while n > 0:
    # 고를 수 있는 선택지 중 max 선택, [:n+1]을 한 이유는 n이 줄어들수록 선택지를 줄이기 위함
    max_avg = max(avg_lst[: n + 1])

    # avg_lst 중 n보다 작은 값중 max를 찾고 종료
    for i in range(1, len(avg_lst)):
        if n >= i and max_avg == avg_lst[i]:
            n -= i
            count_lst.append(i)
            break

# 이렇게 모은 값을 더함
c = 0
for i in count_lst:
    c += lst[i]

print(c)
