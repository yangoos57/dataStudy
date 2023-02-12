from heapq import *


def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        x = heappop(scoville)
        y = heappop(scoville)
        z = x + 2 * y
        heappush(scoville, z)
        answer += 1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = sum(scoville) * 4
solution(scoville, K)
