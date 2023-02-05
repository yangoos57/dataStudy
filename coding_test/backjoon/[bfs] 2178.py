# 16234

from collections import deque


y, x = map(int, input().split(" "))
graph = [list(map(int, input())) for _ in range(y)]


def bfs(graph):
    # 1. visited
    visited = [[False] * x for _ in range(y)]
    visited[0][0] = True
    # 2. queue
    queue = deque([])
    queue.append([0, 0])
    # dx,dy
    da = [-1, 1, 0, 0]
    db = [0, 0, -1, 1]
    # 4. while
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            # 사각형 벗어나는 경우
            # na >= y에서 =을 넣는 이유는 그 이상으로 탐색이 불가능하기 떄문임.
            if na < 0 or na >= y or nb < 0 or nb >= x:
                continue
            # 이미 방문한 경우
            elif visited[na][nb] == True:
                continue
            # 방문할 수 없는 경우
            elif graph[na][nb] == 0 and visited[na][nb] == False:
                visited[na][nb] = True
            else:
                # 방문처리
                visited[na][nb] = True
                # queue 넣기
                queue.append([na, nb])
                # level 업데이트하기
                graph[na][nb] = graph[a][b] + 1

    return graph[-1][-1]


print(bfs(graph))
