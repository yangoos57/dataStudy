# programmers brute force

# 가장 많이 정답인 사람 ['']로 보내기
# 동점일 경우 여러개 넣기
def solution(answers):
    # 12345 5, 21232425 8,3311224455 1000
    s_1 = [1, 2, 3, 4, 5] * 2000
    s_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    s_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    score = [0, 0, 0]
    for i in range(len(answers)):
        if s_1[i] == answers[i]:
            score[0] += 1
        if s_2[i] == answers[i]:
            score[1] += 1
        if s_3[i] == answers[i]:
            score[2] += 1

    answer = []
    for i in range(3):
        if score[i] == max(score):
            answer.append(i + 1)

    return answer


answers = [1, 2, 3, 4, 5]
answers = [1, 3, 2, 4, 2]
print(solution(answers))
