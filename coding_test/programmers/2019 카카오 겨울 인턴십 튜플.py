# 2019 카카오 겨울 인턴십 튜플

# https://school.programmers.co.kr/learn/courses/30/lessons/64065

# 원소의 개수가 n개이고, 중복되는 원소가 없는 튜플 (a1, a2, a3, ..., an)이 주어질 때(단, a1, a2, ..., an은 자연수), 이는 다음과 같이 집합 기호 '{', '}'를 이용해 표현할 수 있습니다.

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"


def solution(s):
    v = s[1:-1].split("},")
    x = list(map(lambda x: x.replace("{", "").replace("}", "").split(","), v))
    k = sorted(x, key=lambda x: len(x))

    answer = []
    for i in k:
        for j in i:
            if j not in answer:
                answer.append(j)

    return list(map(int, answer))


solution(s)
