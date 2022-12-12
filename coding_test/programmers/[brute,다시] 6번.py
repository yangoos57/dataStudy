### Programmers brute force 6


# ㅅㅂ 1번 때문에 통과가 안되는 경우가 있다니..


# BFS로 누군가 효율적으로 푼 것 가지고옴
from collections import deque


def bfs(start, visitied, graph):
    queue = deque([start])
    result = 1
    visitied[start] = True
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if visitied[i] == False:
                result += 1
                queue.append(i)
                visitied[i] = True

    return result


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for start, not_visit in wires:
        visitied = [False] * (n + 1)
        visitied[not_visit] = True
        result = bfs(start, visitied, graph)
        if abs(result - (n - result)) < answer:
            answer = abs(result - (n - result))

    return answer


# 내가  푼것, 결과 비효율 및 1번 틀림
def solution(n, w):
    from collections import deque

    def dfs(graph, start):
        visited = [False] * (n + 1)
        stack = [start[0]]
        answer = 0
        while stack:
            node = stack[-1]
            new_stack = False

            if node == start[1]:
                return answer

            for x, y in graph:
                if x == node and visited[y] == False:
                    stack.append(y)
                    visited[y] = True
                    new_stack = True
                    answer += 1
                elif y == node and visited[x] == False:
                    stack.append(x)
                    visited[x] = True
                    new_stack = True
                    answer += 1
            if new_stack == False:
                stack.pop()
        return answer

    queue = deque(w)
    an = []
    for _ in range(n):
        a = queue.popleft()
        result = dfs(queue, a)
        c = n - result
        d = result
        an.append(abs(c - d))
        print(c, d)
        queue.append(a)

    return min(an)


# n = 9
# w = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]

n = 7

w = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]

n = 3

w = [[1, 2], [1, 3]]
print(solution(n, w))
