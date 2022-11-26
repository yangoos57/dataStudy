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
