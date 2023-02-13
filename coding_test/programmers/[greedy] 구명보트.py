def solution(people, limit):
    # 무게가 무거운 사람부터 시작
    people.sort()
    boat_num = 0
    while people:
        boat = 0
        x = people.pop()
        boat += x
        temp = []
        for _ in range(len(people)):
            y = people.pop()
            if limit >= boat + y:
                boat += y
            else:
                temp.append(y)

        boat_num += 1
        people = sorted(temp)

    return boat_num


solution([70, 50, 80, 50], 100)
