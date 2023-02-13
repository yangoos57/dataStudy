# 값

M, N = map(int, input().split(" "))
board = [input().strip() for _ in range(N)]


# Red, Blue 위치 파악
B = 0
R = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == "R":
            R = (i, j)
        elif board[i][j] == "B":
            B = (i, j)

# blue,red에 대한 방문 리스트
visited_red = [[0] * M for _ in range(N)]
visited_blue = [[0] * M for _ in range(N)]

# 상하좌우에 따른 위치 변동 함수
def moving(i, j, visited):
    # 상
    for m in range(i + 1, 0, -1):
        if board[m][j] == "." and visited[m][j] == 0:
            visited[m][j] = visited[i][j] + 1
        elif board[m][j] == "0":
            visited[m][j] = visited[i][j] + 1
            print(visited[i][j] + 1)
            break
        else:
            break
    # 하
    for m in range(i, N - 1):
        if board[m][j] == "." and visited[m][j] == 0:
            visited[m][j] = visited[i][j] + 1
        elif board[m][j] == "0":
            visited[m][j] = visited[i][j] + 1
            print(visited[i][j] + 1)
            break
        else:
            break
    # 좌
    # 우


# deque으로 bfs 구현해야할듯
