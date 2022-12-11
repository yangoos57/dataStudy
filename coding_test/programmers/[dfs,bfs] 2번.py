# programmers DFS/BFS 2

# 문제풀이
# 최대 네트워크 개수는 N 임(모두 연결 되지 않을 경우)
# 네트워크가 연결되어 있다면

# 배울점
# 얼음 채우기 문제와 스타일이 다른 유형임
# Notion 일일로그에 관련 사진 올려놓음


# BFS
def bfs(i, visited, n, computers):
    from collections import deque

    queue = deque([i])
    while queue:
        x = queue.popleft()
        visited[x] = 1
        # 다른 노드와 연결 여부를 확인
        for a in range(n):
            if computers[x][a] == 1 and visited[a] == False:
                queue.append(a)


def solution(n, computers):
    visited = [0] * n
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            bfs(i, visited, n, computers)
            answer += 1
    return answer


# DFS 방법
def dfs(i, visited, n, computers):
    for a in range(n):
        # 다른 노드와 연결 여부를 확인
        # i = 0이라 할 때 1,2,3과 연결됐는지를 확인하는 절차
        # 만약 0과 1이 연결 됐을 땐, 1 방문처리
        # 1과 2,3 연결 여부를 확인
        # 1과 2는 연결 됐고 1과 3은 연결 되지 않을땐 2 방문처리
        # 다시 2와 3의 연결을 확인 연결되면 3 방문처리 안되면 pass
        if computers[i][a] == 1 and visited[a] == 0:
            visited[i] = 1
            dfs(a, visited, n, computers)


def solution(n, computers):
    visited = [0] * n  # 노드 개수
    answer = 0
    for i in range(n):
        # 개별 노드에 대한 방문 여부 체크
        # 1과 2 노드가 연결 되어있다고 가정할 때
        # 1에서 2를 방문처리 했기 때문에 진행하지 않음.
        if visited[i] == 0:
            dfs(i, visited, n, computers)
            answer += 1
    return answer


n = 4
computers = [[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]

print(solution(n, computers))
