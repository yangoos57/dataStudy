# Programmers DFS/BFS 3


# 배울점
# x,y를 pop한 뒤 방문처리하니 효율성 테스트를 통과하지 못했다.
# 지금까지 x,y를 pop하는 행위를 해당 위치에 방문한다는 것으로 이해했다.
# 그래서 pop에서 얻은 위치를 가지고 방문처리를 수행했다.
# Queue에 쌓는 행위는 해당 위치를 방문했다는 것이므로 쌓는 코드 다음 바로 True 코드를 해야함.
# Queue에서 pop하여 주변을 찾는 것은 탐색 과정이다.

from collections import deque


def solution(maps):
    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while queue:
            x, y = queue.popleft()
            # visited[x][y] = True <= 예전에 했던 것

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                elif visited[nx][ny] == True:
                    continue
                elif maps[nx][ny] == 0:
                    visited[nx][ny] = True
                else:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]

    bfs(0, 0)

    if maps[n - 1][m - 1] == 1:
        answer = -1

    else:
        answer = maps[n - 1][m - 1]
    return answer


maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
]

print(solution(maps))
