# 유클리드 호제법을 활용해 최대 공약수 구하기

# 호제법이란 두 수를 서로 나누는 방법이라 한다.

# a,b에 대해서 a 나누기 b의 나머지가 r이라 할때,
# a와 b의 최대공약수 = b와 r의 최대공약수


# b를 r로 나눠 r`을, r을 r`로 나눠 r`` 등 나머지가 0이 될때까지 진행한다.


def gcd(a, b):  # greatest common divisor
    while b > 0:
        a, b = b, a % b  # 큰 수를 작은 수로 나눈다.
    return a
