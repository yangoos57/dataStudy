# programmers brute force 6

# 2 < n < 100


def solution(n, wires):
    nodes = {i: [] for i in range(1, n + 1)}
    for w, i in wires:
        nodes[i].append(w)
    print(nodes)
    answer = []
    for i in range(1, n + 1):
        if nodes[i] == False:
            answer.append(1)
        else:
            c = len(nodes[i])
            for j in nodes[i]:
                c += len(nodes[j])

            answer.append(c + 1)

    return answer


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
print(solution(n, wires))
