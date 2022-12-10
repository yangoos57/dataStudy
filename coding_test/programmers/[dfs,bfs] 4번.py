# Programmers DFS/BFS 4

# hit =>... =>cog
# 한 번에 1개 단어, 이때 단어 변환은 words 내 단어로
# 반환 불가하면 0
# 단어길이

### 배울점
# 노드가 몇번째 위치하는지 기록하면 매우 쉬운문제
# But 어떻게 기록하는걸까...?
# 이 문제의 경우 계층 List를 새로 만들었다.
# 미로찾기 문제의 경우 미로에다가 표현하면 됐지만
# 해당 문제는 str을 가지고 푸는 문제라 새로 만들었다.

# 1. Level_list를 만든다. [0]* len(node)
# 2. 불러온 단어의 index 파악을 위해 .index 매서드 사용
# 3. 그렇게하면 Level을 쉽게 불러올 수 있음.

## 다른방법으로는 queue에 쌓을 때 아예 depth(=level)과 묶어서 넣는 방법이 있다.
# queue.append([word,depth])
# 이 방법이 더 깔끔한듯 !
# https://leffept.tistory.com/398

from collections import deque


def solution(begin, target, words):
    def bfs(b, t):
        queue = deque()
        queue.append(b)

        while queue:
            m_w = queue.popleft()

            # 연산 종료
            if m_w == t:
                return level_list[-1]

            # 현재 비교할 m_w(main_word)의 level을 찾는다.
            if m_w != b:
                level = level_list[words.index(m_w)]
            else:
                level = 0

            # 방문하지 않은 다른단어들과 비교한 뒤
            # 일치하는 단어들을 queue에 넣고 현재 Level_list에 Level + 1을 한다.
            for i, w in enumerate(words):
                if visited[i] == True:
                    continue
                else:
                    c = 0
                    for j in range(char_len):
                        if m_w[j] != w[j]:
                            c += 1
                    if c == 1:
                        queue.append(w)
                        visited[i] = True
                        level_list[i] = level + 1

            # print(lst)

        return 0

    char_len = len(begin)
    visited = [False] * len(words)
    level_list = [0] * len(words)
    if target in words:
        # target 단어 찾아서 맨 마지막에 넣기
        words.append(words.pop(words.index(target)))
        answer = bfs(begin, target)
        return answer
    else:
        return 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


print(solution(begin, target, words))
