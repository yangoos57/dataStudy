# Programmers DFS/BFS 4

# 행 1 ~ 4
# 전체범위가 1~50 사이


def solution(rectangle, characterX, characterY, itemX, itemY):
    a = rectangle[0]
    a_dot = [
        (a[0], a[1]),  # 왼아
        (a[2], a[1]),  # 우아
        (a[2], a[3]),  # 왼위
        (a[2], a[3]),  # 우상
    ]
    b = rectangle[0]
    b_dot = [
        (b[0], b[1]),  # 왼아
        (b[2], b[1]),  # 우아
        (b[2], b[3]),  # 왼위
        (b[2], b[3]),  # 우상
    ]
    win = a_dot

    for i in a_dot:
        for j in b_dot:
            if i[0] > j[0] and i[1] > j[1]:
                win.append(i)
            elif i[0] < j[0] and i[1] < j[1]:
                win.append(j)
            else:
                win.append(i)

    print(win)


rectangle = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]

characterX = 1

characterY = 3

itemX = 7

itemY = 8

print(solution(rectangle, characterX, characterY, itemX, itemY))
