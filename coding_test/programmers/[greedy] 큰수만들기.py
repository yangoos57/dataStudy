# 큰 수 만들기(stack)
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

# 배울점
# 문제 자체를 이해하는게 가장 우선인듯하다. 코드로 바로 짜는건 무용지물. 자동화 할 수 있는 패턴을 찾아야함.


# 다른사람이 푼 것
def solution(number, k):
    answer = []  # Stack

    for num in number:
        # answer[-1] < num이 핵심인듯. 마지막보다 크면 작아질때까지 버린다.
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return "".join(answer[: len(answer) - k])


# 흠..
def solution(number, k):
    # 역순으로 계산
    reverse_num = number[::-1]

    # 남는 것
    left = ""

    # 정답 길이
    length = len(number) - k

    while k > 0:
        idx = 0
        max_val = 0

        for i in range(len(reverse_num) - 1 - k, len(reverse_num)):
            if int(reverse_num[i]) >= max_val:
                max_val = int(reverse_num[i])
                idx = i

        left += str(max_val)
        k -= abs(len(reverse_num) - len(reverse_num[:idx]) - 1)
        reverse_num = reverse_num[:idx]

        if len(reverse_num) == length - len(left):
            print(len(reverse_num), len(number), k, len(left))
            return left + reverse_num[::-1]

    return left + reverse_num[::-1]


# 틀림
# def solution(number, k):

#     left = ""
#     while k > 0:
#         max_val = 0
#         idx = 0
#         for i in range(0, len(number) - k + 1):
#             max_candidate = int(number[i : i + len(number) - k])
#             if max_candidate >= max_val:
#                 max_val = max_candidate
#                 idx = i
#         left += number[idx]
#         number = number[idx + 1 :]
#         k -= idx

#     return left + number


number = "4177252841"
k = 1
# number = "1924"
# k = 2
print(solution(number, k))
