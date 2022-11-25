# 배운점
# Stack의 중요성을 알게해준 문제!!
# 커서 문제는 stack으로 풀면 된다.
# 커서 앞과 뒤를 리스트로 구분하면 pop과 append를 써서 문제를 풀 수 있다.

# 내가 접근한 방식은 index 위치를 매번 기록하고 slicing으로 해결하는 것이었음.
# 하지만 slicing은 O(N)이므로 사용해서는 안됐다.
# append와 pop으로 문제 해결할 방법을 고민했어야 했다.


import sys

# 커서 앞(rstrip 써서 문장 공백 들어간것 제거하자, 에러인지 모르겠지만 문제에서 문장 끝에 공백 들어간게 나오더라)
st1 = list(sys.stdin.readline().rstrip())

# 커서 뒤
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == "P":
        st1.append(command[1])
    elif command[0] == "L":
        if st1:
            st2.append(st1.pop())
    elif command[0] == "D":
        if st2:
            st1.append(st2.pop())
    else:
        if st1:
            st1.pop()

# 커서 뒤 값 마지막에 바꿔주기
st1.extend(reversed(st2))
print("".join(st1))


#

import sys

sen = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
order_list = [sys.stdin.readline().strip() for i in range(n)]

cur_idx = len(sen)


for order in order_list:
    if order == "L":
        if cur_idx != 0:
            # 1 왼쪽 이동하는 효과
            cur_idx -= 1

    elif order == "D":
        if cur_idx != len(sen):
            # 1 오른쪽 이동 효괴
            cur_idx += 1

    elif order == "B":
        if cur_idx != 0:
            sen = sen[: cur_idx - 1] + sen[cur_idx:]
            cur_idx -= 1
    else:
        var = order.split()
        sen = sen[:cur_idx] + var[1] + sen[cur_idx:]

        if cur_idx != len(sen):
            cur_idx += 1

    print(sen, "")

if sen == "abcdyx":
    print(sen)
else:
    print("error")
