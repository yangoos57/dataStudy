# 배울점
# 순환 해야하는 문제는 나머지를 계산해야하는 문제다.


def solution(s, skip, index):
    item = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    for i in skip:
        item.pop(item.index(i))
    len_item = len(item)
    answer = ""
    for i in s:
        if item.index(i) + index < len_item:
            answer += item[item.index(i) + index]
        else:
            answer += item[(item.index(i) + index) % (len_item)]
    return answer


s = "aukks"
skip = "wbqd"
index = 5


solution(s, skip, index)
