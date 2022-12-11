### Programmers hash 2

# 배운점
# Set으로 풀면 됐는디 굳이 Counter로 풀었음.
# min으로 풀면 됐음.


def solution(nums):
    from collections import Counter

    a = len(Counter(nums).keys())
    b = len(nums) // 2
    if a <= b:
        return a
    else:
        return b


nums = [3, 3, 3, 2, 2, 2]
print(solution(nums))
