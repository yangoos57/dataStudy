## 배울점
# 역순으로 배치하는 것을 많이 배운다..
# 아무래도 역순과 stack이 관련이 있기 때문인듯 하다.

# 문자 재배치 일 경우 for문을 쓰고 list 대신 빈 string('')을 권한다.

# for문에서 역순으로 문자 또는 단어 배치하기 a = i + a
# 한 번에 역순으로 배치하기 [::-1] or reversed()


import sys

new_c = sys.stdin.readline()
answer = ""
change = ""
tag = False
for c in new_c:
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

print("change : ", change)
print(answer + change)
