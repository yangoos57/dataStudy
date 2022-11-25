#

# 문제에서 push하는 순서가 반드시 오름차순이라고 했기 때문에 값이 순차적으로 투입되어야 함.

# 문제 해석 stack과 pop을 활용해 특정 모양의 리스트를 만들 수 있는지를 확인하는 문제임

# 1,2,3,4,5,6,7,8 순서대로 투입하여 [4,3,6,8,7,5,2,1]를 만들 수 있는지를 묻는 문제임

# 특정 순번이 나올 때까지 수를 담아두는 임시 리스트 하나가 필요하다.


# 1,2,3,4,5,6,7,8 순서대로 투입하기 위해 while문과 cur=1 을 쓴다.

# 정답 리스트에 넣어야 하는 값이 나올때 까지 임시 리스트에 값을 저장한다.

# 이때 임시 리스트의 마지막 값과 정답 리스트의 마지막 값이 같으면 임시 리스트에서 빼서 정답 리스트에 넣는다.

# 순번을 돌리고 임시 리스트에 값이 모두 빠져나가면 ok, 임시 리스트에 값이 남아 있으면 stack으로 문제 해결이 불가능하다는 뜻이다.


import sys

n = int(sys.stdin.readline())
input_data = [sys.stdin.readline().strip() for i in range(n)]


c = []
d = []

cur = 1
for i in input_data:
    i = int(i)
    while cur <= i:
        c.append(cur)
        cur += 1
        d.append("+")
    if c[-1] == i:
        c.pop()
        d.append("-")

if c:  # 리스트에 값이 있으면 True, 빈 리스트이면 False를 반환한다.
    print("NO")
else:
    [print(answer) for answer in d]
