# programmers DFS BFS 1


# 배울점
# i == 5가 될때까지 값을 확장해 나간다는 점에서 DFS 임.
# 지수적으로 늘리고 싶을 떄는 dfs를 여러개로 하면 된다.
# 더하거나 뺀 값을 계속 가지고와서 i == 5 일때 푼다.
# dfs 자체에 return을 설정하지 않았기 때문에 함수의 return은 항상 None
# 굳이 역순으로 갈 필요 없다.


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
