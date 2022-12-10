# Programmers DFS/BFS 5

# 공항수 3 ~ 10000
# 항공권 모두 사용
# 모든 도시 방문 가능
# 가능한 모든 도시 중 알파벳 앞서는 것으로 return

# 배울점
# 모든 도시를 방문하기 때문에 꼭 BFS로 풀지 않아도 됨
# tickets.sort(key = lambda x:(x[1], x[0]))
# defaultdict 사용이유와 왜 default dict를 사용해서 풀었는지 궁금
#


# 문제 틀림 광기로 풀었음
# 배운점
# 재귀함수의 특징을 어느정도 이해한 것 같음
# depth를 제한걸고, 하나씩 더한 값을 마지막 depth에 푸는 방식에 익숙해짐


def solution(tickets):
    def bfs(start, end, depth, saving):
        if depth == len(tickets) - 1:

            saving.append(start + " " + end)
            return False

        for t in tickets:

            if t[0] == end:
                bfs(start + " " + end, t[1], depth + 1, saving)

        return False

    # 시작 공항 정하기
    starting = []
    for t in tickets:
        if t[0] == "ICN":
            starting.append(t)

    # 가장 빠른순으로 정리
    starting.sort()

    saving = []
    bfs(starting[0][0], starting[0][1], 0, saving)

    lst_3 = []
    for i in saving:
        lst_1 = i.split(" ")
        lst_2 = []
        for j in range(0, len(lst_1) - 1):
            lst_2.append([lst_1[j], lst_1[j + 1]])
        lst_3.append(lst_2)

    tickets.sort()

    answer = []

    for n, i in enumerate(lst_3):
        i.sort()
        if i == tickets:
            answer.append(saving[n])

    return answer[0].split(" ")
    print(saving)


tickets = [
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
]

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

print(solution(tickets))
