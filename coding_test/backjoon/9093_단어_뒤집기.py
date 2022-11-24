# 배울점
## string에서 [::-1]은 역순 배열이다.

import sys

n = int(sys.stdin.readline())
input = [sys.stdin.readline().strip() for i in range(n)]

for i in range(n):
    v = input[i].split()
    ba = [i[::-1] for i in v]
    answer = " ".join(ba)
    print(answer)
