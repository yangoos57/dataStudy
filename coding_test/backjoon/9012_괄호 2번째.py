# 띄어쓰기만 split()이 가능
# 글자 하나씩 불러올 때는 for문을 써야한다.

import sys

n = int(sys.stdin.readline())
input_data = [sys.stdin.readline().strip() for i in range(n)]

for i in input_data:
    b = 0
    for k in i:
        if k == "(":
            b += 1
        else:
            b -= 1
        if b < 0:
            print("No")
            break
    if b == 0:
        print("Yes")
    elif b > 0:
        print("No")
