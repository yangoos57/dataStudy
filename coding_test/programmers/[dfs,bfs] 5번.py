# Programmers DFS/BFS 5

# 공항수 3 ~ 10000
# 항공권 모두 사용
# 모든 도시 방문 가능
# 가능한 모든 도시 중 알파벳 앞서는 것으로 return

# 배울점
# 모든 도시를 방문하기 때문에 꼭 BFS로 풀지 않아도 됨
# tickets.sort(key = lambda x:(x[1], x[0]))

# dict를 문제풀이에 적용하는 방법을 배움
# dfs 방문처리를 pop()으로 구현할 수 있음.
# while문 안에 dic[s]를 통해 방문하지 않은 하위 노드를 확인할 수 있음
# dic[s] empty면 그 전으로 올라가야하니 stack.pop을 해 s가 전 노드를 지칭하게 한다.

# DFS 원리 다시 생각해보기
# 하단 노드가 존재하면 하단 노드로 계속 이동
# 하단 노드가 존재하지 않으면 상단 노드로 이동
# 상단 노드로 이동하고나서 하단 노드가 존재하면 다시 하단 노드로 이동
# 상단 노드로 이동하고나서 하단 노드가 존재하지 않으면 상단 노드로 이동

# DFS 알고리즘으로 구현시 고려사항
# 알고리즘으로 구현할 때 하단 노드 존재 유무에 따라 상단으로 이동할 수 있는지 고민해야함
# 하나는 pop으로 해결하는 방법
# 상위 노드를 key, 하위 노드들을 list 내 넣는 dict를 만듬
# key 방문 시 하위 노드 중 하나를 pop해서 stack list에 넣음

# 하나는 visit list를 만들어서 해결하는 방법이 있음
# node 번호 방문 시 visited == True로 설정하면 됨


def solution(tickets):
    from collections import defaultdict

    dic = defaultdict(list)
    for s, e in tickets:
        dic[s].append(e)

    for k in dic.keys():
        dic[k].sort(reverse=True)

    stack = ["ICN"]  # stack의 맨 마지막은 현재 노드
    answer = []
    while stack:
        s = stack[-1]  # 현재 노드
        if dic[s]:
            # 방문하지 않은 하위 노드가 존재하는 경우
            stack.append(dic[s].pop())
            # 하위 노드로 이동
        else:
            # 해당 노드에 모든 하위 노드를 방문한 경우
            answer.append(stack.pop())
            # 상위 노드로 이동

    return answer[::-1]


tickets = [
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
]

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

print(solution(tickets))


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
