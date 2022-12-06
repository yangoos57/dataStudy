# programmers brute force 5

# 탐험 가능한 최대 던전 수
# max 8개 던전
# 최소 필요 >= 소모
# 1 ~ 1000
# 던전끼리 같을 수 있다.


def solution(k, dungeons):
    from itertools import permutations

    answer = 0
    for i in permutations(dungeons, len(dungeons)):
        c = 0
        en = k
        for j in i:
            if en >= j[0]:
                en -= j[1]
                c += 1
            if en <= 0:
                break
        # print(i, c)
        answer = max(answer, c)

    return answer


k = 80
dungeons = [[80, 20], [20, 10], [50, 30], [30, 10]]
print(solution(k, dungeons))
