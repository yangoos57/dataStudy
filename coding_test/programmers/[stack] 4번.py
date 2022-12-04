### programmers stack 4

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면
# J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.


def solution(priorities, location):
    from collections import deque

    queue = deque(priorities)

    idx_list = [0] * len(priorities)
    idx_list[location] = 1
    queue_idx = deque(idx_list)

    c = 0
    while True:
        max_val = max(queue)

        f = queue.popleft()
        i = queue_idx.popleft()

        if max_val == f:
            c += 1
            if i == 1:
                break
        else:
            queue.append(f)
            queue_idx.append(i)

    return c


p = [1, 1, 9, 1, 1, 1]
l = 0

print(solution(p, l))
