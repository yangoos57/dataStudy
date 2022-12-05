# programmers brute force

# 가로, 세로 모두 범위 안에 들어가야함.

# 문제풀이
# 모든 카드의 가로 세로 중 가장 큰 값을 찾는다.
# 그렇게 되면 한 변을 고정시킬 수 있음.
# 개별 카드의 가로 세로 중 큰 값을 고정 된 변과 일치하게 둔다.
# 그렇게 되면 개별 카드의 작은 값이 고정되지 않는 영역으로 감
# 그중 가장 큰 값을 선택하면 문제해결


# for i in range(len(sizes)):
#     if sizes[i][s] < sizes[i][e]:
#         sizes[i][s], sizes[i][e] = sizes[i][e], sizes[i][s]
def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    max_size_1 = max(max(sizes))

    max_size_2 = 0
    for i in sizes:
        max_size_2 = max(max_size_2, i[1])

    return max_size_1 * max_size_2


sizes = [[14, 4], [6, 19], [6, 16], [18, 7], [7, 11]]
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

print(solution(sizes))
