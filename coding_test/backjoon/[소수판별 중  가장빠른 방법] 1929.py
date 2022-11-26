# 0~N 범위에 있는 소수를 찾는 방법 중 가장 빠른 방법은 "에라토스테네스의 체"라는 방법임
# https://this-programmer.tistory.com/409
# 설명이 잘되어 있으니 기억나지 않으면 참고하자.
# 에라토스네스 체 말고 추가로 배운점
# 1. range를 활용해 배수 표현하기 range(i,N,i)
# 2. index용으로 리스트를 만들면 좋은점을 배웠음
# idx list를 on/off 기능으로 쓰면 특정 값만을 추출 할 수 있음


N = 100
sieve = [True] * N

sqrt = int((N**0.5))
for i in range(2, sqrt + 1):
    if sieve[i] == True:
        for j in range(i + i, N, i):
            sieve[j] = False


prime_list = [s for s in range(2, N) if sieve[s] == True]


# 내가 푼 방식
# 개별 수를 일일이 소수를 찾는 방식이므로 매우 느림
import math
import sys

input_data = sys.stdin.readline().rstrip().split()

s = int(input_data[0])
e = int(input_data[1])


is_prime = True
for n in range(s, e + 1):
    if n > 1:
        if n % 2 == 0:
            is_prime = False
            break
        else:
            for i in range(1, int(math.sqrt(n) + 1), 2):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime == True:
                print(n)

    is_prime = True
