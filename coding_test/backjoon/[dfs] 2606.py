# 2606

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.


from collections import defaultdict


a = int(input())
b = int(input())

graph = defaultdict(list)

for _ in range(b):
    x, y = map(int, input().split(" "))
    graph[x].append(y)
    graph[y].append(x)


def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited


print(len(dfs(graph, 1)) - 1)
