def solution(number, k):
    answer_len = len(number) - k

    left = ""
    # while k > 0 :
    max_val = 0
    for i in range(0, k):
        max_val = max(max_val, int(number[i : i + answer_len]))
        print(max_val)


number = "1231234"
k = 3
print(solution(number, k))
