# n^2 배열 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/87390

# n*n 행렬의 위치는 몫과 나머지로 표현 가능하다.

# 내가 푼 방법
def solution(n, left, right):
    y = []
    # 몫과 나머지 => 행열 위치
    a = (left // n, left % n)
    b = (right // n, right % n)

    # 모든 값을 구하지 않고 정해진 값만 구하기
    for i in range(a[0] + 1, b[0] + 2):
        y += [i] * i + list(range(i + 1, n + 1))

    return y[a[1] : a[1] + (right - left + 1)]


# 다른 사람이 푼 방법
# 이게 진짜 의도한바로 푼 것임.
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
    return answer


n = 4
left = 7
right = 14
# n = 3
# left = 2
# right = 5


solution(n, left, right)
