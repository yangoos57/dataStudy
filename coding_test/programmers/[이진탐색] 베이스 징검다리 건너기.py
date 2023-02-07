## 징검다리 건너기
# https://school.programmers.co.kr/learn/courses/30/lessons/64062

# def solution(stones, k):
#     answer = 0
#     left = 1
#     right = max(stones)
    
#     while left <= right:
#         count = 0
#         mid = (left+right) // 2

#         # 조건을 만족하는지 보자 .
#         for s in stones:
#             if s - mid <= 0:
#                 count += 1
#             else:
#                 count = 0
            
#             if count == k:
#                 break
        
#         if count < k:
#             left = mid +1
#         else:
#             right = mid -1
#             answer = mid
    
        
#     return answer


def bin_search(items, search_num ) :
    left = min(items)
    right = max(items)

    while left <= right :
        middle = (left + right) // 2

        # 조건식
        count = 0
        for i in range(4) :
            count += 1

        if count < search_num :
            # left or right = mid +-1
        else :
            result = middle
            # left or right = mid +-1