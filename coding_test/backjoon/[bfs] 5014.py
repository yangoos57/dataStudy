# 5014

F, S, G, U, D = map(int, input().split(" "))

# F 건물 높이
# S 현재 위치
# G 기업 위치
# U 위로 이동
# D 아래로 이동

from collections import deque

visited = [0] * (F + 1)
visited[S] = 1

count_list = [0] * (F + 1)

queue = deque([])
queue.append(S)

while queue:
    X = queue.popleft()

    if 0 < X + U <= F and visited[X + U] == 0:
        visited[X + U] = 1
        count_list[X + U] = count_list[X] + 1
        queue.append(X + U)

    if 0 < X - D <= F and visited[X - D] == 0:
        visited[X - D] = 1
        count_list[X - D] = count_list[X] + 1
        queue.append(X - D)

if S == G:
    print(0)
elif count_list[G] == 0:
    print("use the stairs")
else:
    print(count_list[G])
