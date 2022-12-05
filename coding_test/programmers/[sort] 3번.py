### programmers sort 2

# n 1 ~ 1000
# h 0 ~ 10000

# 문제 설명 자체가 잘못됐다고 생각하는데, 나중에 풀어도 같은 의문이 드는지 고민해보자
# h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면
# h의 최댓값이 이 과학자의 H-Index입니다.
# 테스트 케이스로 [10,100]을 찾았다.
# 이 글에서 설명한 케이스를 대입하면
# 10번 이상 인용된 논문이 10편 이상이어야 한다.
# 전체 케이스는 2개 밖에 없으니 10번 이상 인용된 경우는 2회 뿐이다. 따라서 답은 0이 되어야함.
# 그런데 정답은 2다.

# wiki를 보니 이해가 됐다.
# 저자 논문 인용이 [9,7,5,2,1] 이라고할 때
# 문서 개수가 총 5개이니 인용 5회 이상인 경우부터 체크
# 인용이 5 이상인 논문 5개면 5
# 인용 4 이상 논문이 4개면 4
# 인용 3 이상 논문이 3개면 3
# ...
# 차례로 풀면
# 인용 5 이상은 [9,7,5]이므로 논문 개수는 3개, 요구는 5개라 false
# 인용 4 이상은 [9,7,5]이므로 논문 개수는 3개, 요구는 4개라 false
# 인용 3 이상은 [9,7,5]이므로 논문 개수는 3개, 요구는 3개라 True
# 가 된다.

# 새롭게 이해한 방식을 구현하면


def solution(c):
    c.sort(reverse=True)
    for i in range(len(c) + 1, 0, -1):  # 인용 개수 감소
        count = 0
        for j in c:  # 논문 개수 검증
            if j >= i:
                count += 1
            if count == i:  # c와 i 가 같은 순간 종료
                return i

    return 0


### 가장 이상적인 정답

# def solution(citations):
#     answer = 0

#     # citations 배열 내림차순 정렬
#     citations.sort(reverse=True)
#     l = len(citations)

#     for i in range(l):
#         if citations[i] >= i + 1:
#             answer = i + 1

#     return answer


# 문제 이해 못했을 때..
# def solution(c):
#     c.sort(reverse=True)  # [6,5,3,1,0]
#     h_list = []

#     # for _ in range(len(c)):
#     while c:
#         paper = c[-1]  # 5

#         count = 0
#         for p in c:  # 6 5
#             if p >= paper:
#                 count += 1

#         if count >= paper:  # 2 > 5 x
#             h_list.append(paper)
#         c.pop()

#         print(h_list)
#     return h_list[-1]


c = [3, 0, 6, 1, 5]
# c = [10, 100]
c = [9, 7, 6, 2, 1]
c = [0]
print(solution(c))
