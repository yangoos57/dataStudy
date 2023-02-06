# 2573

# 땅 = 0 빙산 = 정수

# 접한 칸의 개수만큼 빙산의 크기가 줄어듬 / max = 0

# 빙산 한 덩어리가 두 덩어리 이상이 되는 시간을 구하시오

# 다 녹을때까지 두 덩어리 이상으로 분리되지 않으면 0

N, M = map(int, input().split(" "))

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split(" "))))


# 매번 돌 때마다 주변에 0이 있는지를 체크해서 높이에 반영


def melting(N, M):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    glacier = []
    for i in range(N):
        temp = []
        for j in range(M):
            if graph[i][j] != 0:
                temp.append(True)
            else:
                temp.append(False)
        glacier.append(temp)

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and glacier[i][j] == False:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if ni < 0 or ni >= N or nj < 0 or nj >= M:
                        continue
                    elif graph[ni][nj] > 0:
                        graph[ni][nj] -= 1


def dfs(i, j, visited):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    stack = [[i, j]]

    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            elif visited[ni][nj] == True:
                continue
            elif visited[ni][nj] == False and graph[ni][nj] == 0:
                visited[ni][nj] = True
            else:
                visited[ni][nj] = True
                stack.append([ni, nj])


def check_melting():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            else:
                return
    return exit(print(0))


year = 0
for _ in range(11):
    year += 1
    # 빙산이 한 번에 사라지는 경우 0 출력
    check_melting()
    melting(N, M)
    warning = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and graph[i][j] != 0:
                dfs(i, j, visited)
                warning += 1
                if warning >= 2:
                    print(year)
                    exit(0)
