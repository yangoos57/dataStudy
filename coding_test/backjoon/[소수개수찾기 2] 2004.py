# combination은 factorial로 치환 가능
# 2배수, 5배수를 찾은 다음
# 2배수 또는 5배수의 최소 개수로 따라가면 0 개수를 찾을 수 있음

import sys

m, n = list(map(int, sys.stdin.readline().split()))


answer = []
i = 0
for mul in [2, 5]:
    for num in [m, n, m - n]:
        while True:
            if num < mul**i:
                break
            i += 1

        sum = 0
        for v in range(1, i):
            sum += num // mul**v

        answer.append(sum)


n2 = answer[0] - answer[1] - answer[2]
n5 = answer[3] - answer[4] - answer[5]

print(min(n2, n5))
