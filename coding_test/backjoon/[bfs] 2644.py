# 2644

# bfs의 level을 확인하고 싶으면 전통적인 방식에 level만 생성해서 관리하면 된다.
# 생각하기 쉽게 하려면 level을 n+1개로 한다.

n = int(input())  # 전체 사람 수
a, b = map(int, input().split(" "))  # 관계를 구해야하는 번호
m = int(input())
from collections import defaultdict, deque

graph = defaultdict(list)
for _ in range(m):
    i, j = map(int, input().split(" "))  # 관계를 구해야하는 번호
    graph[i].append(j)
    graph[j].append(i)

# visited 만들기


def bfs(graph, root):
    visited = []
    level = [0] * (n + 1)
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
            for i in graph[node]:
                if i not in visited:
                    level[i] = level[node] + 1
    return level


result = bfs(graph, a)[b]
if result != 0:
    print(result)
else:
    print(-1)
