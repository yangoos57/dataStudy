# 2468
from copy import deepcopy

N = int(input())

graph = []
for _ in range(N):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)


def dfs(graph, start, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = [start]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            elif visited[nx][ny] == True:
                continue
            elif visited[nx][ny] == False and graph[nx][ny] == 0:
                visited[nx][ny] = True
            else:
                visited[nx][ny] = True
                stack.append([nx, ny])


def new_map(graph, D):
    graph_copy = deepcopy(graph)
    for i in range(N):
        for j in range(N):
            if graph_copy[i][j] <= D:
                graph_copy[i][j] = 0
            else:
                graph_copy[i][j] = 1
    return graph_copy


result = []
# 최대 반복횟수
max_val = max([max(i) for i in graph])
for i in range(1, max_val + 1):
    # 물 수위별로 지도 생성
    map = new_map(graph, i)
    # 방문기록 생성
    visited = [[False] * N for _ in range(N)]
    counts = 0
    # dfs 시작
    for i in range(N):
        for j in range(N):
            # 무조건 시작하는게 아니고 1이어야 시작하므로 아래와 같은 조건을 달아야함.
            if visited[i][j] == False and map[i][j] == 1:
                dfs(map, [i, j], visited)
                counts += 1
    result.append(counts)

# 물에 잠기지 않은 지역 표현
if max(result) == 0:
    print(1)
else:
    print(max(result))
