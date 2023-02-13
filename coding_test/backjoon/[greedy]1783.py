# 1783
# https://www.acmicpc.net/problem/1783

# 배울점
# 문제 풀기전에 어떻게 풀어야할지 계속 고민하는게 좋은듯
# 하지만 계속해서 조건을 한 두개 생략해서 완전한 정답을 맞추지 못하고 있다.
# 큰 조건 하위조건 구분을 잘하자.

x = list(map(int, input().split(" ")))

coor = list(map(lambda x: x - 1, x))

if coor[0] >= 2 and coor[1] >= 6:
    cnt = (coor[1] - 6) + 5

elif coor[0] >= 2 and coor[1] < 6:
    if coor[1] >= 3:
        cnt = 4
    else:
        cnt = coor[1] + 1

elif coor[0] == 1:
    cnt = min(4, int(coor[1] // 2) + 1)

elif coor[0] == 0:
    cnt = 1

print(cnt)
