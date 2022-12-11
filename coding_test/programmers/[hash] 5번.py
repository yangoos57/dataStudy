### Programmers hash 5

# 배울점
# sort 할 때 고려 대상이 2개 이상일때 (ex[2,100],[3,200],[4,50])
# 두번째를 우선으로 정배열 한 다음 첫번째는 역배열 하는 경우 key setting은
# lambda x : -x[1],x[0] 으로 설정해야함. 역배열은 -를 붙인다.

# value를 기준으로 key를 정리하고 싶으면 dict.items()를 활용해 sort를 쓴다.


def solution(genres, plays):
    from collections import defaultdict

    dic_gen = defaultdict(int)
    dic_all = defaultdict(list)

    for i in range(len(genres)):
        dic_gen[genres[i]] += plays[i]
        dic_all[genres[i]].append([i, plays[i]])

    print(dic_all)
    for j in dic_all.keys():
        dic_all[j].sort(key=lambda x: (x[1], -x[0]))

    print(dic_all)
    gen_name = sorted(dic_gen.items(), reverse=True, key=lambda x: x[1])
    answer = []

    for name, _ in gen_name:
        for _ in range(2):
            try:
                answer.append(dic_all[name].pop()[0])
            except:
                pass

    return answer


g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 500, 2500]
# g = ["classic", "pop", "classic", "classic"]
# p = [500, 600, 150, 800]
print(solution(g, p))
