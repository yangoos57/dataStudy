# programmers brute force 7
# 가능한 조합 수 ,중복 불가, 순서 상관없이 = combinations
# 가능한 조합 수, 중복 불가, 순서 상관있이 = Permutations
# 모든 경우의 수, 중복 가능  = product


def solution(word):
    from itertools import product

    char = ["A", "E", "I", "O", "U"]

    product_list = []
    for i in range(1, 6):
        for j in product(char, repeat=i):
            product_list.append("".join(j))

    product_list.sort()

    product_list = ["0"] + product_list

    for i, v in enumerate(product_list):
        if word == v:
            answer = i

    return answer


word = "EIO"
print(solution(word))
