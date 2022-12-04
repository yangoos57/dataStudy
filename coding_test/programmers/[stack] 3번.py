### programmers stack 3

# index로 한 번에 list 2개 불러오기
# 예외 문제 극단적인 것 만든다음 넣어서 오류 잡기


def solution(a, b):
    answer = []
    while a:
        for i in range(len(a)):
            a[i] += b[i]

        c = 0
        while a and a[0] >= 100:
            a.pop(0)
            b.pop(0)
            c += 1

        if c > 0:
            answer.append(c)

    return answer


a = [1, 1, 50]
b = [100, 2, 1]

print(solution(a, b))
