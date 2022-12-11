### programmers sort 2

# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.

# 오답정리
# https://esoongan.tistory.com/103 참고
# [3, 30, 34, 5, 9]	=> "9534330"
# 핵심은 3, 30, 34의 배열인데
# [3, 30, 34] => 34330으로 만드는 방법을 고민해야했다.
# 3이 30보다 커야했다.

# 인터넷에서 검색하는 모든 풀이는 3을 곱해서 해결했다.
# '3' * 3 = '333','30' * 3= '303030'
# 이라 100의자리까지 비교할 수 있다. *3을 한 이유는 원소가 1000이하이기 떄문
# sort(key=lambda x: x*3)으로 정렬 기준을 정해주면 쉽게 해결가능

# [0,0,0,0] 반례의 경우 0이 되어야 하므로 마지막에 Int-> str을 넣는다.

### 배울점
# 1. 문자형 정수의 정렬 방식
# 2. [3, 30, 34] 유형을 보듯
# 33보다 작은 32,31,30이 올경우 3보다 뒤로가는 것이 가장 큰 값이 된다.
# 3. sort(key=lambda) : 정렬 기준을 알려준다. 다양한 방법으로 사용 가능!

# https://somjang.tistory.com/entry/Python-%EB%82%B4%EA%B0%80-%EC%9B%90%ED%95%98%EB%8A%94-%EC%88%9C%EC%84%9C%EB%8C%80%EB%A1%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%A5%BC-%EC%A0%95%EB%A0%AC%ED%95%98%EB%8A%94-%EB%8B%A4%EC%96%91%ED%95%9C-%EB%B0%A9%EB%B2%95


#
def solution(numbers):

    str_lst = list(map(str, numbers))
    str_lst.sort(key=lambda x: x * 3, reverse=True)
    answer = "".join(str_lst)
    print(str(int(answer)))


# Permutation 말도안됐지만 이렇게 풀어봤다...


def solution(numbers):
    from itertools import permutations

    str_lst = list(map(str, numbers))
    str_lst.sort()

    list_last = []
    for i in range(9, 0, -1):
        list_i = []
        for val in str_lst:
            if val[0] == str(i):
                list_i.append(val)

        if bool(list_i) == True:
            c = []
            for i in permutations(list_i, len(list_i)):
                b = ""
                for j in range(len(list_i)):
                    b += i[j]
                c.append(b)

            d = str(max(list(map(int, c))))
            print(d)
            list_last.append(d)

    answer = ""

    for i in list_last:
        answer += i

    return answer


numbers = [391, 39, 41, 79, 97, 5, 9, 971, 8]
# numbers = [3, 30, 34, 5, 9]

print(solution(numbers))
