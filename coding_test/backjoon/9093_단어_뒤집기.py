# 배울점
## pop(index) = 원하는 위치 아이템 띄우기

import sys

n = int(sys.stdin.readline())
input = [sys.stdin.readline().strip() for i in range(n)]

for i in range(n):
    v = input[i].split()
    ba = [i[::-1] for i in v]
    answer = " ".join(ba)
    print(answer)
