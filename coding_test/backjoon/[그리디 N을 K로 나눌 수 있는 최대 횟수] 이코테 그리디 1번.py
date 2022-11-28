### 이코테 그리디 1번 문제
# https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2

## 베울점
# 문제 자체가 정말 유용한 알고리즘이다.

# N을 k로 최대한 나눌 수 있는 횟수는?
# N이 k로 나눠지지 않으면 N-1로 나눈다.

# 25를 3으로 최대 나누는 횟수는 ?
# 25 - 1 = 24
# 24 / 3 = 8 --- 1회
# 8 - 1 = 7
# 7 - 1 = 6
# 6 / 3 = 2  --- 2회
# 2 < 3이므로 break

# 소스코드로 구현

# 25를 3으로 나누는 횟수를 소스코드로 표현하면?
# (25//3) * 3
# (8//3) * 3

# 그렇다면 -1을 하는 횟수를 소스코드로 표현하면?
# 25 - (25//3) * 3
# 8 - (8//3) * 3


n = 25
k = 3

result = 0
mul = 0
while True:
    # n과 가장 가까운 값 중 k로 나눠지는 값
    mul = (n // k) * k

    # k의 배수로 만들기 위해 1을 몇 번 빼야하는지 계산
    result += n - mul

    # k로 나눌 수 없으면 break
    if n < k:
        break

    # k로 나눈 몫이 n
    n = n // k

# 1로 민들기 위해 n-1번 추가로 계산해야함.
result += n - 1

print(result)
