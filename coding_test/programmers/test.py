### Programmers DFS/BFS 3

# n 1 ~ 200
# computers[i][j] == 1 연결


def solution(n, computers):
    visited = [False] * n

    def dfs(i):
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == False:
                visited[j] = True
                dfs(j)

        return False

    answer = 0
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1

    return answer


n = 3
# c = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
c = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# n = 4
# c = [[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
print(solution(n, c))
