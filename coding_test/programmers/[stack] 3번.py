### programmers stack 3

# index로 한 번에 list 2개 불러오기
# 예외 문제 극단적인 것 만든다음 넣어서 오류 잡기


def solution(a, b):
    answer = []
    while a:
        # 일단위 변화사항 체크
        for i in range(len(a)):
            a[i] += b[i]

        # 성공이 100% 이상인 경우 모두 뽑아내기
        c = 0
        while a and a[0] >= 100:
            a.pop(0)
            b.pop(0)
            c += 1

        # 1개라도 있다면 answer에 append 하기
        if c > 0:
            answer.append(c)

    return answer


a = [1, 1, 50]
b = [100, 2, 1]

print(solution(a, b))

# ---

### 23.1.31. 다시 품
# QA의 중요성을 다시 한 번 꺠닫는다.
# while 문 안에 else 항목의 x = y 를 y = x로 썼다가 원인 찾느라 고생했음
# 코드를 에러없이 쓰게하기 위해선 개별 단위를 점검 할 수 있는 방법에 대해서 고민해야할듯
# if else 문을 쓰면 값들이 나눠져서 흐르느끼 둘 다 점검 해야하는 것을 잊지 말자


def solution(p, s):
    from math import ceil

    # 개별 값의 완성 날짜를 계산
    finish = []
    for i in range(len(p)):
        rest = 100 - p[i]
        days = ceil(rest / s[i])
        finish.append(days)

    # stack을 쓰기 위해 reversed
    finish = list(reversed(finish))
    print(finish)

    # 기준 되는 값 생성
    x = finish.pop()  # 7

    deploy = []
    v = 1
    while finish:
        y = finish.pop()
        if x >= y:  # 3
            v += 1
        else:
            deploy.append(v)
            # 기준 변경하고 새로 생성
            x = y
            v = 1

    # 마지막 배포도 저장
    deploy.append(v)

    return deploy
