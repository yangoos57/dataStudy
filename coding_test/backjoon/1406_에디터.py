# 배운점
# Stack의 중요성을 알게해준 문제!!
# Stack은 커서라고 생객하면 된다.
# 앞/뒤 로 쪼깨는 용도로 사용하면 매우 좋음

# Pop은 시간복잡도 1이므로 Stack과 함께 쓰면 시간을 절약할 수 있음!!!!
# append도 시간복잡도 1이므로 Stack과 함께 쓰면 시간 절약!!

import sys

# 커서 앞
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


# import sys

# sen = sys.stdin.readline()
# n = int(sys.stdin.readline())
# input_list = [sys.stdin.readline().strip() for i in range(n)]


# new_sen = list(sen)
# new_sen.remove("\n")

# inputs = input_list

# cursor = len(new_sen)
# for input in inputs:

#     var = input.split(" ")

#     if var[0] == "L":
#         if cursor != 0:
#             cursor -= 1

#     elif var[0] == "D":
#         if cursor != len(sen):
#             cursor += 1

#     elif var[0] == "B":
#         if cursor != 0:
#             new_sen.pop(cursor - 1)
#             cursor -= 1

#     elif var[0] == "P":
#         new_sen.insert(cursor, var[1])
#         if cursor != len(sen):
#             cursor += 1
# print("".join(new_sen))
