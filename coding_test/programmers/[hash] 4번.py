### Programmers hash 4

# 조합에 대한 통찰이 필요한 문제

# 1. 조합 문제는 개수가 증가할수록 지수적으로 증가함
# 3C0 + 3C1 +3C2 + 3C3 = 8
# 4C0 + 4C1 + 4C2 + 4C3 +4C4 = 16
# ...
# nC0 + nC1 + ... + nCn = 2^n
# 2^16 = 65536 2^30은 억단위 넘어감..

# 2. 하위 항목이 있는 모든 경우의 수 쉽게 연산하는 방법
# 하위 항목이 포함되지 않은 경우를 1개 추가해서 연산하고 마지막으로 모두 포함되지 않는 경우인 1을 뺌
# a = 2, b = 3, c = 4개일 때(하위 항목은 구분 가능)
# 3 * 4 * 5 = 모든 경우의 수임.
# 이때 모두 들어가지 않는 0,0,0인 경우를 뺴야하므로
# 정답은 3*4*5 -1 = 59


def solution(clothes):
    from collections import defaultdict

    dic = defaultdict(int)
    for i, c in clothes:
        dic[c] += 1

    answer = 1
    for i in dic.values():
        answer *= i + 1

    return answer - 1


n = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
    ["crow_mask", "face"],
    ["blue_sunglasses", "face"],
    ["smoky_makeup", "face"],
]
# n = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(n))
