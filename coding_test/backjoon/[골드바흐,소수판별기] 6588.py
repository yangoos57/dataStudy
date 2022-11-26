# 에라토스테네스의 체를 써서 푸는 문제
# 인터넷에는 천재들만 있나 왜 이런식으로 코드를 구성하는지 쓰는 놈은 한 명도 없네
# 외울 수 있을 정도로 이해는 했으니 외워서 나중에 써먹자

# 1929 문제는 소수가 필요해서 개별적으로 값을 구했다면
# 6588 문제는 소수인지 아닌지 여부만 필요함.

# 6588 문제의 핵심은 짝수 - 소수 = 소수 인지를 확인하는 것
# 따라서 체를 소수 판별기로 사용할 수 있음
# n = 42 일 때 array[3], array[42-3] 이므로 소수판별기에서 True, False가 나옴
# array[5], array[37] 이므로 True True 정답이 된다.

# 배울점
# 에라토스테네스의 체를 소수 판별기로 사용할 수 있다는 점
# 골드바흐 추측 문제는 소수 + 소수를 더해서 짝수가 될 수 있는지를 찾는게 아니라
# 짝수 - 소수 = 소수 인지 여부를 확인하는 것임


from sys import stdin

array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    n = int(stdin.readline())

    if n == 0:
        break

    for i in range(3, len(array)):
        if array[i] and array[n - i]:
            print(n, "=", i, "+", n - i)
            break


### 내가 푼 것

# 체를 통해 가능한 수를 고름
# 가능한 수를 가지고 하나씩 대입해봄
# 이때 b-a가 가장 큰 값이어야함


# 체 만들기
import sys

# for n in input_list:
n = 100000
sieve = [True] * n
for i in range(2, int((n**0.5) + 1)):
    if sieve[i] == True:
        for j in range(i + i, n, i):
            sieve[j] = False

# 소수를 직접 구했다는게 에러

prime_list = [s for s in range(2, n) if sieve[s] == True]

while True:
    n = int(input())
    if n == 0:
        break

    for k in range(len(prime_list)):
        gc = False
        a = prime_list[k]
        for b in prime_list[k:]:
            if a + b == n:
                gc = True
                break

        if gc == True:
            print(f"{n} = {a} + {b}")
            break

    if gc == False:
        print("Goldbach's conjecture is wrong.")
