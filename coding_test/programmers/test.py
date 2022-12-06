# programmers DFS BFS 1


#  2 <= len(num) <= 20
#  1<= num[n] <= 50
#  target < 1000


from itertools import product


def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    print(*l)
    print(list(product(*l)))
    s = list(map(sum, product(*l)))
    print(s)
    print(s.count(target))
    return s.count(target)


numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))
