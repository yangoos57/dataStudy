## 배울점
# 1,-1로 푸는건 아닌 듯
# Stack을 공부하는 문제인듯


import sys

n = int(sys.stdin.readline())
input = [sys.stdin.readline().strip() for i in range(n)]


def k(a):
    if a == "(":
        return 1
    else:
        return -1


def func(new_a):
    if new_a[0] == -1:
        return print("NO")
    elif sum(new_a) != 0:
        return print("NO")
    else:
        k = 0
        for i in new_a:
            k += i
            if k < 0:
                return print("NO")

    return print("YES")


for i in range(n):
    a = input[i].split()
    ist_a = list(a[0])
    new_a = list(map(k, ist_a))
    func(new_a)
