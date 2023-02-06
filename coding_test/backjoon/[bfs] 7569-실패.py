# 7569 토마토
# https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-7569%EB%B2%88-%ED%86%A0%EB%A7%88%ED%86%A0
import sys

a, b, c = map(int, input().split(" "))  # 전체 사람 수

graph = []
for _ in range(c):
    graph_low = []
    for _ in range(b):
        graph_low.append(list(map(int, sys.stdin.readline().split())))

    graph.append(graph_low)

visited = [[[False] * a for _ in range(b)] for _ in range(c)]

level = [[[0] * a for _ in range(b)] for _ in range(c)]


def bfs(graph, start, visited):
    from collections import deque

    queue = deque([])
    queue.append(start)
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 범위
            if nx < 0 or nx >= a or ny < 0 or ny >= b or nz < 0 or nz >= c:
                continue
            # 방문
            elif visited[nz][ny][nx] == True:
                continue
            # 없거나 이미 익은 경우
            elif visited[nz][ny][nx] == False and graph[nz][ny][nx] != 0:
                visited[nz][ny][nx] = True
            #
            else:
                graph[nz][ny][nx] = graph[z][y][x] + 1

                visited[nz][ny][nx] = True
                queue.append([nz, ny, nx])

    return


for i in range(c):
    for j in range(b):
        for k in range(a):
            if graph[i][j][k] == 1 and visited[i][j][k] == False:
                bfs(graph, [k, j, i], visited)

print(graph)
answer = 0
for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(b))

print(answer - 1)
