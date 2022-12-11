### programmers stack 5

### stack

# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.

#


def solution(b, w, truck):
    from collections import deque

    bridge = deque([0] * b)
    truck = deque(truck)
    time = 0
    b_w = 0
    while truck:
        t = truck.popleft()
        # 시간이 지나면서 무조건 해야하는 절차
        # 시간추가, 맨 왼편 bridge pop
        time += 1
        f = bridge.popleft()

        # finish가 트럭인 경우 weight 빼기
        if f > 0:
            b_w -= f
        # 조건에 충족한 경우 truck 넣기
        if b_w + t <= w:
            bridge.append(t)
            b_w += t
        # 조건에 충족하지 못한 경우 truck 기다리게 하고 시간 보내기
        else:
            bridge.append(0)
            truck.appendleft(t)
        print(time, bridge, w)

    return time + b


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
# bridge_length = 100
# weight = 100
# truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


print(solution(bridge_length, weight, truck_weights))
