# programmers brute force 4

# y 1 ~ 2,000,000
# b 8 ~ 5,000
# 가로 >= 세로


# 배울점
# y%i == 0 방식은 O(N)이다. O(N^(1/2))로 줄일 수 있으니 외워서 사용하자.
# C = A*B일 때 C를 A로 나누면 몫이 B가 되니까 A를 찾으면 B도 자동으로 찾아진다.
# 대신 C = A*A일 때 A가 중복되기 들어가는것을 막고자  if A^2 !=C 를 추가한다.
# 코드로 구현하면
y = 25
divisor = []
for i in range(1, y ** (1 / 2) + 1):
    if y % i == 0:
        divisor.append(i)
        if i**2 != y:
            divisor.append(y // i)


# solution
# 약수 구하는 방법은?
# deque로 0과 -1 을 불러온다.
# brown = 2(a+b+2)를 만족하면
# a>b일 때 [a,b]


def solution(brown, yellow):
    from collections import deque

    # y 약수
    divisor = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            divisor.append(i)
    queue = deque(divisor)
    while queue:
        if len(queue) == 1:
            a = b = queue.pop()
        else:
            a = queue.popleft()
            b = queue.pop()

        if 2 * (a + b + 2) == brown:
            return [b + 2, a + 2]


b = 16
y = 9
print(solution(b, y))
