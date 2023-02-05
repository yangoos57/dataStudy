# 2644
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
            if nx < 0 or nx >= c or ny < 0 or ny >= b or nz < 0 or nz >= a:
                continue
            # 방문
            elif visited[nx][ny][nz] == True:
                continue
            # 없거나 이미 익은 경우
            elif visited[nx][ny][nz] == False and graph[nx][ny][nz] != 0:
                visited[nx][ny][nz] = True
            #
            else:
                if visited[nx][ny][nz] == False and graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1

                visited[nx][ny][nz] = True
                queue.append([nx, ny, nz])

    return


result = 0  # 며칠 걸리는지
for i in range(c):
    for j in range(b):
        for z in range(a):
            if graph[i][j][z] == 0:  # 토마토가 모두 익지 못한 상황 발견시
                print(-1)
                exit(0)  # 바로 종료
            else:
                result = max(result, gra[i][j][z])  # 며칠 걸리는지 업데이트

print(result - 1)
