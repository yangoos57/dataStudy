# 16234

## 주의할점
# visited = [[0,0],[0,0]]
# visited[0][0] = 1
# print('visited',visited)

# visited [[1, 0], [0, 0]]


# visited2 = [[0]* 2 for _ in range(2)]
# visited2[0][0] = 1
# print('visited2',visited2)

# visited2 [[1, 0], [0, 0]]

#### visited 3같이 하면 이상하게 idx가 변하니까 신경쓰기
# visited3 = [[0]*2]*2
# visited3[0][0] = 1
# print('visited3',visited3)

# visited3 [[1, 0], [1, 0]]


N, L, R = map(int, input().split())
graph = []
for n in range(N):
    graph.append(list(map(int, input().split())))


visited = [[0] * N for _ in range(N)]
c = []


def dfs(i, j, c):
    if i < 0 or i >= N or j < 0 or j >= N:
        return False
    elif L <= graph[i][j] <= R and visited[i][j] == 0:
        visited[i][j] = 1
        c.append(graph[i][j])
        dfs(i + 1, j, c)  # 동
        dfs(i - 1, j, c)  # 서
        dfs(i, j - 1, c)  # 남
        dfs(i, j + 1, c)  # 북
        return True
    else:
        return False


answer = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j, c) == True:
            if len(c) > 1:
                v = int(sum(c) / len(c))
                print(v)
                for i in range(N):
                    for j in range(N):
                        if visited[i][j] == True:
                            visited[i][j] = v
                c.clear()
                answer += 1
            else:
                c.clear()
print(answer)
