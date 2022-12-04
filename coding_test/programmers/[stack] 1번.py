### programmers stack 1

# 연속된 값을 비교할 떈 이전 값과 비교한다.


def solution(arr):
    num = len(arr)
    l = [arr[0]]
    for i in range(0, num - 1):
        if arr[i] != arr[i + 1]:
            l.append(arr[i + 1])
    return l


arr = [1, 1, 3, 3, 0, 1, 1]
arr = [4, 4, 4, 3, 3]

print(solution(arr))
