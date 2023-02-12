# 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42895

# DP 개념은 아래
# https://velog.io/@euneun/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-N%EC%9C%BC%EB%A1%9C-%ED%91%9C%ED%98%84-DP-%EB%8F%99%EC%A0%81%EA%B3%84%ED%9A%8D%EB%B2%95-C

# 배운점
# 내가 푼 방식은 풀고나서 이해해보니 Greedy 였음.
# Greedy로 풀때 Defaultdict로 푸니까 메모리를 매우 아낄 수 있었음
from collections import deque, defaultdict


def solution(N, number):
    memo = defaultdict(int)
    memo[N] = 1
    queue = deque()
    queue.append([N, 1])

    while queue:
        print(memo)
        V, S = queue.popleft()

        if S > 8:
            return -1

        if memo[V * N] == 0:
            memo[V * N] = S + 1
            queue.append([V * N, S + 1])

        if memo[V - N] == 0:
            memo[V - N] = S + 1
            queue.append([V - N, S + 1])

        if memo[V + N] == 0:
            memo[V + N] = S + 1
            queue.append([V + N, S + 1])

        if memo[int(V / N)] == 0:
            memo[int(V / N)] = S + 1
            queue.append([int(V / N), S + 1])

        if memo[int(str(V) + str(N))] == 0:
            memo[int(str(V) + str(N))] = S + 1
            queue.append([int(str(V) + str(N)), S + 1])

        if memo[number] > 0:
            return memo[number]


N = 5
number = 12
N = 2
number = 11
N = 1
number = 1111
# N = 2
# number = 711
print(solution(N, number))
