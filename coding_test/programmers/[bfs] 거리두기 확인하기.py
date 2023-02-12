# https://school.programmers.co.kr/learn/courses/30/lessons/81302

# bfs로 풀었다. level 2라고 제한을 뒀기 때문에 dfs로 풀 수 없었음.
# 값 저장할 때 level을 추가로 넣은점 칭찬함.


from collections import deque


def bfs(x, y, place_list):
    queue = deque()
    queue.append([x, y, 1])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True
    while queue:
        x, y, z = queue.popleft()
        if z > 2:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue
            elif place_list[nx][ny] == "P" and visited[nx][ny] == False:
                return False
            elif visited[nx][ny] == True:
                continue
            elif place_list[nx][ny] == "X":
                visited[nx][ny] = True
            else:
                queue.append([nx, ny, z + 1])
                visited[nx][ny] = True
    return True


def solution(places):
    answer = []
    for j in places:
        result = True
        place_list = [list(i) for i in j]
        for i in range(5):
            for j in range(5):
                if place_list[i][j] == "P":
                    if bfs(i, j, place_list) == False:
                        result = False

        if result == False:
            answer.append(0)
        else:
            answer.append(1)

    return answer


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
]
solution(places)
