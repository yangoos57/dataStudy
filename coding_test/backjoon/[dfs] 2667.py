# 2667

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

n = int(input())
graph = []
for i in range(n):
    a = list(map(int, list(input())))
    graph.append(a)

# visited 만들기


visited = [[False] * n for _ in range(n)]


def dfs(graph, root, visited):

    stack = [root]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    while stack:
        x, y = stack.pop()
        # 현재 위치를 포함해야하므로 현재 단계에서 방문처리와 count를 수행
        if visited[x][y] == False and graph[x][y] == 1:
            # visited
            visited[x][y] = True
            count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #  범위를 넘어서는 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 이미 방문한 경우
            elif visited[nx][ny] == True:
                continue
            # 방문할 수 없는 경우
            elif visited[nx][ny] == False and graph[nx][ny] == 0:
                visited[nx][ny] = True
            else:
                stack.append([nx, ny])
    return count


a = 0
answer = []
for x in range(n):
    for y in range(n):
        # 실행조건 2개 방문 안했고, 시작점이 1인 경우
        if visited[x][y] == False and graph[x][y] == 1:
            k = dfs(graph, [x, y], visited)
            answer.append(k)
            a += 1

for i in [a] + sorted(answer):
    print(i)
