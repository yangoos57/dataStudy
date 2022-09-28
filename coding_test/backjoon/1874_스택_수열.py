# 배운점
# While을 쓰면 원하는 숫자에서 종료시킬 수 있음
# While을 쓰고 cur = 1 초기화 안하면 연속된 수 list 쓴것과 같은 효고..
# 말로 하니 어렵네. cur이 변화가 없다는 걸 알고 보면 이해할듯


import sys

n = int(sys.stdin.readline())
input = [sys.stdin.readline().strip() for i in range(n)]


c = []
d = []
cur = 1
for i in input:
    i = int(i)
    while cur <= i:
        c.append(cur)
        cur += 1
        d.append("+")
    if c[-1] == i:
        c.pop(-1)
        d.append("-")

if c:
    print("NO")
else:
    [print(answer) for answer in d]
