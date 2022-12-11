### Programmers hash 1


def solution(participant, completion):
    from collections import Counter

    par = Counter(participant)
    com = Counter(completion)
    for name in sorted(par):
        if par[name] != com[name]:

            return name

    # return answer


participant = ["marina", "josipa", "nikola", "vinko", "filipa", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))
