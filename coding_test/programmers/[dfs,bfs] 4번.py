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


def solution(begin, target, words):
    from collections import deque

    if target in words:
        # 방문
        visited = [False] * len(words)
        # 단계 표시
        level = [0] * len(words)

        # 단어 변화
        change = deque()
        change.append(begin)

        # words 내 target idx
        idx = words.index(target)

        while change:
            x = change.popleft()

            # begin 아닌 경우
            if x != begin:
                x_idx = words.index(x)
            else:
                x_idx = 1

            for n, word in enumerate(words):
                if visited[n] == False:
                    v = 0
                    # 안좋은 예시 남겨놓기
                    # x_list = list(x)
                    # word_list = list(word)
                    # for _ in range(len(x)):
                    #     if x_list.pop() != word_list.pop():
                    #         v += 1
                    for i in range(len(x)):
                        if x[i] != word[i]:
                            v += 1
                    if v == 1:
                        visited[n] = True
                        level[n] = level[x_idx] + 1
                        change.append(word)

        return level[idx]
    else:
        return 0
