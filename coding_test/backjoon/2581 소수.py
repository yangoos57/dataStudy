# 값
from utils import set_logging


if __name__ == "__main__":
    logger = set_logging()

    # M, N = map(int, input().split(" "))
M, N = [int(input()) for _ in range(2)]

num = 10001


sqrt_n = num ** (0.5)

# 아리스토테네스체 구현
sieve = [True] * (num)
for i in range(2, int(sqrt_n) + 1):
    if sieve[i] == True:
        for j in range(i + i, num, i):
            sieve[j] = False

# 요구조건 충족시키기
sum_prime = 0
first_prime = 0
for i in range(M, N + 1):
    # i가 1인경우가 있다.
    if sieve[i] == True and i > 1:
        if first_prime == 0:
            first_prime += i
        sum_prime += i

# 결과 생성
if first_prime == 0:
    print(-1)
else:
    print(sum_prime)
    print(first_prime)
