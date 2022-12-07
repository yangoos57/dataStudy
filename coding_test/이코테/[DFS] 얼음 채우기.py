# 이코테 DFS/BFS 음료수 얼려먹기

# 개념
# 채워진 부분 0 채워지지 않은 부분 1
# 두가지 절차를 수행한다.
# 1. 그래프를 탐색해서 채워지지 않은 부분을 찾는다.
# 2. 채워지지 않은 부분을 DFS를 통해 채운다.
# 3. 끝까지 반복한다.

# 재귀가 곧 stack이다.
# Stack은 끝까지 나아간다는 개념이 있음.
# 재귀함수는 함수를 쌓아가면서 끝까지 나아가는 방식임
# 일단 쭉 나아가다가 끝에 도달하면 역순으로 돌아오면서 문제를 해결하는 방식임


def DFS(i, j):
    if i < 0 or i >= a or j < 0 or j >= b:
        return False
    if graph[i][j] == 1:
        return False
    else:
        graph[i][j] = 1
        DFS(i + 1, j)  # 동 # 동쪽 확장을 위해 stack을 쌓는다.
        DFS(i - 1, j)  # 서
        DFS(i, j + 1)  # 남
        DFS(i, j - 1)  # 북
        return True


a, b = 4, 5
graph = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

result = 0
for i in range(a):
    for j in range(b):
        if DFS(i, j) == True:
            result += 1

print(result)
