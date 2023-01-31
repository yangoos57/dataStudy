### Programmers hash 3

# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.
# 같은게 있으면 False 없으면 True
# 어떤 번호가 다른 번호의 접두어인 경우

# 배운점
# phone_book.sort(key=lambda x: x * 20)
# 이렇게 할 경우 작은 숫자가 뒤로 가는 문제 발생


def solution(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][0 : len(phone_book[i])]:
            return False
    return True


nums = ["119", "97674223", "1195524421"]
nums = ["123", "456", "789"]
nums = ["12", "123", "1235", "567", "88"]
nums = ["12", "124", "1253", "567", "88"]

print(solution(nums))


### 2023-01-31 다시 풀었음

# 아래의 식은 13번 예시에서 오류가 발생했음
# 문제에서 요구하는 내용은 접두사가 동일한지를 판별하는 것이었지만
# in을 사용함으로써 접두사 뿐만 아니라 문자열 전체를 판별하는 것으로 만들었음.


def solution(lst):
    # 리스트를 정렬하는게 1번인듯
    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i] in lst[i + 1]:
            return False
    return True
