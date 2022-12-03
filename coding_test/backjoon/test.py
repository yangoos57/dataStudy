# 탐색 문제는 방문한 경우를 기록해야함.

from collections import deque

visit_list = [0] * 100001
count_list = [0] * 100001

s, e = list(map(int, input().split()))

queue = deque()

queue.append(s)

while True:
    if visit_list[e] > 0:
        print(count_list[e])
        break

    x = queue.popleft()

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
