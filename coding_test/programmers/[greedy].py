# 문제

# 틀린이유
# 좌우 이동을 오른쪽만, 왼쪽만을 고민했던 것 같다.
# ABAAAB같은 경우는 오왼왼 이동하도록 해야함.


def solution(name):
    alpha_list = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    # 상하 이동 최솟값(문제 없음)
    def change_alpha(alpha):
        idx = alpha_list.index(alpha)

        if idx >= 13:
            answer = 26 - idx
        else:
            answer = idx

        return answer

    answer = 0
    for s in name:
        answer += change_alpha(s)

    #### 좌우 이동 최솟값(문제 있음)

    # 찾아야하는 A 외 Alphabet
    obj = 0
    for s in name[1:]:
        if s != "A":
            obj += 1

    from itertools import product

    # 경우의 수 생성(AABBA인 경우 최대 4번 이동가능)
    x = [(-1, 1)] * (len(name) - 1)

    new_name = name[1:] + name

    lst = [len(name) - 1]
    for j in product(*x):
        result = 0
        idx = len(name) - 1
        visited = [False] * (len(new_name) + 1)

        for n, i in enumerate(j):
            idx += i
            if new_name[idx] != "A" and visited[idx] == False:
                visited[idx] = True
                result += 1

            if obj == result:
                lst.append(n + 1)
                break

    answer += min(lst)

    return answer


# 원구조 어떻게 만들지


# name = "ABABAAAAAAABA"
name = "JAN"


print(solution(name))
