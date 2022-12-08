# 16234

import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = []
for n in range(N):
    arr.append(list(map(int, input().split())))


# N, L, R = 3, 5, 10
# arr = [[10, 15, 20], [20, 30, 25], [40, 22, 10]]

# N, L, R = 2, 20, 50
# arr = [[50, 30], [30, 40]]


def bfs(i, j):

    from collections import deque

    queue = deque()
    queue.append((i, j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    an = []
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            elif L <= abs(arr[x][y] - arr[nx][ny]) <= R and visited[nx][ny] == False:
                visited[nx][ny] = True
                an.append(arr[nx][ny])
                queue.append((nx, ny))

        if len(an) > 1:
            val = sum(an) // len(an)
        else:
            return 0

        for i in range(N):
            for j in range(N):
                if visited[i][j] == True:
                    arr[i][j] = val

    return 1


c = 0
l = []
day_count = 0
while True:
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                l.append(bfs(i, j))

    if sum(l) == 0:
        break
    else:
        day_count += 1
        l.clear()

print(day_count)
# an = [0]
# c = 0
# while an:
#     for i in range(N) :
#         for j in range(N) :
#             an = bfs(i, j)
#             c += 1
# print(c)
