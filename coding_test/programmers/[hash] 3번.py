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
