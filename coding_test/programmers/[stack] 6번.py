### programmers stack 6

# 목적 : 가격이 떨어지지 않은 기간은 몇 초

# 가격 1 ~ 10,000 / 길이 2 ~ 100,000

# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.


def solution(prices):
    from collections import deque

    prices = deque(prices)
    num_prices = len(prices)

    answer = []
    for _ in range(num_prices):
        val = prices.popleft()
        c = 0
        for i in prices:
            if val <= i:
                c += 1
            else:
                c += 1
                break

        answer.append(c)

    return answer


prices = [1, 1, 1, 2, 1]

print(solution(prices))
