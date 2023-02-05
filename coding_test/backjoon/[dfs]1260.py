# 16234

from collections import defaultdict, deque


n, m, v = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    graph[i] = list(set(graph[i]))
    graph[i].sort()


def dfs(graph, root):
    visited = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))

    return visited


print(*dfs(graph, v))


def bfs(graph, root):
    visited = []
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited


print(*bfs(graph, v))
