# programmers DFS BFS 1


# 다른 사람 방법(DFS로 푼 방법)
# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS


# DFS로 풀기

# 배울점
# i == 5가 될때까지 값을 확장해 나간다는 점에서 DFS 임.
# 지수적으로 늘리고 싶을 떄는 dfs를 여러개로 하면 된다.
# 더하거나 뺀 값을 계속 가지고와서 i == 5 일때 푼다.
# dfs 자체에 return을 설정하지 않았기 때문에 함수의 return은 항상 None
# 굳이 역순으로 재귀를 만들 필요 없다.


def dfs(i, value, answer, c):
    if i == len(numbers):
        answer.append(value)
    else:
        dfs(i + 1, value + numbers[i], answer, c)
        dfs(i + 1, value - numbers[i], answer, c)
        c.append(i + 1)


def solution(numbers, target):
    answer = []
    numbers = numbers
    c = []
    dfs(0, 0, answer, c)
    return answer.count(target)


numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))


# 다른 사람의 방법(DFS로 풀지 않는 방법)
# 배울점
# 1. product((4, -4) (1, -1) (2, -2) (1, -1)) => 2*2*2*2 경우의 수를 생성함
# 2. list.count(x) => x의 개수를 파악할 수 있음.

from itertools import product


def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    print(*l)
    print(list(product(*l)))
    s = list(map(sum, product(*l)))
    print(s)
    print(s.count(target))
    return s.count(target)


numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))


# 정답이 맞더라도 이렇게 풀면 공부가 안될듯


def solution(numbers, target):
    from itertools import product

    lst = [True, False]
    answer = 0
    for i in product(lst, repeat=len(numbers)):
        new_numbers = numbers.copy()
        for j, k in enumerate(i):
            if k == True:
                new_numbers[j] = -new_numbers[j]
        if target == sum(new_numbers):
            # print(i)
            answer += 1

    return answer


numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))
