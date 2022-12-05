# programmers brute force

# 소수를 전부 구한다.
# 값의 가능한 경우의 수를 모두 나열한다?
# 1,7 => 17,71,1,7
# 1,2,3 => 1,2,3,
#          21,13, 12,23, 32,31,
#          321,213, 312,123, 123,231, 132,321, 231,312
# 그 다음 int를 떄린다음 set으로 중복제거한다.
# 여기서 소수 개수를 찾음.


# 배운점
# permutation이 Itertools 안에 있는 이유를 알았다.
# for문에 permutation을 쓰면 경우의 수를 구할 수 있음
# 모든 경우의 수를 구하고 싶으면 1 ~ 최대 개수까지 for문을 다시 돌려야함.


def solution(numbers):
    # 에라토스테네스 체 구현
    sieve = [True] * 1000001
    for i in range(2, 1001):
        if sieve[i] == True:
            for j in range(i + i, 1000001, i):
                sieve[j] = False
    l = [l for l in numbers]

    # 가능한 경우의 수 구현
    from itertools import permutations

    answer = []
    for i in range(1, len(l) + 1):
        for i in permutations(l, i):
            answer.append(int("".join(i)))

    answer = list(set(answer))
    print(len(answer), answer)
    answer = [i for i in answer if 1000001 > i and i > 1 and sieve[i]]

    return len(answer)


numbers = "1234567"
print(solution(numbers))
