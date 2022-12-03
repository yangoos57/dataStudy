# 탐색 문제는 방문한 경우를 기록해야함.
#

from collections import deque

visit_list = [0] * 100001
count_list = [0] * 100001

s, e = list(map(int, input().split()))

queue = deque()

queue.append(s)

while True:
    x = queue.popleft()

    # if x == e:
    #     print(count_list[e])
    #     break

    # 아래 구문에서 문제 발생
    # 얼핏 x==e와 같아보이지만, 아래 조건은 무조건 해당 수를 지나야 종료된다.
    # 따라서 5 5인 경우 2를 반환함.
    # if visit_list[e] > 0:
    #     print(count_list[e])
    #     break

    if 0 <= x + 1 <= 100000 and visit_list[x + 1] == 0:
        visit_list[x + 1] = 1
        count_list[x + 1] = count_list[x] + 1
        queue.append(x + 1)

    if 0 <= x - 1 <= 100000 and visit_list[x - 1] == 0:
        visit_list[x - 1] = 1
        count_list[x - 1] = count_list[x] + 1
        queue.append(x - 1)

    if 0 <= 2 * x <= 100000 and visit_list[2 * x] == 0:
        visit_list[2 * x] = 1
        count_list[2 * x] = count_list[x] + 1
        queue.append(2 * x)


# +1 or -1 가능
# 2x로 이동 가능

# 역순으로 문제 풀어보자
from collections import deque

s, e = list(map(int, input().split()))

graph = [0] * (e + 2)
queue = deque()

queue.append(e)


while queue:

    if graph[s] > 0:
        break

    x = queue.popleft()

    if x % 2 == 0:
        nx = x // 2
    else:
        nx = 0

    if x <= e:
        nx_1, nx_2 = x + 1, x - 1

        if graph[nx] == 0:
            graph[nx] = graph[x] + 1
            queue.append(nx)

        if graph[nx_1] == 0:
            graph[nx_1] = graph[x] + 1
            queue.append(nx_1)

        if graph[nx_2] == 0:
            graph[nx_2] = graph[x] + 1
            queue.append(nx_2)

if s >= e:
    print(s - e)
else:
    print(graph[s])
