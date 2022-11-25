## 배울점
# 문자 역순 배치는 stack 문제이다.
# 문자 재배치 문제인 경우 for문을 통해 해결한다.
# list 대신 빈 string('')을 사용한다.

# 매우중요!!
# 역순으로 문자 또는 단어 배치하기 for문을 사용하고 a = i + a로 쓴다.

# a += str 은 stack
# a = str + a 는 queue


import sys

sen = sys.stdin.readline().rstrip()
answer = ""
change = ""
tag = False
for c in sen:
    if tag == False:
        if c == "<":
            tag = True
            if change:
                answer += change
                change = ""
            answer += c

        elif c == " ":
            # stack 방식으로 쌓기
            answer += change
            answer += c
            change = ""
        else:
            # queue 방식으로 쌓기
            change = c + change

    else:
        if c == ">":
            tag = False
            answer += c
        else:
            answer += c

print(answer + change)


# import sys

# sen = sys.stdin.readline().rstrip()

holding = ""
changing = ""

answer = []

for c in sen:
    if c == "<":
        holding += c
        if len(changing) != 0:
            answer.append(changing)
            changing = ""

    elif len(holding) > 0 and c != ">":
        holding += c

    elif c == ">":
        holding += c
        answer.append(holding)
        holding = ""

    else:
        if c == " ":
            answer.append(changing)
            answer.append(c)
            changing = ""
        else:
            changing = c + changing


answer = "".join(answer) + changing

print(answer)
