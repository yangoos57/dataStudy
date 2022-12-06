# programmers DFS BFS 1


#  2 <= len(num) <= 20
#  1<= num[n] <= 50
#  target < 1000


def solution(numbers, target):
    from itertools import product

    lst = [True, False]
    answer = 0
    for i in product(lst, repeat=len(numbers)):
        new_numbers = numbers.copy()
        for j, k in enumerate(i):
            if k == True:
                new_numbers[j] = -new_numbers[j]
        if target == sum(new_numbers):
            # print(i)
            answer += 1

    return answer


numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))
