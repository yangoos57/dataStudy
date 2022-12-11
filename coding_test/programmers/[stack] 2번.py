### programmers stack 2

# 조건 생각해서 문제 풀기


def solution(s):
    c = 0
    for v in s:
        if v == "(":
            c += 1
        else:
            c -= 1
        if c < 0:
            return False

    if c > 0:
        return False

    elif c == 0:
        return True
